# Pipeline técnico – jurimetria_aved_stf

## 1. Setup (notebook 01)
- cria config/project_config.json
- cria data/00_pdf_raw ... data/05_master
- cria outputs/ e notebooks/

## 2. Extração (notebook 02)
- tenta pdfplumber primeiro (sem OCR)
- só usa OCR se o texto vier muito curto
- salva em data/01_pdf_txt/

## 3. Limpeza (notebook 03)
- remove cabeçalho/rodapé do STF
- aplica bigramas (incluindo 'extrema direita' -> 'extrema_direita')
- salva em data/02_corpus_clean/

## 4. Filtro temático (notebook 04)
- grupo A: desinformação / redes / mobilização
- grupo B: 8 de janeiro / atos antidemocráticos / sedes dos poderes
- janela de 40 tokens + limiar adaptativo
- txt temáticos em data/03_thematic/
- copia PDFs para data/03_thematic/pdfs/

## 5. Ranking (notebook 05)
- BM25 + TF-IDF/cosseno + cobertura + diversidade (Shannon)
- z-score e WSM (pesos iguais)
- salva data/05_master/thematic_ranking.csv

## 6. Amostra estratificada (notebook 06)
- estratos alto/médio/baixo, seleção proporcional (>10% se preciso)
- salva data/05_master/thematic_sample.csv

## 7. Nuvem (notebook 07)
- usa só amostra estratificada
- remove nomes próprios e ruídos
- salva outputs/figures/wordcloud_thematic_sample.png

## 8. Heatmap (notebook 08)
- janelas de 50 tokens
- coocorrência temática + PPMI
- top ~25 termos
- salva outputs/figures/semantic_similarity_matrix.png
- salva outputs/tables/semantic_similarity_ppmi.csv
