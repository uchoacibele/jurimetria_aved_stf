# jurimetria_aved_stf

Projeto de análise empírica de decisões do Supremo Tribunal Federal (STF) sobre desinformação, atos antidemocráticos e 8 de janeiro de 2023, com ênfase em transparência metodológica, reprodutibilidade e rigor quantitativo aplicado à linguagem natural jurídica.

## 1. Ambiente e dependências

- **Linguagem:** Python 3.11 (recomendado)
- **Ambiente virtual:** `conda` ou `venv`, com isolamento dedicado ao projeto.
- **Principais bibliotecas:**
  - `pdfplumber` — extração de texto de PDFs nativamente pesquisáveis.
  - `pytesseract` e `pdf2image` — suporte opcional a OCR (mantido na configuração, ainda que não essencial aos acórdãos digitalmente pesquisáveis).
  - `pandas`, `numpy` — manipulação de dados.
  - `matplotlib` — visualizações.
  - `tqdm` — barras de progresso.
  - `scikit-learn` — TF-IDF e similaridade do cosseno.
  - `wordcloud` — nuvem de palavras temática.
  - `unidecode` — suporte auxiliar de normalização quando aplicável.

A criação do ambiente e o registro das versões utilizadas são realizados no **Notebook 01**, garantindo rastreabilidade.

## 2. Estrutura de diretórios

A estrutura base do projeto é:

```text
jurimetria_aved_stf/
├── config/
│   └── project_config.json
├── data/
│   ├── 00_pdf_raw/
│   ├── 01_pdf_txt/
│   ├── 02_corpus_clean/
│   ├── 03_thematic/
│   ├── 04_ranked/
│   └── 05_master/
├── docs/
│   └── pipeline_jurimetria_aved.md
├── logs/
├── notebooks/
├── outputs/
│   ├── figures/
│   ├── tables/
│   └── reports/
├── scripts/
└── README.md
