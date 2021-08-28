from io import StringIO
from numpy import extract
import classify

from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfdocument import PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.pdfparser import PDFParser
from pdfminer.high_level import extract_text
from pdfminer.high_level import extract_text_to_fp

class Chapter:
    def __init__(self, title, text):
        self.title = title
        self.text = text

pdf_file_path = "/media/ogawatakafumi/HDD_1TB/lab_研/2021/省庁RFP/ニュース速報.pdf"

with open(pdf_file_path, 'rb') as fp:
    # 出力先をPythonコンソールにするためのメソッドを取得
    output_text = StringIO()

    # 各種テキスト抽出に必要なPdfminer.sixのオブジェクトを取得する処理
    rmgr = PDFResourceManager() 
    lprms = LAParams()
    device = TextConverter(rmgr, output_text, laparams=lprms)
    iprtr = PDFPageInterpreter(rmgr, device)

    # PDFファイルから1ページずつ解析(テキスト抽出)処理する
    for page in PDFPage.get_pages(fp):
        # page = page.rstrip('\n')
        iprtr.process_page(page)
    

    # Pythonコンソールへの出力内容を取得
    text = output_text.getvalue().strip()
    # text = extract_text(pdf_file_path)

    # extract_text_to_fp(fp, output_text)
    # text = output_text.getvalue().strip()

    # 閉じる
    output_text.close()
    device.close()

    # print(text)
    # textの中の改行コードを削除
    # i = 0
    # str = ''
    # for o in text:
    #     # print(o)
    #     print(i)
    #     if o != '\n':
    #         str += o
    #     else:
    #         # if str != "\n": 
    #         print(str)
    #         str = ''
    #     i += 1
    #     if i == 100: break

# pdf = []

# pdf.append(Chapter(classify.Chapters[0], ))
import pandas as pd
import tabula

# lattice=Trueでテーブルの軸線でセルを判定
dfs = tabula.read_pdf(pdf_file_path, lattice=True, pages = 'all')

# PDFの表をちゃんと取得できているか確認
for df in dfs:
    print(df)