# Constitutional time: who binds whom in the data on constitutions

Companion repository for a manuscript under review (venue withheld). It holds the data, code and
figures the article uses, so that every count and the pilot classification can be reproduced or
re-coded.

## What is here

| Path | Content |
|---|---|
| `data/crisisdb_constitution_present.csv` | The 44 Seshat CrisisDB crises coded `constitution` = present or inferred present, with the databank's case descriptions (Polaris-2026 release; CC BY-NC-SA). |
| `data/crisisdb_constitution_pilot_classification.csv` | The same 44 cases with the pilot classification on two axes, `break_type` and `access_direction`, and a `reading_note` per case. **Single coder, not validated.** Reported in the article's §8 as a pilot only. |
| `code/ccp_counts.py` | Recomputes the event counts quoted in §5 from the CCP Chronology v6.0 (`ccpcce_v6.csv`, download from the Comparative Constitutions Project; not redistributed). |
| `code/figure1_timeline.py` | Builds Figure 1 from the same file. |
| `code/pilot_crosstab.py` | Builds Table 3 from the pilot classification. |
| `figures/` | Figures 1 and 2 as PNG (300 dpi) and PDF. |
| `manuscript/` | The anonymised text as submitted (Markdown). |

## Status

Nothing in the article is claimed as executed except the pilot in `data/…pilot_classification.csv`,
which was made by one coder from the databank's secondary descriptions and is published so that it
can be independently re-coded. The coding schema (four items) has not been applied to any order.

## Sources

- Elkins, Ginsburg and Melton, *Comparative Constitutions Project*: Chronology of Constitutional Events v6.0; Characteristics of National Constitutions v5.0. comparativeconstitutionsproject.org
- Seshat: Global History Databank, Polaris-2026 release; CrisisDB. seshat-db.com — Benam et al. 2022, doi:10.5281/zenodo.6642229 (CC BY-NC-SA).

## Licence

Text, code and figures: CC BY 4.0. The Seshat-derived data files keep the databank's CC BY-NC-SA licence.
