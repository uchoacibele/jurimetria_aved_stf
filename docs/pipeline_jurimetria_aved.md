# Pipeline metodológico – jurimetria_aved_stf

Este documento descreve, em linguagem técnica e reprodutível, as etapas do pipeline de análise aplicada aos acórdãos do STF sobre desinformação, atos antidemocráticos e 8 de janeiro de 2023.

## 1. Organização do ambiente

A análise foi desenvolvida em Python 3.11, em ambiente virtual dedicado, com registro das versões das principais dependências (`pdfplumber`, `pandas`, `numpy`, `matplotlib`, `tqdm`, `scikit-learn`, `wordcloud`, `unidecode`, entre outras) em arquivo de log. A configuração central é armazenada em `config/project_config.json`, que define a estrutura de diretórios, parâmetros de extração e caminhos padronizados para dados, saídas e relatórios, garantindo transparência e reprodutibilidade.

## 2. Extração de texto (Notebook 02)

Os acórdãos em formato PDF são armazenados em `data/00_pdf_raw/`. A extração é realizada prioritariamente com `pdfplumber`, por se tratar de documentos digitalmente pesquisáveis, gerando arquivos `.txt` em `data/01_pdf_txt/`. Para cada arquivo são registrados, em `logs/extraction_log.csv`, o método utilizado, número de páginas, extensão do texto e eventuais exceções. A arquitetura mantém suporte a OCR (`pdf2image` + `pytesseract`) para cenários futuros, sem comprometer a integridade dos acórdãos nativamente textuais.

## 3. Limpeza e normalização do corpus (Notebook 03)

O texto bruto passa por um processo de filtragem orientado a reduzir ruído sem eliminar informação substantiva. São removidos elementos de cabeçalho e rodapé, URLs, metadados de autenticação, marcadores de página, termos de autenticação eletrônica, stopwords da língua portuguesa, abreviações processuais recorrentes e nomes próprios de partes e autoridades, mitigando interferências nominais. Expressões com significado consolidado no contexto analisado — como *fake news*, *atos antidemocráticos*, *redes sociais*, *Palácio do Planalto*, *Praça dos Três Poderes* — são tratadas como unidades lexicais compostas. A tokenização preserva acentuação na visualização, utilizando normalizações pontuais apenas para corrigir deformações evidentes. O resultado é salvo em `data/02_corpus_clean/`, com rastreio em `logs/cleaning_log.csv`.

## 4. Filtro temático supervisionado (Notebook 04)

A aderência temática é estimada a partir de um léxico supervisionado voltado à interseção entre desinformação, mobilização em redes e os atos de 8 de janeiro. O modelo considera (i) um grupo de termos relacionados a desinformação, conteúdos enganosos e infraestruturas de circulação (por exemplo, *fake news*, conteúdos falsos, desinformação, redes sociais, grupos de mensagens, financiamento, convocação) e (ii) um grupo de termos vinculados a 8/1 e às instituições e locais atingidos (por exemplo, 8 de janeiro, atos antidemocráticos, invasão, depredação, Praça dos Três Poderes, Palácio do Planalto, Congresso Nacional, STF). A presença e a coocorrência desses grupos em janelas simétricas de contexto, combinadas à intensidade de menções e à concisão decisória, gera um escore determinístico e reprodutível de aderência. Documentos classificados como temáticos são copiados para `data/03_thematic/`, e a distribuição entre decisões temáticas e não temáticas é visualizada em `outputs/figures/thematic_adherence.png`.

## 5. Ranking temático por MCDA (Notebook 05)

Sobre o subcorpus temático aplicam-se quatro métricas independentes: (i) relevância lexical com BM25; (ii) direcionamento semântico por TF-IDF e similaridade do cosseno em relação a um protótipo do tema; (iii) cobertura temática, definida como a fração de sentenças em que o léxico do tema aparece; e (iv) diversidade temática entre subgrupos léxicos, calculada com entropia de Shannon normalizada (0–1). Cada métrica é padronizada por z-score, e o escore composto é calculado via Weighted Sum Model (WSM), com pesos iguais (0,25) na ausência de justificativa robusta para ponderações diferenciadas, em linha com a literatura de Multi-Criteria Decision Analysis (MCDA). Os resultados são armazenados em `data/05_master/thematic_ranking.csv` e visualizados em `outputs/figures/thematic_ranking.png`.

## 6. Amostragem estratificada (Notebook 06)

O escore composto é utilizado para segmentar os documentos temáticos em estratos de alta, média e baixa pertinência temática. A partir desses estratos, é selecionada uma amostra estratificada aproximada de 10% dos documentos, assegurando representação de casos centrais, intermediários e limítrofes. A seleção é aleatória dentro de cada estrato, com equilíbrio entre faixas, e registrada em `outputs/tables/stratified_sample.csv` e `outputs/figures/stratified_ranking.png`, constituindo base robusta para análises qualitativas subsequentes.

## 7. Nuvem de palavras temática (Notebook 07)

A nuvem de palavras é construída a partir da amostra estratificada de documentos temáticos, com aplicação de filtros rigorosos: exclusão de stopwords, nomes próprios, siglas processuais irrelevantes, deformações ortográficas e ruídos de cabeçalho/rodapé; preservação de acentuação para fins de leitura; tratamento de expressões multi-palavra relevantes como unidades lexicais; e limitação do número máximo de termos para garantir legibilidade. A nuvem sintetiza campos léxicos recorrentes associados à desinformação, mobilização para os atos e enquadramentos institucionais presentes nas decisões.

## 8. Heatmap de coocorrência temática (Notebook 08)

A matriz de similaridade semântica é construída com base na coocorrência de termos no subcorpus temático. Utilizam-se janelas deslizantes de 50 tokens, registrando-se, para cada termo, frequências individuais e coocorrências em pares. A força de associação é medida por Informação Mútua Pontual Positiva (PPMI), comparando a coocorrência observada com o valor esperado sob independência. São considerados apenas pares com suporte mínimo e PPMI positiva, compondo uma matriz normalizada em escala 0–1 e visualizada em heatmap com paleta viridis, garantindo legibilidade, continuidade perceptual e compatibilidade com padrões de acessibilidade. A matriz numérica é registrada em `outputs/tables/ppmi_matrix.csv`, permitindo auditoria e replicação dos padrões observados.
