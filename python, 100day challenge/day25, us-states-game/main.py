import turtle
import pandas as pd

# 유저의 입력을 받고 첫 글자를 자동으로 대문자로 처리해야함 # clear!
# 유저의 입력이 주의 이름과 일치한다 해당 주의 위치에 이름이 생긴다.
# 만약 틀렸다면 아무일도 일어나지않고 다시 텍스트 창을 보여준다.
# textinput의 title은 유저가 맞춘 갯수를 추적한다 ex) 14/50

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

df = pd.read_csv("50_states.csv")
state_lsit = df["state"].to_list()

correct_answer = []

while len(correct_answer) < 50:
    answer_state = screen.textinput(title=f"{len(correct_answer)}/50 correct",
                                    prompt="What's another state's name?").capitalize()

    if answer_state == "Exit":
        break

    elif answer_state in state_lsit and answer_state not in correct_answer:
        find_state = df[df["state"] == answer_state]
        correct_answer.append(answer_state)
        state_x = int(find_state.x)
        state_y = int(find_state.y)

        state = turtle.Turtle()
        state.hideturtle()
        state.penup()
        state.goto(state_x, state_y)
        state.write(answer_state, font=('Arial', 20, 'normal'))

print(f"당신의 점수는 50점 만점에 {len(correct_answer)}점 입니다")

# 유저가 맟추지 못한 주들을 저장한 CSV파일을 만든다.
miss_answer = [i for i in state_lsit if i not in correct_answer]

# # open 메서드로 저장하기
# with open("miss_answer.csv", "w") as file:
#     for i in miss_answer:
#         file.write(i + "\n")

# # pandas로 저장하기
miss_answer_df = pd.DataFrame(miss_answer)
miss_answer_df.to_csv("miss_answer.csv")




screen.exitonclick()