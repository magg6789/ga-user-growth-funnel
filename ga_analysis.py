"""
User Growth & Funnel Optimization Analysis
Dataset: Google Analytics Sample (BigQuery Public Data)
Author: Miriam Garcia | miriamgarcia.org
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
from scipy.stats import chi2_contingency
import warnings
warnings.filterwarnings('ignore')

BLUE="#1A73E8"; TEAL="#00897B"; GREEN="#34A853"
YELLOW="#FBBC04"; RED="#EA4335"; GRAY="#5F6368"
NAVY="#174EA6"; LGRAY="#F1F3F4"; WHITE="#FFFFFF"

plt.rcParams.update({'figure.facecolor':WHITE,'axes.facecolor':WHITE,
    'axes.spines.top':False,'axes.spines.right':False})

def load_data(path="ga_sessions.csv"):
    df = pd.read_csv(path, low_memory=False)
    df['date'] = pd.to_datetime(df['date'], format='%Y%m%d')
    df['month'] = df['date'].dt.to_period('M')
    for col in ['bounces','transactions']:
        df[col] = df[col].fillna(0).astype(int)
    for col in ['revenue','time_on_site','pageviews']:
        df[col] = df[col].fillna(0)
    df['converted'] = df['transactions'] > 0
    df['bounced']   = df['bounces'] > 0
    return df

def print_kpis(df):
    print(f"Sessions:        {len(df):,}")
    print(f"Unique visitors: {df['fullVisitorId'].nunique():,}")
    print(f"Transactions:    {int(df['transactions'].sum()):,}")
    print(f"Revenue:         ${df['revenue'].sum():,.2f}")
    print(f"CVR:             {df['converted'].mean():.2%}")
    print(f"Bounce rate:     {df['bounced'].mean():.2%}")

if __name__ == "__main__":
    import os
    os.makedirs("images", exist_ok=True)
    df = load_data()
    print_kpis(df)
    print("Run the Jupyter notebook for full analysis and visualizations.")
