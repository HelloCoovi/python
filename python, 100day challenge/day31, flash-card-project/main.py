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
    canvas.itemconfig(word_text, fill="black",text=french_word)
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




#
# # 라벨(텍스트) 생성하기, config로 수정 + 글자 표시하기
# label = Label(text="This is old text", font=("Arial", 24, "italic"))
# label.config(text="This is new text")
# label.pack()
#
# # 버튼이 눌렸을때 작동하는 함수 만들기
# def action():
#     print("Do something")
#
# # 버튼 생성 및 버튼이 눌렸을때 실행되는 함수 지정
# button = Button(text="Click Me", command=action)
# button.pack()
#
# # 문자 입력창 만들기
# entry = Entry(width=30)
# # 미리 텍스트를 넣어둘수있다.(END는 사용자가 원하는 요소를 찾는데 쓰임)
# # 손대지 말것
# entry.insert(END, string="Some text to begin with.")
# # get 함수는 텍스트를 받아온다.
# print(entry.get())
# entry.pack()
#
# # 큰 문자 입력창
# text = Text(height=5, width=30)
# # 커서가 이곳에서 시작할수 있게 설정해주는 함수
# text.focus()
# # 원하는 문자를 입력창에 가지고 시작
# text.insert(END, "Example of multi-line text entry.")
# # 첫번째 줄에서 글자 0으로 시작하는 텍스트를 받아온다
# print(text.get("1.0", END))
# text.pack()
#
# # Spinbox: 값을 올리고 내릴수 있는 입력창
# def spinbox_used():
#     # spinbox의 값을 받아온다
#     print(spinbox.get())
# spinbox = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
# spinbox.pack()
#
# # Scale: 슬라이더를 이용하는 입력창
# # 슬라이더의 위치 값을 출력하는 함수
# def scale_used(value):
#     print(value)
# scale = Scale(from_=0, to=100, command=scale_used)
# scale.pack()
#
# # Checkbutton
# def checkbutton_used():
#     # 상태 출력하기(on == 1, off == 0)
#     print(checked_state.get())
# # IntVar: tkinter에 있는 클래스이며 객체를 생성해 특정 객체(checkbutton, radiobutton)에 추가하면
# # 해당 객체의 값을 추적해서 가지고 있는다.
# # 이경우 on일때는 1 off일때는 0으로 추적
# checked_state = IntVar()
# checkbutton = Checkbutton(text="Is On?", variable=checked_state, command=checkbutton_used)
# checked_state.get()
# checkbutton.pack()
#
# #Radiobutton: 여러가지 옵션중 하나만을 선택해야할때
# def radio_used():
#     print(radio_state.get())
# # IntVar를 부르고 각 버튼에 값을 할당한 다음 추적
# radio_state = IntVar()
# radiobutton1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
# radiobutton2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
# radiobutton1.pack()
# radiobutton2.pack()
#
#
# # 리스트 박스
# def listbox_used(event):
#     # 리스트 박스의 값을 받아온다
#     print(listbox.get(listbox.curselection()))
#
# listbox = Listbox(height=4)
# fruits = ["Apple", "Pear", "Orange", "Banana"]
# for item in fruits:
#     listbox.insert(fruits.index(item), item)
# listbox.bind("<<ListboxSelect>>", listbox_used)
# listbox.pack()

