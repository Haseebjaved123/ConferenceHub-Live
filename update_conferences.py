#!/usr/bin/env python3
"""
Automated Conference Tracker
Updates README.md with upcoming conferences from multiple sources.
Filters out past deadlines and sorts by nearest upcoming deadline.
"""

import argparse
import datetime as dt
import json
import os
import re
import requests
from dataclasses import dataclass
from typing import List, Optional, Dict, Any
import pandas as pd
from bs4 import BeautifulSoup
import time

# Configuration
DATA_DIR = "data"
COLUMNS = [
    "ConferenceName", "AbstractDeadline", "PaperDeadline", "Notification", 
    "CameraReady", "EventDate", "Location", "Website", "AcceptanceRate", "Tags", "Source"
]
DATE_COLS = ["AbstractDeadline", "PaperDeadline", "Notification", "CameraReady", "EventDate"]

def parse_date(date_str: Optional[str]) -> Optional[dt.datetime]:
    """Parse various date formats to datetime object."""
    if not date_str or str(date_str).strip() == "":
        return None
    
    formats = [
        "%Y-%m-%d", "%Y/%m/%d", "%d-%m-%Y", "%d/%m/%Y", 
        "%Y-%m-%d %H:%M:%S", "%Y-%m-%dT%H:%M:%S"
    ]
    
    for fmt in formats:
        try:
            return dt.datetime.strptime(str(date_str).strip(), fmt)
        except ValueError:
            continue
    
    try:
        return pd.to_datetime(date_str).to_pydatetime()
    except:
        return None

def get_primary_deadline(row: pd.Series) -> Optional[dt.datetime]:
    """Get the earliest upcoming deadline (abstract or paper)."""
    abstract = parse_date(row.get("AbstractDeadline"))
    paper = parse_date(row.get("PaperDeadline"))
    
    deadlines = [d for d in [abstract, paper] if d is not None]
    return min(deadlines) if deadlines else None

def load_csv_safe(filepath: str) -> pd.DataFrame:
    """Safely load CSV file, return empty DataFrame if not found."""
    if not os.path.exists(filepath):
        return pd.DataFrame(columns=COLUMNS)
    
    try:
        df = pd.read_csv(filepath)
        # Ensure all required columns exist
        for col in COLUMNS:
            if col not in df.columns:
                df[col] = ""
        return df[COLUMNS]
    except Exception as e:
        print(f"Warning: Could not load {filepath}: {e}")
        return pd.DataFrame(columns=COLUMNS)

def fetch_openreview_conferences() -> pd.DataFrame:
    """Fetch conference data from OpenReview API."""
    rows = []
    try:
        # OpenReview public API for venues
        url = "https://api.openreview.net/venues"
        response = requests.get(url, timeout=30)
        
        if response.status_code == 200:
            data = response.json()
            venues = data.get("venues", [])
            
            for venue in venues[:50]:  # Limit to avoid too many results
                name = venue.get("name", "")
                if "2025" in name or "2024" in name:  # Focus on current/recent years
                    rows.append({
                        "ConferenceName": name,
                        "AbstractDeadline": "",
                        "PaperDeadline": "",
                        "Notification": "",
                        "CameraReady": "",
                        "EventDate": "",
                        "Location": "",
                        "Website": f"https://openreview.net/group?id={venue.get('id', '')}",
                        "AcceptanceRate": "",
                        "Tags": "OpenReview",
                        "Source": "openreview"
                    })
    except Exception as e:
        print(f"Warning: OpenReview fetch failed: {e}")
    
    return pd.DataFrame(rows, columns=COLUMNS)

def fetch_wikicfp_conferences() -> pd.DataFrame:
    """Fetch conference data from WikiCFP."""
    rows = []
    queries = ["machine learning", "computer vision", "artificial intelligence", "data mining"]
    
    for query in queries:
        try:
            url = f"http://www.wikicfp.com/cfp/servlet/tool.search?q={query}&year=t"
            response = requests.get(url, timeout=20)
            
            if response.status_code == 200:
                soup = BeautifulSoup(response.text, 'html.parser')
                
                # Find conference links
                for link in soup.find_all('a', href=re.compile(r'eventid')):
                    title = link.get_text().strip()
                    if title and ("2025" in title or "2024" in title):
                        cfp_url = "http://www.wikicfp.com" + link.get('href', '')
                        rows.append({
                            "ConferenceName": title,
                            "AbstractDeadline": "",
                            "PaperDeadline": "",
                            "Notification": "",
                            "CameraReady": "",
                            "EventDate": "",
                            "Location": "",
                            "Website": cfp_url,
                            "AcceptanceRate": "",
                            "Tags": "WikiCFP",
                            "Source": "wikicfp"
                        })
            
            time.sleep(1)  # Be respectful to the server
        except Exception as e:
            print(f"Warning: WikiCFP fetch failed for {query}: {e}")
    
    return pd.DataFrame(rows, columns=COLUMNS)

def tag_bk21_conferences(df: pd.DataFrame, bk21_df: pd.DataFrame) -> pd.DataFrame:
    """Tag conferences with BK21 status."""
    if bk21_df.empty:
        return df
    
    bk21_venues = set(bk21_df['Acronym'].dropna().str.upper().unique())
    
    def add_bk21_tag(row):
        current_tags = str(row.get('Tags', '')).strip()
        conf_name = str(row.get('ConferenceName', '')).upper()
        
        # Check if conference name contains any BK21 venue
        for venue in bk21_venues:
            if venue in conf_name:
                if current_tags:
                    return f"{current_tags}, BK21"
                return "BK21"
        return current_tags
    
    df['Tags'] = df.apply(add_bk21_tag, axis=1)
    return df

def attach_acceptance_rates(df: pd.DataFrame, acc_df: pd.DataFrame) -> pd.DataFrame:
    """Attach acceptance rate data to conferences."""
    if acc_df.empty:
        return df
    
    # Create lookup dictionary
    acc_lookup = {}
    for _, row in acc_df.iterrows():
        venue = str(row.get('Venue', '')).upper()
        year = str(row.get('Year', ''))
        rate = row.get('AcceptanceRatePercent', '')
        key = f"{venue}|{year}"
        acc_lookup[key] = rate
    
    def lookup_acceptance_rate(row):
        conf_name = str(row.get('ConferenceName', '')).upper()
        year = str(row.get('EventDate', ''))[:4] if row.get('EventDate') else ""
        
        # Try exact match first
        key = f"{conf_name}|{year}"
        if key in acc_lookup:
            return f"{year}:{acc_lookup[key]}%"
        
        # Try partial matches
        for lookup_key, rate in acc_lookup.items():
            venue_part = lookup_key.split('|')[0]
            if venue_part in conf_name and len(venue_part) > 3:
                year_part = lookup_key.split('|')[1]
                return f"{year_part}:{rate}%"
        
        return row.get('AcceptanceRate', '')
    
    df['AcceptanceRate'] = df.apply(lookup_acceptance_rate, axis=1)
    return df

def filter_upcoming_conferences(df: pd.DataFrame) -> pd.DataFrame:
    """Filter to only upcoming conferences and sort by deadline."""
    if df.empty:
        return df
    
    today = dt.datetime.now()
    upcoming = []
    
    for _, row in df.iterrows():
        primary_deadline = get_primary_deadline(row)
        
        # Include if deadline is in the future or no deadline specified
        if primary_deadline is None or primary_deadline >= today:
            upcoming.append(row)
    
    if not upcoming:
        return pd.DataFrame(columns=COLUMNS)
    
    # Convert back to DataFrame and sort by primary deadline
    upcoming_df = pd.DataFrame(upcoming)
    upcoming_df['PrimaryDeadline'] = upcoming_df.apply(get_primary_deadline, axis=1)
    
    # Sort by deadline (None values go to end)
    upcoming_df = upcoming_df.sort_values('PrimaryDeadline', na_position='last')
    upcoming_df = upcoming_df.drop('PrimaryDeadline', axis=1)
    
    return upcoming_df

def format_markdown_table(df: pd.DataFrame) -> str:
    """Convert DataFrame to markdown table format."""
    if df.empty:
        return """| # | Conference | Abstract | Paper | Notification | Camera-Ready | Event | Location | Website | Acceptance | Tags |
|---|---|---|---|---|---|---|---|---|---|---|
| No upcoming conferences found | | | | | | | | | | |"""
    
    lines = [
        "| # | Conference | Abstract | Paper | Notification | Camera-Ready | Event | Location | Website | Acceptance | Tags |",
        "|---|---|---|---|---|---|---|---|---|---|---|"
    ]
    
    for i, (_, row) in enumerate(df.iterrows(), 1):
        def format_date(date_str):
            if not date_str:
                return ""
            date_obj = parse_date(date_str)
            return date_obj.strftime("%Y-%m-%d") if date_obj else str(date_str)
        
        def format_links(website):
            if not website:
                return ""
            return f"[Link]({website})"
        
        # Truncate long conference names
        conf_name = str(row.get('ConferenceName', ''))[:60]
        if len(str(row.get('ConferenceName', ''))) > 60:
            conf_name += "..."
        
        lines.append(
            f"| {i} | {conf_name} | {format_date(row.get('AbstractDeadline'))} | "
            f"{format_date(row.get('PaperDeadline'))} | {format_date(row.get('Notification'))} | "
            f"{format_date(row.get('CameraReady'))} | {format_date(row.get('EventDate'))} | "
            f"{row.get('Location', '')} | {format_links(row.get('Website'))} | "
            f"{row.get('AcceptanceRate', '')} | {row.get('Tags', '')} |"
        )
    
    return "\n".join(lines)

def update_readme(readme_path: str, table_content: str):
    """Update README.md with new conference table."""
    try:
        with open(readme_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Find and replace the table section
        start_marker = "<!-- BEGIN:UPCOMING-CONFS -->"
        end_marker = "<!-- END:UPCOMING-CONFS -->"
        
        pattern = re.compile(
            re.escape(start_marker) + r'.*?' + re.escape(end_marker),
            re.DOTALL
        )
        
        new_section = f"{start_marker}\n{table_content}\n{end_marker}"
        
        if pattern.search(content):
            content = pattern.sub(new_section, content)
        else:
            # If markers not found, append to end
            content += f"\n\n{new_section}\n"
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"✅ Updated {readme_path} successfully")
        
    except Exception as e:
        print(f"❌ Error updating README: {e}")

def main():
    parser = argparse.ArgumentParser(description="Update conference information in README")
    parser.add_argument("--readme", default="README.md", help="Path to README.md file")
    parser.add_argument("--data-dir", default=DATA_DIR, help="Data directory path")
    args = parser.parse_args()
    
    print("🔄 Starting conference update...")
    
    # Load data sources
    print("📂 Loading data sources...")
    manual_df = load_csv_safe(os.path.join(args.data_dir, "manual_seeds.csv"))
    bk21_df = load_csv_safe(os.path.join(args.data_dir, "bk21_list.csv"))
    acc_df = load_csv_safe(os.path.join(args.data_dir, "acceptance_rates.csv"))
    
    # Fetch from APIs
    print("🌐 Fetching from APIs...")
    openreview_df = fetch_openreview_conferences()
    wikicfp_df = fetch_wikicfp_conferences()
    
    # Combine all sources
    print("🔗 Combining data sources...")
    all_conferences = pd.concat([
        manual_df, openreview_df, wikicfp_df
    ], ignore_index=True)
    
    # Clean and process data
    print("🧹 Processing data...")
    for col in COLUMNS:
        if col not in all_conferences.columns:
            all_conferences[col] = ""
        all_conferences[col] = all_conferences[col].fillna("")
    
    # Apply enhancements
    all_conferences = tag_bk21_conferences(all_conferences, bk21_df)
    all_conferences = attach_acceptance_rates(all_conferences, acc_df)
    
    # Filter and sort
    print("📅 Filtering upcoming conferences...")
    upcoming_df = filter_upcoming_conferences(all_conferences)
    
    # Generate markdown table
    print("📝 Generating markdown table...")
    table_md = format_markdown_table(upcoming_df)
    
    # Update README
    print("📄 Updating README...")
    update_readme(args.readme, table_md)
    
    print(f"✅ Complete! Found {len(upcoming_df)} upcoming conferences")
    print(f"📊 Sources: {len(manual_df)} manual, {len(openreview_df)} OpenReview, {len(wikicfp_df)} WikiCFP")

if __name__ == "__main__":
    main()
