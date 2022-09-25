import random
from replit import clear
import hangman_art, hangman_word

print(hangman_art.logo)

life = 6

chosen_word = random.choice(hangman_word.word_list)
print(f"chosen word is {chosen_word}")


reslut = []
for _ in range(len(chosen_word)):
    reslut.append("_")

end_of_game = False

while not end_of_game:
    guess = input("Guess a letter:\n").lower()

    # 리플잇에서 지원하는 커맨드 초기화 명령어
    clear()
    
    print("---------------------------")
    
    if guess in reslut:
        print(f"You've already guessed {guess}")
        
    for index in range(len(chosen_word)):
        if chosen_word[index] == guess:
            reslut[index] = guess

    if guess not in chosen_word:
        life -= 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

    
    print(hangman_art.stages[life])
    print(" ".join(reslut))
    
    # 종료 조건
    if  "_" not in reslut:
        end_of_game = True
        print("you win")

    if life == 0:
        end_of_game = True
        print("You lose")

