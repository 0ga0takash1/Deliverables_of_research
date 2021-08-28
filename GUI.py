# coding: utf-8

# tkinterのインポート
import tkinter as tk

### 関数 ###
# 関数の定義
def runFunc():
    print("Hello!!")
    print("OK")

### GUI ###
# ウインドウの作成
root = tk.Tk()
# ウインドウのサイズ指定
root.geometry("1000x600")
root.title('takashi app')

label = tk.Label(text='Hello World!', font=("MSゴシック","50", "bold"))
label.pack(anchor='center', expand=1)

# Runボタン
run_button = tk.Button(root, text = "Run", command = runFunc)
run_button.pack(anchor='center', expand=1)

# ウインドウ状態の維持
root.mainloop()