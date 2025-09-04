# 📅 ConferenceHub-Live

Automated tracker for upcoming academic conferences with focus on BK21-listed venues. Updates daily to show only upcoming deadlines, sorted by nearest deadline first.

## Upcoming Conferences
*🔄 Live updates every 6 hours | Last updated: 2025-01-04 22:15 KST (2025-01-04 13:15 UTC) | Next update: Auto-refreshing*

<!-- BEGIN:UPCOMING-CONFS -->
| # | Conference | Abstract | Paper | Notification | Camera-Ready | Event | Location | Website | Acceptance | Tags | Time Left |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | International Conference on Machine Learning (ICML) | 2025-01-15 | 2025-01-22 | 2025-04-15 | 2025-05-15 | 2025-07-21 | Philadelphia, USA | [Link](https://icml.cc/Conferences/2025) | 26% | T1, BK21 | 11 days left |
| 2 | International Joint Conference on Artificial Intelligence (IJCAI) | 2025-01-15 | 2025-01-22 | 2025-04-15 | 2025-05-15 | 2025-08-09 | Seoul, Korea | [Link](https://ijcai.org/) | 15.2% | T1, BK21 | 11 days left |
| 3 | Association for Computational Linguistics (ACL) | 2025-01-15 | 2025-01-22 | 2025-04-15 | 2025-05-15 | 2025-07-28 | Bangkok, Thailand | [Link](https://2025.aclweb.org/) | 19.2% | T1, BK21 | 11 days left |
| 4 | European Conference on Computer Vision (ECCV) | 2025-02-15 | 2025-02-22 | 2025-05-15 | 2025-06-15 | 2025-09-29 | Milan, Italy | [Link](https://eccv2025.ecva.net/) | 20.8% | T1, BK21 | 1 month left |
| 5 | International Conference on Computer Vision (ICCV) | 2025-03-15 | 2025-03-22 | 2025-06-15 | 2025-07-15 | 2025-10-04 | Paris, France | [Link](https://iccv2025.thecvf.com/) | 21.3% | T1, BK21 | 2 months left |
| 6 | Conference on Neural Information Processing Systems (NeurIPS) | 2025-05-15 | 2025-05-22 | 2025-09-15 | 2025-10-15 | 2025-12-08 | Vancouver, Canada | [Link](https://neurips.cc/Conferences/2025) | 25.8% | T1, BK21 | 4 months left |
| 7 | Empirical Methods in Natural Language Processing (EMNLP) | 2025-05-15 | 2025-05-22 | 2025-08-15 | 2025-09-15 | 2025-11-17 | Singapore | [Link](https://2025.emnlp.org/) | 18.7% | T1, BK21 | 4 months left |
| 8 | International Conference on Learning Representations (ICLR) | 2025-09-15 | 2025-09-22 | 2025-12-15 | 2026-01-15 | 2026-05-04 | Vienna, Austria | [Link](https://iclr.cc/Conferences/2026) | 31.8% | T1, BK21 | 8 months left |
| 9 | AAAI Conference on Artificial Intelligence | 2025-08-15 | 2025-08-22 | 2025-11-15 | 2025-12-15 | 2026-02-22 | Seattle, USA | [Link](https://aaai.org/aaai-conference/) | 23.5% | T1, BK21 | 7 months left |
| 10 | Computer Vision and Pattern Recognition (CVPR) | 2025-11-15 | 2025-11-22 | 2026-02-15 | 2026-03-15 | 2026-06-17 | Seattle, USA | [Link](https://cvpr2026.thecvf.com/) | 22.1% | T1, BK21 | 10 months left |
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
