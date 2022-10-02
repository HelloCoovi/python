import art
import random

print(art.logo)

level  = input("난이도를 입력하세요.\n'EASY' 혹은 'HARD'").lower()

if level == "easy":
    turn = 10
elif level == "hard":
    turn = 5


answer = random.randint(1, 99)

game_over = False

while not game_over:
    if turn <= 0:
        game_over = True
    
    guess = int(input("정답은?"))
    
    if guess > answer:
        print("추측한 숫자가 큽니다.")
        turn -= 1
        print(f"남은 턴 {turn}")
    elif guess < answer:
        print("추측한 숫자가 작습니다.")
        turn -= 1
        print(f"남은 턴 {turn}")
    elif guess == answer:
        print(f"정답은 {answer} 입니다!")
        game_over = True




