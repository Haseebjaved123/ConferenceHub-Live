# 📅 ConferenceHub-Live

Automated tracker for upcoming academic conferences with focus on BK21-listed venues. Updates daily to show only upcoming deadlines, sorted by nearest deadline first.

## Template Format
```
Conference Name | Abstract Deadline | Paper Deadline | Notification | Camera-Ready | Event Date | Location | Website | Acceptance Rate | Tags
```

## Upcoming Conferences
*Auto-updated daily - only shows upcoming deadlines*

<!-- BEGIN:UPCOMING-CONFS -->
| # | Conference | Abstract | Paper | Notification | Camera-Ready | Event | Location | Website | Acceptance | Tags |
|---|---|---|---|---|---|---|---|---|---|---|
| No upcoming conferences found | | | | | | | | | | |
<!-- END:UPCOMING-CONFS -->

## Data Sources
- **Manual Seeds**: Curated list of important conferences
- **BK21 List**: BK21-approved venues for Korean researchers  
- **Acceptance Rates**: Historical acceptance rate data
- **Live APIs**: 
  - OpenReview.net (comprehensive venue search)
  - WikiCFP (expanded field coverage)
  - Conference Alerts (workshops & symposiums)
  - AllConferences.com (global conference database)
  - IEEE Xplore (academic conferences)
  - ACM Digital Library (computer science venues)
  - ResearchGate (research community events)
  - Google Scholar (academic conference search)
- **Auto-filtering**: Past deadlines automatically hidden

## How It Works
1. Daily GitHub Action fetches latest conference data
2. Merges multiple sources and validates dates
3. Filters out past deadlines (abstract OR paper)
4. Sorts by nearest upcoming deadline
5. Updates this README automatically

*Last updated: Auto-refreshed daily*
