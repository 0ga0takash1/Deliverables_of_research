# 要求文抽出・分類ツール

## 実行環境
- Ubuntu20.04
- Python 3.7.6

## 使用しているPythonライブラリ
- sys
- os
- re
- pdfminer
- collections
- subprocess
- spacy

# 使い方
## 0. 前準備
**現状は、<br>本プログラムはPDFをtxtファイル化したものを、<br>前もって`doc_examples`ディレクトリ内に作った状態でなければ実行できないことに注意**
### 0.1.PDFファイルをtxtファイル化・表や図の部分をエスケープ

### 0.2.ファイルの省構成情報を入力

## 1. 端末上で、<br>
```
python main.py <PDF文書名>
```
と入力する

```
input file name: <PDF文書名>
Classification is complete.
create: index.html
Push to HTML is complete.
Serving HTTP on 0.0.0.0 port 8000 (http://0.0.0.0:8000/) ...
```

という出力がされる<br>
この処理には1〜2分程度が想定される

## 2. ブラウザから「http://0.0.0.0:8000/ 」にアクセスすると、<br>分類結果を見ることができる

# 処理の流れ

# ファイル説明
## 処理系
- 主要ファイル
    - main.py
        - 本ツールのmain関数
- 前処理用ファイル
    - document_read.py
        - PDFファイルをtxtファイルにおとす
    - read_doc.txt
        - docment_read.pyの実行結果を保存するtxtファイル
- 内部処理用ファイル
    - arrays.py
        - 要求品質特性の名称リストや設定したIDを格納
    - prog_keyword.py
        - キーワード群を読み込む
    - format_document_to_array.py
        - read_doc.txtを読み込み、省と節の構成に則った階層の配列を生成
    - read_formated_array.py
        - format_document_to_array.pyで生成した配列を読み込み、分類を実行し、result配列を生成
    - nlp.py
        - 形態素解析と係り受け解析を用いた具体的な処理を定義
    - classify_to_array.py
        - result配列を生成するための具体的な処理を定義
    - to_result_html.py
        - result配列からindex.htmlを作成
    - server.py
        - localhostを起動
- 結果画面用ファイル
    - index.html
        - 出力結果用htmlファイル
    - sample.html
        - index.htmlのテンプレート
    - style.scss, style.css, style.css.map
        - index.html用CSS
    - select_list.js
        - index.htmlの動作を定義

## キーワードの設定
`keyword_lists`ディレクトリの中に、要求品質特性別にキーワード用のディレクトリ・txtファイルがある

txtファイルの1行に書き込むことでキーワードを登録する

`[[キーワード1++キーワード2` <br>
とすることで、組み合わせキーワードの設定ができる

## 実験データ
`doc_examples`ディレクトリの中に、<br>
PDFをtxtファイル化したものと実験結果のhtmlファイルがある

それぞれ以下のようになっている
- PDFをtxtファイル化したもの
    - 「format**.txt」という名前のファイル
- 実験結果のhtmlファイル
    - キーワードのみで分類した結果
        - 「unnlp**.html」
    - 文法解析を交えて分類した結果
        - 「**.html」
