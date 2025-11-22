# Pipeline (resumo)

- **Notebook 01**: criação do ambiente e `project_config.json` (paths, versões).
- **Notebook 02**: extração de texto de PDFs pesquisáveis com `pdfplumber`.
- **Notebook 03**: limpeza com preservação de acentos para visualização; remoção de paratextos/stopwords/nomes próprios; bigramas relevantes.
- **Notebook 04**: filtro temático determinístico (léxico A: desinformação; léxico B: 8/1 e instituições) com janelas simétricas.
- **Notebook 05**: ranking por MCDA/WSM (BM25; TF-IDF+cos; cobertura; diversidade).
- **Notebook 06**: amostragem estratificada (top/middle/bottom) ~10%.
- **Notebook 07**: nuvem de palavras (máx 200–400), janelas ±200 caracteres, keyness e filtros.
- **Notebook 08**: heatmap condicionado à temática (PPMI normalizada, janelas 25, passo 10; TOP_TERMS=50; clustering hierárquico p/ ordenação).
