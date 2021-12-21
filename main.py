import sys, os

# import prog_keyword as pk
import document_read as doc
import format_document_to_array as f_doc_ar
import read_formated_array as r_f_ar
import classify_to_array as cl
import to_result_html as to_html

def main(file_path):
    # ----------------------------------- #
    # 1. PDFを取得、読み込み
    print("input file name: ", file_path)
    # file_path = doc.get_txt(file_path)
    # doc.main(file_path)
    # ----------------------------------- #
    # 2. PDFからフォーマット配列を作成
    formated_array = f_doc_ar.main(file_path)
    # ----------------------------------- #
    # テスト用
    # from doc_examples import toukei_bunseki as sample
    # formated_array = sample.formated_array
    # cl.result = toukei_bunseki.to_html
    result = os.path.abspath(os.curdir)+"/doc_examples/"
    result += "unnlp"
    result += os.path.basename(file_path)[6:-3]
    result += 'html'
    # ----------------------------------- #
    # 3. キーワードから文章を抽出・分配
    r_f_ar.main(formated_array)
    print("Classification is complete.")
    # ----------------------------------- #
    # 4. 分配した文章をhtmlにpush
    cl.leveling_to_result_array()
    # result = "index.html"
    to_html.push(result)
    print("create:", result)
    print("Push to HTML is complete.\n")

if __name__ == "__main__":
    main(sys.argv[1])
    # 5. html用のローカルサーバをたてる
    # import server
    # exams = os.path.abspath(os.curdir)
    # exams += "/doc_examples/"
    # for i in os.listdir(exams):
    #     if i[-4:] == ".txt":
    #         i = exams+i
    #         main(i)
    #         cl.result_clear()
    # main("doc_examples/formatニュース速報.txt")
    # main("doc_examples/format解析システム移植.txt")
    # main("doc_examples/format技術調査報告書DB.txt")
    # main("doc_examples/format集計システム.txt")
    # main("doc_examples/format電子申請.txt")
