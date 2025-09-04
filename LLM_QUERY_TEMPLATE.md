# LLM Query Template for Conference Data

Use this template to query LLMs for conference information:

## Basic Query Template

```
Generate a structured list of upcoming academic conferences in the following format:

Conference Name | Abstract Deadline | Paper Deadline | Notification | Camera-Ready | Event Date | Location | Website | Acceptance Rate | Tags

Focus on:
- BK21-listed conferences (ICML, NeurIPS, AAAI, IJCAI, CVPR, ECCV, ICCV, ICLR, ACL, EMNLP, etc.)
- Top-tier venues in AI, ML, CV, NLP, Data Mining, Software Engineering
- Conferences with deadlines in the next 12 months
- Include acceptance rates when available
- Provide official websites and submission links

Example format:
International Conference on Machine Learning (ICML) | 2025-01-15 | 2025-01-22 | 2025-04-15 | 2025-05-15 | 2025-07-21 | Philadelphia USA | https://icml.cc/ | 2024:26% | BK21

Please provide at least 20 conferences with complete information.
```

## Advanced Query Template

```
I need comprehensive conference data for an automated tracking system. Please provide:

1. **Conference List** in this exact CSV format:
"Conference Name","Abstract Deadline","Paper Deadline","Notification","Camera Ready","Event Date","Location","Website","Acceptance Rate","Tags","Source"

2. **Requirements:**
- Focus on BK21-approved venues and top-tier conferences
- Include AI, ML, CV, NLP, Data Mining, Software Engineering, HCI, Systems conferences
- Only conferences with deadlines in 2025-2026
- Provide accurate dates in YYYY-MM-DD format
- Include acceptance rates with year (e.g., "2024:26%")
- Tag BK21 conferences appropriately
- Provide official websites and submission URLs

3. **Priority Venues:**
- ICML, NeurIPS, AAAI, IJCAI, CVPR, ECCV, ICCV, ICLR
- ACL, EMNLP, NAACL, CoNLL
- KDD, ICDM, WWW, SIGIR
- ICSE, FSE, ASE, OOPSLA, PLDI, POPL
- CHI, UIST, MobiCom, SIGCOMM, INFOCOM

4. **Data Quality:**
- Verify all dates are accurate and in the future
- Ensure websites are accessible and official
- Double-check acceptance rates are recent
- Include both abstract and paper deadlines when available

Please provide at least 30 conferences with complete, verified information.
```

## Specific Field Queries

### For BK21 Conferences Only:
```
List all BK21-approved academic conferences with upcoming deadlines. Include:
- Conference name and acronym
- Abstract and paper submission deadlines
- Notification and camera-ready dates
- Event dates and locations
- Official websites
- Recent acceptance rates
- Focus on A+ and A ranked venues
```

### For Acceptance Rates:
```
Provide recent acceptance rates (2023-2024) for major AI/ML conferences:
- ICML, NeurIPS, AAAI, IJCAI
- CVPR, ECCV, ICCV, ICLR
- ACL, EMNLP, NAACL
- KDD, ICDM, WWW
- ICSE, FSE, CHI

Format: Conference | Year | Acceptance Rate
Example: ICML | 2024 | 26%
```

### For Conference Websites:
```
Find official websites and submission URLs for these conferences:
[List of conference names]

For each conference, provide:
- Official conference website
- Call for papers (CFP) URL
- Submission system URL
- Contact information if available
```

## Data Validation Queries

```
Verify the accuracy of this conference data:
[List of conferences with dates and details]

Please check:
1. Are the dates correct and in the future?
2. Are the websites accessible and official?
3. Are the acceptance rates recent and accurate?
4. Are the locations and venues correct?
5. Are there any missing or incorrect details?

Provide corrections for any inaccurate information.
```

## Usage Instructions

1. **Copy the appropriate template** based on your needs
2. **Customize the query** with specific requirements
3. **Run the query** with your preferred LLM
4. **Validate the results** before adding to your system
5. **Update your CSV files** with the new data

## Tips for Better Results

- Be specific about date formats (YYYY-MM-DD)
- Request verification of information
- Ask for multiple sources when possible
- Specify the time range (e.g., "next 12 months")
- Include quality requirements (official websites, recent data)
- Request both abstract and paper deadlines
- Ask for acceptance rates with year context
