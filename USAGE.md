# ConferenceHub-Live Usage Guide

## Quick Start

1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the update:**
   ```bash
   python update_conferences.py
   ```

3. **Check results:**
   - Open `README.md` to see the updated conference table
   - Only upcoming conferences are shown, sorted by nearest deadline

## Data Sources

### Manual Seeds (`data/manual_seeds.csv`)
Curated list of important conferences with complete information:
- Conference name, deadlines, location, website
- Acceptance rates and tags
- Source: manual

### BK21 List (`data/bk21_list.csv`)
BK21-approved venues for Korean researchers:
- Venue acronyms and full names
- Field classification and ranking
- Used for automatic tagging

### Acceptance Rates (`data/acceptance_rates.csv`)
Historical acceptance rate data:
- Venue, year, acceptance rate percentage
- Used to populate acceptance rate column

### API Sources
- **OpenReview**: Fetches conference metadata
- **WikiCFP**: Scrapes conference call for papers

## Configuration

Edit `config.json` to customize:
- API timeouts and limits
- Filtering criteria
- Output formatting
- Data source paths

## Template Format

Each conference entry follows this format:
```
Conference Name | Abstract Deadline | Paper Deadline | Notification | Camera-Ready | Event Date | Location | Website | Acceptance Rate | Tags
```

### Example Entry:
```
International Conference on Machine Learning (ICML) | 2025-01-15 | 2025-01-22 | 2025-04-15 | 2025-05-15 | 2025-07-21 | Philadelphia USA | https://icml.cc/ | 2024:26% | BK21
```

## Adding New Conferences

### Method 1: Edit CSV directly
1. Open `data/manual_seeds.csv`
2. Add new row with conference details
3. Run update script

### Method 2: Use template
Copy this template and fill in details:
```csv
"Conference Name","Abstract Deadline","Paper Deadline","Notification","Camera Ready","Event Date","Location","Website","Acceptance Rate","Tags","Source"
"Your Conference","2025-XX-XX","2025-XX-XX","2025-XX-XX","2025-XX-XX","2025-XX-XX","Location","https://website.com","Year:XX%","Tag","manual"
```

## Automated Updates

The system runs automatically via GitHub Actions:
- **Schedule**: Daily at 3:00 AM UTC (12:00 PM KST)
- **Manual trigger**: Available in GitHub Actions tab
- **Auto-commit**: Changes are automatically committed and pushed

## Troubleshooting

### Common Issues

1. **No conferences showing:**
   - Check if dates are in the future
   - Verify CSV format is correct
   - Run with debug output

2. **API errors:**
   - Check internet connection
   - Verify API endpoints are accessible
   - Check timeout settings in config

3. **Date parsing errors:**
   - Use YYYY-MM-DD format
   - Ensure dates are valid
   - Check for extra spaces or characters

### Debug Mode
Run with verbose output:
```bash
python update_conferences.py --readme README.md --data-dir data
```

## File Structure

```
ConferenceHub-Live/
├── README.md                 # Main documentation with conference table
├── update_conferences.py     # Main update script
├── requirements.txt          # Python dependencies
├── config.json              # Configuration settings
├── setup.py                 # Setup script
├── test_update.py           # Test script
├── .github/workflows/       # GitHub Actions
│   └── update-conferences.yml
├── data/                    # Data sources
│   ├── manual_seeds.csv     # Curated conferences
│   ├── bk21_list.csv        # BK21 venues
│   └── acceptance_rates.csv # Historical rates
└── .gitignore              # Git ignore rules
```

## Contributing

1. Fork the repository
2. Add conferences to `data/manual_seeds.csv`
3. Test with `python update_conferences.py`
4. Submit pull request

## Support

For issues or questions:
1. Check this documentation
2. Review error messages
3. Test with sample data
4. Open GitHub issue with details
