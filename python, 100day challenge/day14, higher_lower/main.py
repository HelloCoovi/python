import art
from game_data import data
import random

print(art.logo)


def random_pick():
    """data에서 랜덤한 요소를 뽑아온다"""
    return random.choice(data)

def print_data(data):
    """data의 이름, 직업, 지역을 출력해준다"""
    return f"{data['name']}, a {data['description']}, from {data['country']}."
    
def get_answer(a_option, b_option):
    """팔로워가 더 많은 option을 찾아준다."""
    a_follower = a_option["follower_count"]
    b_follower = b_option["follower_count"]
    if a_follower > b_follower:
        return "a"
    elif b_follower < a_follower:
        return "b"
    
    
# 각각 A,B에 할당


# 사용자의 입력을 받고 follower_count가 더 많은 사람을 맞추면 또 다시 랜덤하게 뽑는다.
def game():
    score = 0
    game_over = False
    
    while not game_over:
        a_option = random_pick()
        b_option = random_pick()
        while a_option == b_option:
            b_option = random_pick()
        
        answer = get_answer(a_option, b_option)
        
        if score > 0:
            print("------------------------------------------------------------------")
            print(f"You're right! Current score: {score}")
    
        print(f"Compare A : {print_data(a_option)}")
        print(art.vs)
        print(f"Compare B : {print_data(b_option)}")
        
        guess = input("Who has more followers? Type 'A' or 'B':\n -> ").lower()
        
        if guess == answer:
            score += 1
        elif guess != answer:
            print(f"Sorry, that's wrong. Final score: {score}")
            game_over = True
        

game()