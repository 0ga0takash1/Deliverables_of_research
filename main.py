import sys

# import prog_keyword as pk

if __name__ == "__main__":
    # ----------------------------------- #
    # 1. PDFを取得、読み込み
    file_path = sys.argv[1]
    print("input file name: ", file_path)
    import document_read as doc
    doc.main(file_path)
    # ----------------------------------- #
    # 2. PDFからフォーマット配列を作成
    import format_document_to_array as f_doc_ar
    formated_array = f_doc_ar.main(doc.get_txt(file_path))
    # ----------------------------------- #
    # テスト用
    # from doc_examples import toukei_bunseki as sample
    # formated_array = sample.formated_array
    # cl.result = toukei_bunseki.to_html
    # ----------------------------------- #
    # 3. キーワードから文章を抽出・分配
    import read_formated_array as r_f_ar
    r_f_ar.main(formated_array)
    print("Classification is complete.")
    # ----------------------------------- #
    # 4. 分配した文章をhtmlにpush
    import classify_to_array as cl
    cl.leveling_to_result_array()
    import to_result_html as to_html
    to_html.push()
    print("Push to HTML is complete.")
    # ----------------------------------- #
    # 5. html用のローカルサーバをたてる
    import server