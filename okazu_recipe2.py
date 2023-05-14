import random
import tkinter as tk
import tkinter.messagebox as tkmsg



meat_recipe = ["肉じゃが", "ハンバーグ", "豚の生姜焼き", "牛肉のステーキ",
               "すき焼き", "回鍋肉", "鶏の唐揚げ", "牛丼", "鶏の香草焼き",
               "青椒肉絲", "焼肉", "しゃぶしゃぶ", "鶏のさっぱり煮",
               "鶏のトマト煮", "ビーフシチュー", "豚の角煮", "とんかつ",
               "棒棒鶏", "冷しゃぶ"]

fish_recipe = ["鮭の塩焼き", "鮭のムニエル", "鮭のクリーム煮", "アクアパッツァ",
               "ぶりの塩焼き", "ぶりの照り焼き", "お刺身", "お寿司", "銀鱈の塩焼き",
               "カルパッチョ", "サバの塩焼き", "イカリング", "さんまの塩焼き",
               "エビフライ", "白身魚の黒酢炒め"]

other_recipe = ["麻婆豆腐", "カレーライス", "クリームシチュー", "ポトフ", "鍋料理",
                "天ぷら", "スパゲッティ", "うどん", "そば", "オムライス", "グラタン",
                "そうめん"]


def meat_click():
    meat_random = random.choice(meat_recipe)
    rireki1.insert(tk.END, "・提案する肉料理は{}です。\n".format(meat_random))
    rireki1.see("end")  #出力範囲を超えるとスクロールバーが自動で下がる
    
def fish_click():
    fish_random = random.choice(fish_recipe)
    rireki1.insert(tk.END, "・提案する魚料理は{}です。\n".format(fish_random))
    rireki1.see("end")
    
def other_click():
    other_random = random.choice(other_recipe)
    rireki1.insert(tk.END, "・提案する料理は{}です。\n".format(other_random))
    rireki1.see("end")

def finish_click():
    ret = tkmsg.askyesno("終了", "レシピ検索プログラムを終了します")
    if ret == True:
        root.destroy()    
    
root = tk.Tk()
root.geometry("500x700")
root.title("レシピ検索プログラム")

canvas = tk.Canvas(root, width=500, height=700, bg="white")
canvas.place(x=0, y=0)

rireki1 = tk.Text(root, font=("Helvetica", 14))
rireki1.place(x=0, y=500, width=480, height=200)

button1 = tk.Button(root, text="肉料理", font=("Helvetica", 24), command=meat_click)
button1.place(x=180, y=40)

button2 = tk.Button(root, text="魚料理", font=("Helvetica", 24), command=fish_click)
button2.place(x=180, y=130)

button3 = tk.Button(root, text="その他", font=("Helvetica", 24), command=other_click)
button3.place(x=180, y=220)

button4 = tk.Button(root, text="終了", font=("HElvetica", 24), command=finish_click)
button4.place(x=180, y=310)

#縦方向のスクロールバーの作成
yscroll = tk.Scrollbar(root, orient = tk.VERTICAL, command = rireki1.yview)
yscroll.pack(side=tk.RIGHT, fill=tk.Y)
#動きをスクロールバーに反映
rireki1["yscrollcommand"] = yscroll.set


root.mainloop()
