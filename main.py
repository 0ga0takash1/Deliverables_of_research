# import prog_keyword as pk
# 1. PDFを入力、PDFのPathを取得
# file_path = "/media/ogawatakafumi/HDD_1TB/lab_研/2021/省庁RFP/ニュース速報.pdf"
# import document_read as doc
# doc.read(file_path)
# 2. PDFからChapter配列を作成
# 3. キーワードから文章を抽出・分配
# import nlp
import classify_to_array as cl
from doc_examples import toukei_bunseki
cl.result = toukei_bunseki.to_html
# 4. 分配した文章をhtmlにpush
import to_result_html as to_html
to_html.push()
# 5. html用のローカルサーバをたてる
# import server