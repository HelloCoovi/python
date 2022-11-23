from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

# Search 버튼 생성 @clear
# 함수 find_password 생성 및 Search에 연결 @clear
# 함수 실행시 site_entry에 있는 내용이 data.json에 있다면 @clear
# true? email과 password를 출력
# false? "No details for the websire exists" @clear
# 애초에 data.json이 없다면 "No Data File Found." 출력 @clear


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)] + [random.choice(symbols) for _ in
                                                                           range(nr_symbols)] + [random.choice(numbers)
                                                                                                 for _ in
                                                                                                 range(nr_numbers)]

    random.shuffle(password_list)

    # password = ""
    # for char in password_list:
    #     password += char

    password = "".join(password_list)

    # print(f"Your password is: {password}")
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def find_password():
    site = site_entry.get()
    try:
        with open("data.json", "r") as data_file:
            data = json.load(data_file)
    except FileNotFoundError:
        messagebox.showinfo(title="Oops", message="No Data File Found.")
    else:
        try:
            found_email = data[site]["email"]
            found_password = data[site]["password"]
        except KeyError:
            messagebox.showinfo(title="Oops", message="No details for the websire exists")
        else:
            messagebox.showinfo(title="User_info", message=f"Email: {found_email}\nPassword: {found_password}")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_info():
    site = site_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    new_data = {
        site: {
            "email": email,
            "password": password,
        }
    }

    if len(site) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=site, message=f"These are the details entered: \n Email: {email}"
                                                           f"\nPassword: {password} \nIs it ok to save?")
        if is_ok:
            try:
                with open("data.json", "r") as data_file:
                    # 저장된 데이터를 읽어오고
                    data = json.load(data_file)  # 불러온 json의 타입은 딕셔너리

            except FileNotFoundError:
                with open("data.json", "w") as data_file:
                    # 업데이트 한 데이터를 저장한다.
                    json.dump(new_data, data_file, indent=4)

            else:
                # 데이터를 업데이트 해준뒤
                data.update(new_data)

                with open("data.json", "w") as data_file:
                    # 업데이트 한 데이터를 저장한다.
                    json.dump(data, data_file, indent=4)

            finally:
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

site_entry = Entry(width=21)
site_entry.grid(column=1, row=1)
site_entry.focus()
email_entry = Entry(width=35)
email_entry.insert(0, "myemail@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2)
password_entry = Entry(width=21)
password_entry.grid(column=1, row=3)

input_button = Button(text="Add", width=36, command=save_info)
input_button.grid(column=1, row=4, columnspan=2)
generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(column=2, row=3)
search_button = Button(text="Search", width=14, command=find_password)
search_button.grid(column=2, row=1)

window.mainloop()
