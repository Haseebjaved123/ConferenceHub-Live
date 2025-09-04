# ConferenceHub-Live Project Summary

## 🎯 Project Overview

**ConferenceHub-Live** is an automated conference tracking system that maintains an up-to-date list of upcoming academic conferences, with special focus on BK21-listed venues. The system automatically updates daily and shows only upcoming deadlines, sorted by nearest deadline first.

## 📁 Project Structure

```
ConferenceHub-Live/
├── README.md                    # Main documentation with live conference table
├── update_conferences.py        # Core update script
├── requirements.txt             # Python dependencies
├── config.json                  # Configuration settings
├── setup.py                     # Setup script
├── test_update.py               # Test script
├── run_update.bat               # Windows batch file
├── USAGE.md                     # Detailed usage guide
├── LLM_QUERY_TEMPLATE.md        # Templates for LLM queries
├── PROJECT_SUMMARY.md           # This file
├── .gitignore                   # Git ignore rules
├── .github/workflows/           # GitHub Actions
│   └── update-conferences.yml   # Daily update workflow
└── data/                        # Data sources
    ├── manual_seeds.csv         # Curated conferences (15 entries)
    ├── bk21_list.csv            # BK21 venues (40+ entries)
    └── acceptance_rates.csv     # Historical rates (40+ entries)
```

## 🚀 Key Features

### ✅ Automated Updates
- **Daily GitHub Action** runs at 3:00 AM UTC (12:00 PM KST)
- **Manual trigger** available in GitHub Actions tab
- **Auto-commit** changes to README.md

### ✅ Smart Filtering
- **Past deadlines hidden** automatically
- **Upcoming conferences only** displayed
- **Sorted by nearest deadline** first
- **Compact table format** to save space

### ✅ Multiple Data Sources
- **Manual Seeds**: 15 curated top-tier conferences
- **BK21 List**: 40+ BK21-approved venues
- **Acceptance Rates**: Historical data for 40+ venues
- **API Integration**: OpenReview and WikiCFP

### ✅ BK21 Focus
- **Automatic tagging** of BK21 conferences
- **Priority display** for BK21 venues
- **Comprehensive list** of approved venues

## 📊 Data Coverage

### Conference Types
- **AI/ML**: ICML, NeurIPS, AAAI, IJCAI, ICLR
- **Computer Vision**: CVPR, ECCV, ICCV
- **NLP**: ACL, EMNLP, NAACL, CoNLL
- **Data Mining**: KDD, ICDM
- **Software Engineering**: ICSE, FSE, ASE
- **Systems**: SIGCOMM, INFOCOM, OSDI, SOSP
- **HCI**: CHI, UIST

### Information Included
- Conference name and acronym
- Abstract and paper submission deadlines
- Notification and camera-ready dates
- Event dates and locations
- Official websites and submission URLs
- Acceptance rates with year context
- BK21 and other tags

## 🛠️ Technical Implementation

### Core Script (`update_conferences.py`)
- **Date parsing** with multiple format support
- **API integration** for OpenReview and WikiCFP
- **Data merging** from multiple sources
- **Smart filtering** for upcoming conferences
- **Markdown table generation**
- **README update** with proper formatting

### GitHub Actions Workflow
- **Daily schedule** with cron job
- **Python environment** setup
- **Dependency installation**
- **Automatic execution**
- **Change detection** and commit

### Configuration System
- **JSON config** for easy customization
- **API settings** and timeouts
- **Filtering criteria**
- **Output formatting** options

## 📋 Usage Instructions

### Quick Start
1. **Install dependencies**: `pip install -r requirements.txt`
2. **Run update**: `python update_conferences.py`
3. **Check results**: View updated table in README.md

### Windows Users
- Use `run_update.bat` for easy execution
- Double-click to run with automatic setup

### Adding Conferences
1. **Edit CSV**: Add to `data/manual_seeds.csv`
2. **Use template**: Follow format in USAGE.md
3. **Run update**: Execute update script
4. **Verify results**: Check README.md

## 🔧 Customization

### Configuration (`config.json`)
- **API settings**: Enable/disable sources, timeouts
- **Filtering**: Date ranges, venue types
- **Output**: Display limits, formatting options

### Data Sources
- **Manual seeds**: Add your own conferences
- **BK21 list**: Update approved venues
- **Acceptance rates**: Add recent data

### LLM Integration
- **Query templates**: Use LLM_QUERY_TEMPLATE.md
- **Data validation**: Verify information accuracy
- **Bulk updates**: Add multiple conferences

## 📈 Benefits

### For Researchers
- **Never miss deadlines** with daily updates
- **BK21 focus** for Korean researchers
- **Comprehensive coverage** of top venues
- **Acceptance rate data** for planning

### For Institutions
- **Automated maintenance** reduces manual work
- **Consistent formatting** across all entries
- **Multiple data sources** ensure accuracy
- **Easy customization** for specific needs

### For Community
- **Open source** and freely available
- **Easy to contribute** with clear templates
- **Well documented** with usage guides
- **Extensible** for additional features

## 🎯 Next Steps

1. **Push to GitHub** to enable automated updates
2. **Add more conferences** to manual_seeds.csv
3. **Customize configuration** in config.json
4. **Monitor daily updates** via GitHub Actions
5. **Contribute improvements** via pull requests

## 📞 Support

- **Documentation**: Check USAGE.md for detailed instructions
- **Templates**: Use LLM_QUERY_TEMPLATE.md for data collection
- **Issues**: Open GitHub issues for problems or suggestions
- **Contributions**: Submit pull requests for improvements

---

**ConferenceHub-Live** - Keeping researchers ahead of conference deadlines! 🚀
