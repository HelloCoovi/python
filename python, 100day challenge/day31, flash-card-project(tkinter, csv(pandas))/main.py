from tkinter import *
import pandas
import random

import pandas as pd

# 체크 버튼을 누르면 해당 단어가 리스트에서 삭제된다. OK
# 데이터가 삭제된 리스트로 새로운 CSV파일을 만든다. OK
# 다음에 실행시 words_to_learn.csv 파일이 있는지 확인하고 OK
    # 있다면 words_to_learn을 불러와서 사용하고 OK
    # 아니라면 french_words를 부른다. OK


# ------------------- DATA -------------------
try:
    dataframe = pandas.read_csv("data/words_to_learn.csv")
    dict_data = dataframe.to_dict(orient='records')
except FileNotFoundError:
    print("파일 못찾음 새로운 유저로 시작함")
    dataframe = pandas.read_csv("data/french_words.csv")
    dict_data = dataframe.to_dict(orient='records')

# ------------------- FUNCTION -------------------
random_word = {}

def next_card():
    global random_word, filp_timer

    window.after_cancel(filp_timer)
    random_word = random.choice(dict_data)
    french_word = random_word['French']
    canvas.itemconfig(titel_text, fill="black", text="French")
    canvas.itemconfig(word_text, fill="black", text=french_word)
    canvas.itemconfig(card_image, image=card_front_img)

    filp_timer = window.after(3000, flip_card)

def flip_card():
    english_word = random_word['English']
    canvas.itemconfig(titel_text, fill="white", text="English")
    canvas.itemconfig(word_text, fill="white", text=english_word)
    canvas.itemconfig(card_image, image=card_back_img)

def learn():
    print(len(dict_data))
    dict_data.remove(random_word)
    save_data = pd.DataFrame(dict_data)
    save_data.to_csv("data/words_to_learn.csv", index=False)
    next_card()


# ------------------- UI SETUP -------------------
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

filp_timer = window.after(3000, flip_card)

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400, 263, image=card_front_img)
titel_text = canvas.create_text(400, 150, text="Titel", font=("Ariel", 40, "italic"))
word_text = canvas.create_text(400, 263, text="trouve", font=("Ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, command=learn, highlightthickness=0)
right_button.grid(column=1, row=1)
wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, command=next_card, highlightthickness=0)
wrong_button.grid(column=0, row=1)


next_card()

# ------------------- LOOP -------------------
window.mainloop()

