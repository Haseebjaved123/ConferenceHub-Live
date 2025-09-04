# 📅 ConferenceHub-Live

Automated tracker for upcoming academic conferences with focus on BK21-listed venues. Updates daily to show only upcoming deadlines, sorted by nearest deadline first.

## Upcoming Conferences
*🔄 Live updates every 6 hours | Next update: Auto-refreshing | Korea Time (KST) | AOE (Anywhere on Earth)*

<!-- BEGIN:UPCOMING-CONFS -->
| # | Conference | Abstract | Paper | Notification | Camera-Ready | Event | Location | Website | Acceptance | Tags |
|---|---|---|---|---|---|---|---|---|---|---|
| No upcoming conferences found | | | | | | | | | | |
<!-- END:UPCOMING-CONFS -->

## Data Sources
- **Manual Seeds**: 50+ curated top-tier conferences with real deadlines
- **BK21 List**: BK21-approved venues for Korean researchers  
- **Acceptance Rates**: Historical acceptance rate data
- **Live APIs (8 real sources)**: 
  - OpenReview.net (comprehensive venue search)
  - WikiCFP (expanded field coverage + detailed parsing)
  - Conference Alerts (workshops & symposiums)
  - AllConferences.com (global conference database)
  - IEEE Xplore (academic conferences)
  - ACM Digital Library (computer science venues)
  - ResearchGate (research community events)
  - Google Scholar (academic conference search)
- **Auto-filtering**: Past deadlines automatically hidden
- **Live Updates**: Every 6 hours with Korea Time (KST) and UTC timestamps

## How It Works
1. Daily GitHub Action fetches latest conference data
2. Merges multiple sources and validates dates
3. Filters out past deadlines (abstract OR paper)
4. Sorts by nearest upcoming deadline
5. Updates this README automatically

*Last updated: Auto-refreshed daily*
