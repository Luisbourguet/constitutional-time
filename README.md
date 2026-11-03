# Constitutional Time: Who Binds Whom in the Data on Constitutions

[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.23903482.svg)](https://doi.org/10.5281/zenodo.23903482)

**Preprint, version 1.1 (3 November 2026)** · Luis Bourguet · not yet peer reviewed · prepared for
double-anonymous peer review at a journal (venue withheld) · CC BY 4.0

- PDF: [`Bourguet_2026_Constitutional_Time_preprint_v1-1.pdf`](Bourguet_2026_Constitutional_Time_preprint_v1-1.pdf)
- DOCX: [`Bourguet_2026_Constitutional_Time_preprint_v1-1.docx`](Bourguet_2026_Constitutional_Time_preprint_v1-1.docx)
- Source: [`preprint.md`](preprint.md) (Pandoc; build files in `build/`)

The repository also holds the data, code and figures the article uses, so that every count and the
pilot classification can be reproduced or re-coded.

## What is here

| Path | Content |
|---|---|
| `data/crisisdb_constitution_present.csv` | The 44 Seshat CrisisDB crises coded `constitution` = present or inferred present, with the databank's case descriptions (Polaris-2026 release; CC BY-NC-SA). |
| `data/crisisdb_constitution_pilot_classification.csv` | The same 44 cases with the pilot classification on two axes, `break_type` and `access_direction`, and a `reading_note` per case. **One reading, AI-assisted and confirmed by the author (3 Nov 2026); not independently validated.** Reported in the article's §8 as a pilot only. |
| `code/ccp_counts.py` | Recomputes the event counts quoted in §5 from the CCP Chronology v6.0 (`ccpcce_v6.csv`, download from the Comparative Constitutions Project; not redistributed). |
| `code/figure1_timeline.py` | Builds Figure 1 from the same file. |
| `code/pilot_crosstab.py` | Builds Table 3 from the pilot classification. |
| `figures/` | Figures 1 and 2 as PNG (300 dpi) and PDF. |
| `manuscript/` | The anonymised text prepared for review (Markdown). |
| `build/` | Header and DOCX finisher used to build the preprint (XeLaTeX via Pandoc). |

## Status

Nothing in the article is claimed as executed except the pilot in `data/…pilot_classification.csv`,
which was made by one coder from the databank's secondary descriptions (a provisional classification
drafted with the assistance of a large language model and reviewed case by case and confirmed by the author on 3 November 2026) and is published so that it can be
independently re-coded. The coding schema (four items) has not been applied to any order.

## Sources

- Elkins, Ginsburg and Melton, *Comparative Constitutions Project*: Chronology of Constitutional Events v6.0; Characteristics of National Constitutions v5.0. comparativeconstitutionsproject.org
- Seshat: Global History Databank, Polaris-2026 release; CrisisDB. seshat-db.com — Benam et al. 2022, doi:10.5281/zenodo.6642229 (CC BY-NC-SA).

## Licence

Text, code and figures: CC BY 4.0. The Seshat-derived data files keep the databank's CC BY-NC-SA licence.

## How to cite

Bourguet, L. 2026, *Constitutional Time: Who Binds Whom in the Data on Constitutions* (preprint, version 1), Zenodo, doi:[10.5281/zenodo.23903482](https://doi.org/10.5281/zenodo.23903482).

## Versions

| Version | Date | DOI | Change |
|---|---|---|---|
| v1.0-preprint | 2026-11-03 | [10.5281/zenodo.23903483](https://doi.org/10.5281/zenodo.23903483) | First deposit |
| v1.0.1-preprint | 2026-11-03 | [10.5281/zenodo.23903503](https://doi.org/10.5281/zenodo.23903503) | Concept DOI written into PDF, DOCX, README and CITATION; text unchanged |
| v1.1-preprint | 2026-11-03 | [10.5281/zenodo.23903794](https://doi.org/10.5281/zenodo.23903794) | Pilot reviewed and confirmed by the author (all 44 codes unchanged); provenance stated in §1 and §8; DOI in the data statement |

The concept DOI [10.5281/zenodo.23903482](https://doi.org/10.5281/zenodo.23903482) always resolves to the latest version.
