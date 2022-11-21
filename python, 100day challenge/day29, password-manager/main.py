from tkinter import *
from tkinter import messagebox
import random
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + [random.choice(symbols) for _ in range(nr_symbols)] + [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \n Email: {email}"
                                                           f"\nPassword: {password} \nIs it ok to save?")

        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{site} | {email} | {password}\n")

            site_entry.delete(0, END)
            password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200, highlightthickness=0)
main_image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=main_image)
canvas.grid(column=1, row=0)

site_label = Label(text="Website:")
site_label.grid(column=0, row=1)
email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)
password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

site_entry = Entry(width=35)
site_entry.grid(column=1, row=1, columnspan=2)
site_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "myemail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
input_button = Button(text="Add", width=36, command=save_info)
input_button.grid(column=1, row=4, columnspan=2)


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
window.mainloop()