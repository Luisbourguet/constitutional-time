"""Table 3: pilot classification cross-tab (single coder; not validated).
Usage: python pilot_crosstab.py ../data/crisisdb_constitution_pilot_classification.csv
"""
import sys, pandas as pd
d = pd.read_csv(sys.argv[1])
order = ['re-inscription from within','replacement','fragmentation','secession / independence','external imposition']
t = pd.crosstab(d.break_type, d.access_direction, margins=True).reindex(order + ['All'])
print(t[['widened','narrowed','unclear','All']])
print('post-1789 cases:', int((d.year_from >= 1789).sum()))
