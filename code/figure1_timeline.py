"""Figure 1: constitutional events 1900-2025 for the eight cases and Kenya (CCP Chronology v6.0).
Usage: python figure1_timeline.py path/to/ccpcce_v6.csv out.png
Colours: validated categorical palette (blue, aqua, orange, yellow); event type by symbol.
"""
import sys, pandas as pd, matplotlib
matplotlib.use('Agg'); import matplotlib.pyplot as plt
from matplotlib.patches import Patch; from matplotlib.lines import Line2D
plt.rcParams['font.family'] = 'DejaVu Serif'
d = pd.read_csv(sys.argv[1]); out = sys.argv[2]
COL = {'Accumulative':'#2a78d6','Frozen':'#1baf7a','Cyclical':'#eb6834','Note':'#eda100'}
rows = [('Accumulative',[('Mexico','Mexico'),('Italy/Sardinia','Italy'),('India','India'),('South Africa','South Africa')]),
        ('Frozen',[('Japan','Japan'),('Namibia','Namibia')]),('Cyclical',[('Ghana','Ghana'),('Thailand','Thailand')]),('Note',[('Kenya','Kenya')])]
X0, X1 = 1900, 2025
fig, ax = plt.subplots(figsize=(7.2, 5.0), dpi=300)
y = 0; ylabels = []; ypos = []; groups = []
for g, cs in rows:
    gstart = y
    for c, lab in cs:
        x = d[(d.country == c) & (d.year >= X0)].sort_values('year'); last = int(x.year.max())
        for sid, xs in x.dropna(subset=['systid']).groupby('systid'):
            a, b = int(xs.year.min()), int(xs.year.max()); b = X1 if b == last else b
            ax.barh(y, b-a+0.9, left=a-0.45, height=0.44, color=COL[g], alpha=0.55, edgecolor='white', linewidth=0.6)
        for _, r in x[x.evnttype.isin(['interim','suspension'])].iterrows():
            ax.barh(y, 1.0, left=r.year-0.5, height=0.44, color='white', edgecolor='#444444', hatch='////', linewidth=0.3)
        am = x[x.evnttype.isin(['amendment','samendment'])].year
        ax.vlines(am, y-0.34, y+0.34, color='#1a1a1a', linewidth=0.7)
        nw = x[x.evnttype == 'new'].year
        ax.plot(nw, [y]*len(nw), marker='v', markersize=5, linestyle='', color='#1a1a1a', markeredgecolor='white', markeredgewidth=0.5, zorder=5)
        ax.text(X1+1.5, y, f"to {last}", va='center', fontsize=6, color='#555555')
        ylabels.append(lab); ypos.append(y); y += 1
    groups.append((g, gstart, y-1)); y += 0.7
ax.set_yticks(ypos); ax.set_yticklabels(ylabels, fontsize=8); ax.invert_yaxis()
ax.set_xlim(X0-1, X1+10); ax.set_xticks(range(1900, 2026, 25)); ax.tick_params(axis='x', labelsize=7)
for sp in ['top','right','left']: ax.spines[sp].set_visible(False)
ax.spines['bottom'].set_color('#888888'); ax.tick_params(axis='y', length=0, pad=4)
ax.grid(axis='x', color='#e6e6e6', linewidth=0.5); ax.set_axisbelow(True)
for g, a, b in groups:
    ax.text(-0.19, (a+b)/2, 'Kenya (note)' if g == 'Note' else g, rotation=90, va='center', ha='center', fontsize=7, color=COL[g], weight='bold', transform=ax.get_yaxis_transform())
leg = [Patch(facecolor=COL['Accumulative'], alpha=0.55, label='accumulative pattern'), Patch(facecolor=COL['Frozen'], alpha=0.55, label='frozen pattern'),
       Patch(facecolor=COL['Cyclical'], alpha=0.55, label='cyclical pattern'), Patch(facecolor=COL['Note'], alpha=0.55, label='Kenya (note)'),
       Line2D([0],[0], marker='v', color='#1a1a1a', linestyle='', markersize=5, label='new constitution'),
       Line2D([0],[0], color='#1a1a1a', linewidth=0.8, label='year with at least one formal amendment'),
       Patch(facecolor='white', edgecolor='#444444', hatch='////', label='interim constitution or suspension')]
ax.legend(handles=leg, loc='lower center', bbox_to_anchor=(0.45, -0.33), ncol=2, fontsize=6.5, frameon=False, title='Bar colour: pattern · Marks: event type', title_fontsize=6.5)
plt.subplots_adjust(left=0.2, right=0.97, top=0.97, bottom=0.26); plt.savefig(out, dpi=300)
