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
    file_name = os.path.basename(file_path)[:-4]
    file_path = doc.get_txt(file_path)
    # doc.main(file_path)
    # ----------------------------------- #
    # 2. PDFからフォーマット配列を作成
    file_path = os.path.abspath(os.curdir)+"/doc_examples/format"+file_path[:-3]+"txt"
    # formated_array = f_doc_ar.main(file_path)
    # ----------------------------------- #
    # 3. キーワードから文章を抽出・分配 -> 文法解析による取捨選択
    r_f_ar.main(formated_array)
    print("Classification is complete.")
    # ----------------------------------- #
    # 4. 分配した文章をhtmlにpush
    cl.leveling_to_result_array()
    result = "index.html"
    to_html.push(file_name, result)
    print("create:", result)
    print("Push to HTML is complete.")

if __name__ == "__main__":
    main(sys.argv[1])
    # 5. html用のローカルサーバをたてる
    import server
