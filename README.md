# User Growth & Funnel Optimization Analysis

**Tools:** Python, SQL (BigQuery), Pandas, Matplotlib, Seaborn, SciPy  
**Dataset:** [Google Analytics Sample](https://console.cloud.google.com/marketplace/details/obfuscated-ga360-data/obfuscated-ga360-data) — BigQuery Public Data  
**Portfolio:** [miriamgarcia.org](https://miriamgarcia.org)

---

## Overview

Analysis of 12 months of real web analytics data from the Google Merchandise Store, focused on user growth, acquisition channel performance, device behavior, and conversion funnel optimization. Includes a simulated A/B test for a mobile checkout intervention with statistical significance testing.

## Key Findings

| Finding | Insight |
|---------|---------|
| Mobile CVR gap | Mobile drives significant traffic but converts 5-10x below desktop |
| Organic quality | Organic search delivers highest revenue per session |
| Funnel drop-off | Large bounce volume indicates top-of-funnel engagement problem |
| A/B test result | 20% relative CVR lift on mobile is statistically significant (p < 0.05) |

## Visualizations

![KPI Dashboard]
![Monthly Growth]
![Channel Analysis]
![Device Analysis]
![Conversion Funnel]
![A/B Test Results]

## Repo Structure

```
ga-user-growth-funnel/
├── GA_User_Growth_Funnel_Analysis.ipynb
├── ga_analysis.py
├── images/
└── README.md
```

## Setup

```bash
git clone https://github.com/magg6789/ga-user-growth-funnel.git
cd ga-user-growth-funnel
pip install pandas numpy matplotlib seaborn scipy
```

Export the dataset from BigQuery:
```sql
SELECT
  fullVisitorId, visitId, date, channelGrouping,
  device.deviceCategory AS device_category,
  device.operatingSystem AS operating_system,
  geoNetwork.country AS country,
  geoNetwork.continent AS continent,
  totals.visits AS visits,
  totals.hits AS hits,
  totals.pageviews AS pageviews,
  totals.bounces AS bounces,
  totals.timeOnSite AS time_on_site,
  totals.transactions AS transactions,
  ROUND(IFNULL(totals.totalTransactionRevenue, 0) / 1000000, 2) AS revenue
FROM `bigquery-public-data.google_analytics_sample.ga_sessions_*`
WHERE _TABLE_SUFFIX BETWEEN '20160801' AND '20170801'
```

Save as `ga_sessions.csv` in the project root, then run the notebook.

## Dataset

Google Analytics Sample dataset via BigQuery Public Data. Contains session-level data from the Google Merchandise Store.
