########################################################################
# PDFをtxtファイルにするコード

# main関数を実行することで、
# doc_examplesフォルダ内に「format<文書名>.txt」を作ってくれる
########################################################################

from pdfminer.high_level import extract_pages
from pdfminer.layout import LAParams, LTTextBox
import collections
import os, sys, argparse

class ConvertPDF2text():
    def __init__(self, argv:list):
        self.input_path = r'70_197.pdf'
        self.output_path = "read_doc.txt"
        self.border = 0
        self.footer = 60
        self.header = 1000
        self.start_page = 1
        self.last_page = 0

        if not argv: return

        parser = argparse.ArgumentParser()
        parser.add_argument('input_path', type=str, help="入力ファイル名")
        parser.add_argument('output_path', nargs="?", default=self.output_path, type=str, help="出力ファイル名(default:月日_時分_秒.txt)")
        parser.add_argument("-b", '--border', type=int, metavar="n", default=1, help="段組みの切れ目  0の場合、用紙幅の半分(default:%(default)s)")
        parser.add_argument("-f", '--footer', type=int, metavar="n", default=30, help="フッター位置(default:%(default)s)")
        parser.add_argument("-t", '--top', type=int, metavar="n", default=1000, help="ヘッダー位置(default:%(default)s)")
        parser.add_argument("-s",'--s_page', type=int, metavar="n", default=1, help="開始ページ(default:%(default)s)")
        parser.add_argument("-e",'--e_page', type=int, metavar="n", default=0, help="終了ページ(0:最終)(default:%(default)s)")
                
        args = parser.parse_args(argv)
        print(args)
        self.input_path = args.input_path
        self.start_page = args.s_page
        self.last_page = args.e_page
        self.output_path = args.output_path
        self.border = args.border
        self.footer = args.footer
        self.header = args.top
        self.sheet_name = os.path.splitext(os.path.basename(self.output_path))[0]

    def flatten(self, l):
        for el in l:
            if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
                yield from self.flatten(el)
            else:
                yield el

    def flatten_lttext(self, l, _type):
        for el in l:
            if isinstance(el, (_type)):
                yield el
            else:
                if isinstance(el, collections.abc.Iterable) and not isinstance(el, (str, bytes)):
                    yield from self.flatten_lttext(el, _type)
                else:
                    continue

    def write2text(self, f):
        f.write(self.text_l)
        f.write(self.text_r)
        self.text_l = self.text_r = ""

    def convert_pdf_to_text(self):
        laparams = LAParams()
        laparams.boxes_flow = None
        laparams.word_margin = 0.2
        laparams.char_margin = 2.0
        laparams.line_margin = 0

        with open(self.output_path, "w", encoding="utf-8") as f:
            self.text_l = ""
            self.text_r = ""
            
            print("Analyzing from {} page to {} page(0:to last)".format(self.start_page, self.last_page))
            
            for page_layout in extract_pages(self.input_path, maxpages=0, laparams=laparams):    # ファイルにwithしている
                if page_layout.pageid < self.start_page: continue                   # 指定開始ページより前は飛ばす
                if self.last_page and self.last_page < page_layout.pageid: break    # 指定終了ページ以降は中断
                if self.border == 0:
                    self.border = int(page_layout.width / 2)
                if page_layout.pageid == self.start_page:
                    print("Check on page #{}".format(page_layout.pageid))
                    print("Page Info width:{}, heght:{}".format(page_layout.width, page_layout.height))
                    print("Calc result border: {}, footer: {}".format(self.border, self.footer))

                for element in sorted(self.flatten_lttext(page_layout, LTTextBox), key=lambda x: (-x.y1, x.x0)):
                    if element.y1 < self.footer: continue  # フッター位置の文字は抽出しない
                    if element.y0 > self.header: continue  # ヘッダー位置の文字は抽出しない
                    _text =element.get_text()

                    if element.x1 < self.border:
                        self.text_l += _text
                    else:
                        if element.x0 >= self.border:
                            self.text_r += _text
                        else:
                            if self.text_r:
                                self.write2text(f)
                            self.text_l += _text
                self.write2text(f)

def make_clear_txt(out_txt):
    print("create:", out_txt)
    with open("read_doc.txt") as fp:
        out = fp.read()
        out = out.replace(' ', '')
        out = out.replace('　', '')
        while out.count('\n\n') != 0:
            out = out.replace('\n\n', '\n')
        with open(out_txt, "w") as f:
            f.write(out)

def get_txt(input_file):
    res = os.path.join(os.path.abspath(os.curdir), "doc_examples")
    name = os.path.basename(input_file)[:-4]
    res = os.path.join(res, "format{}.txt".format(name))
    return res

def main(input_path):
    cnv = ConvertPDF2text([input_path])
    cnv.convert_pdf_to_text()
    make_clear_txt(get_txt(input_path))

if __name__ == '__main__':
    main(sys.argv[1:][0])