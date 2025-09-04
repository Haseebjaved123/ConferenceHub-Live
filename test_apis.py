#!/usr/bin/env python3
"""
Test script to check which APIs actually work
"""

import requests
import time

def test_api(url, name, timeout=10):
    """Test if an API endpoint is accessible"""
    try:
        print(f"Testing {name}...")
        response = requests.get(url, timeout=timeout)
        print(f"  {name}: {response.status_code} - {'✅ Working' if response.status_code == 200 else '❌ Failed'}")
        return response.status_code == 200
    except Exception as e:
        print(f"  {name}: ❌ Error - {str(e)[:50]}...")
        return False

def main():
    print("🔍 Testing Conference APIs...")
    print("=" * 50)
    
    # Test real APIs that should work
    working_apis = []
    
    # Test OpenReview
    if test_api("https://api.openreview.net/venues", "OpenReview"):
        working_apis.append("OpenReview")
    
    # Test WikiCFP
    if test_api("http://www.wikicfp.com/cfp/servlet/tool.search?q=machine+learning&year=t", "WikiCFP"):
        working_apis.append("WikiCFP")
    
    # Test Google Scholar (might be blocked)
    if test_api("https://scholar.google.com/scholar?q=conference+2025", "Google Scholar"):
        working_apis.append("Google Scholar")
    
    # Test some conference websites
    if test_api("https://conferencealerts.com", "Conference Alerts"):
        working_apis.append("Conference Alerts")
    
    if test_api("https://allconferences.com", "AllConferences"):
        working_apis.append("AllConferences")
    
    # Test IEEE (might need API key)
    if test_api("https://ieeexplore.ieee.org", "IEEE Xplore"):
        working_apis.append("IEEE Xplore")
    
    # Test ACM
    if test_api("https://dl.acm.org", "ACM Digital Library"):
        working_apis.append("ACM Digital Library")
    
    print("\n" + "=" * 50)
    print(f"✅ Working APIs: {len(working_apis)}")
    for api in working_apis:
        print(f"  - {api}")
    
    print(f"\n❌ Non-working APIs: {15 - len(working_apis)}")
    print("  - Many of the APIs I added don't actually exist or require authentication")
    print("  - Need to focus on real, working APIs")
    
    return working_apis

if __name__ == "__main__":
    working = main()
