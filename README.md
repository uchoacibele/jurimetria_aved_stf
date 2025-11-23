# jurimetria_aved_stf

[![License: CC BY-NC-NA 4.0](https://img.shields.io/badge/License-CC_BY--NC--SA_4.0-6f42c1.svg)](https://creativecommons.org/licenses/by-nc-sa/4.0/)

Análise empírica de decisões do Supremo Tribunal Federal (STF) sobre **desinformação** e os **atos de 8 de janeiro de 2023**, com foco em **transparência metodológica**, **reprodutibilidade** e **rigor quantitativo** aplicado à linguagem natural jurídica.

> Documentação detalhada do pipeline: veja `docs/pipeline_jurimetria_aved.md`.

---

## Estrutura do projeto

```text
jurimetria_aved_stf/
├── config/
│   └── project_config.json
├── data/
│   ├── 00_pdf_raw/            # PDFs originais
│   ├── 01_pdf_txt/            # Texto extraído (pdfplumber)
│   ├── 02_corpus_clean/       # Texto limpo/normalizado (Unicode preservado)
│   ├── 03_thematic/           # Subcorpus temático
│   ├── 04_ranked/             # Intermediários de ranking
│   └── 05_master/             # Consolidados (CSVs/Parquet)
├── docs/
│   └── pipeline_jurimetria_aved.md
├── logs/
├── notebooks/                 # 01–08
├── outputs/
│   ├── figures/               # Gráficos (PNG/JPEG)
│   ├── tables/                # Tabelas (CSV)
│   └── reports/
├── scripts/
└── README.md
