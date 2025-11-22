from pathlib import Path

def main():
    root = Path.home() / "Documents" / "jurimetria_aved_stf"
    docs_dir = root / "docs"
    docs_dir.mkdir(parents=True, exist_ok=True)

    # 1) README.md
    readme_text = (
        "# jurimetria_aved_stf\n\n"
        "Pipeline de análise temática e jurimétrica de acórdãos do STF "
        "relacionados a desinformação e aos atos antidemocráticos de 8/1/2023.\n\n"
        "## Ordem de execução\n"
        "1. notebooks/01_setup.ipynb\n"
        "2. notebooks/02_extraction.ipynb\n"
        "3. notebooks/03_cleaning.ipynb\n"
        "4. notebooks/04_thematic_filter.ipynb\n"
        "5. notebooks/05_thematic_ranking.ipynb\n"
        "6. notebooks/06_stratified_sample.ipynb\n"
        "7. notebooks/07_wordcloud.ipynb\n"
        "8. notebooks/08_cooccurrence_heatmap.ipynb\n\n"
        "## Pastas principais\n"
        "- data/00_pdf_raw/\n"
        "- data/01_pdf_txt/\n"
        "- data/02_corpus_clean/\n"
        "- data/03_thematic/ (+ /pdfs)\n"
        "- data/04_ranked/\n"
        "- data/05_master/\n"
        "- outputs/figures/\n"
        "- outputs/tables/\n"
    )
    (root / "README.md").write_text(readme_text, encoding="utf-8")

    # 2) docs/pipeline_jurimetria_aved_stf.md
    pipeline_text = (
        "# Pipeline técnico – jurimetria_aved_stf\n\n"
        "## 1. Setup (notebook 01)\n"
        "- cria config/project_config.json\n"
        "- cria data/00_pdf_raw ... data/05_master\n"
        "- cria outputs/ e notebooks/\n\n"
        "## 2. Extração (notebook 02)\n"
        "- tenta pdfplumber primeiro (sem OCR)\n"
        "- só usa OCR se o texto vier muito curto\n"
        "- salva em data/01_pdf_txt/\n\n"
        "## 3. Limpeza (notebook 03)\n"
        "- remove cabeçalho/rodapé do STF\n"
        "- aplica bigramas (incluindo 'extrema direita' -> 'extrema_direita')\n"
        "- salva em data/02_corpus_clean/\n\n"
        "## 4. Filtro temático (notebook 04)\n"
        "- grupo A: desinformação / redes / mobilização\n"
        "- grupo B: 8 de janeiro / atos antidemocráticos / sedes dos poderes\n"
        "- janela de 40 tokens + limiar adaptativo\n"
        "- txt temáticos em data/03_thematic/\n"
        "- copia PDFs para data/03_thematic/pdfs/\n\n"
        "## 5. Ranking (notebook 05)\n"
        "- BM25 + TF-IDF/cosseno + cobertura + diversidade (Shannon)\n"
        "- z-score e WSM (pesos iguais)\n"
        "- salva data/05_master/thematic_ranking.csv\n\n"
        "## 6. Amostra estratificada (notebook 06)\n"
        "- estratos alto/médio/baixo, seleção proporcional (>10% se preciso)\n"
        "- salva data/05_master/thematic_sample.csv\n\n"
        "## 7. Nuvem (notebook 07)\n"
        "- usa só amostra estratificada\n"
        "- remove nomes próprios e ruídos\n"
        "- salva outputs/figures/wordcloud_thematic_sample.png\n\n"
        "## 8. Heatmap (notebook 08)\n"
        "- janelas de 50 tokens\n"
        "- coocorrência temática + PPMI\n"
        "- top ~25 termos\n"
        "- salva outputs/figures/semantic_similarity_matrix.png\n"
        "- salva outputs/tables/semantic_similarity_ppmi.csv\n"
    )
    (docs_dir / "pipeline_jurimetria_aved_stf.md").write_text(pipeline_text, encoding="utf-8")

    print("README.md gerado")
    print("docs/pipeline_jurimetria_aved_stf.md gerado")

if __name__ == "__main__":
    main()
