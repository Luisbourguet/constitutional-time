"""Event counts for the eight cases and Kenya from the CCP Chronology of Constitutional Events, v6.0.
Input: ccpcce_v6.csv (download from comparativeconstitutionsproject.org; not redistributed here).
Usage: python ccp_counts.py path/to/ccpcce_v6.csv
"""
import sys, pandas as pd
d = pd.read_csv(sys.argv[1])
cases = {'Mexico':'Mexico','Italy/Sardinia':'Italy','India':'India','South Africa':'South Africa',
         'Japan':'Japan','Namibia':'Namibia','Ghana':'Ghana','Thailand':'Thailand','Kenya':'Kenya'}
for c, name in cases.items():
    x = d[d.country == c].sort_values('year')
    cur = x.systid.dropna().iloc[-1]; xs = x[x.systid == cur]
    am = xs[xs.evnttype.isin(['amendment', 'samendment'])]
    print(f"{name:13s} systems={x.systid.nunique():3d} new={(x.evnttype=='new').sum():2d} "
          f"interim={(x.evnttype=='interim').sum()} suspension={(x.evnttype=='suspension').sum()} | "
          f"current system from {int(xs.year.min())}: {len(xs)} years, amendment years {am.year.nunique()} | data to {int(x.year.max())}")
