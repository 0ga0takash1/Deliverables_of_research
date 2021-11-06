# import prog_keyword as pk
# ----------------------------------- #
# 1. PDFを入力、PDFのPathを取得
# file_path = "/media/ogawatakafumi/HDD_1TB/lab_研/2021/省庁RFP/ニュース速報.pdf"
# import document_read as doc
# doc.read(file_path)
# ----------------------------------- #
# 2. PDFからChapter配列を作成
# ----------------------------------- #
# テスト用
# from doc_examples import toukei_bunseki
# cl.result = toukei_bunseki.to_html
# ----------------------------------- #
# 3. キーワードから文章を抽出・分配
import format_document_to_array as f_doc_ar
import read_formated_array as r_f_ar
formated_array = f_doc_ar.formated_array
r_f_ar.read_process(formated_array)
# ----------------------------------- #
# 4. 分配した文章をhtmlにpush
import classify_to_array as cl
cl.leveling_to_result_array()
import to_result_html as to_html
to_html.push()
# ----------------------------------- #
# 5. html用のローカルサーバをたてる
import server