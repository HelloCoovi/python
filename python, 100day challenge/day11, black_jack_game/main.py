from random import choice
from art import logo

print(logo)

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def draw(player):
    player.append(choice(cards))


player_card = [choice(cards), choice(cards)]
computer_card = [choice(cards), choice(cards)]

print(f"Your cards: {player_card}, current score: {sum(player_card)}")
print(f"Computer's first card: {computer_card[0]}")

def blackjack(player_card, computer_card):
    
    while True:
        draw_card = input("Type 'y' to get another card, type 'n' to pass: ")
    
        if draw_card == "y":
            draw(player_card)
            print(f"Your cards: {player_card}, current score: {sum(player_card)}")
            if sum(player_card) > 21:
                print("You loss, Your score is over 21")
                return
        else:
            break
    
    while sum(computer_card) < 18:
        draw(computer_card)
        if sum(computer_card) > 21:
            print("You win, The computer was greedy")
            return
    
    print(f"Your final hand: {player_card}, final score: {sum(player_card)}")
    print(f"Computer's final hand: {computer_card}, final socre: {sum(computer_card)}")
    
    if sum(player_card) > sum(computer_card):
        print("You win")
    elif sum(player_card) < sum(computer_card):
        print("You loss")
    else:
        print("Draw")

            
blackjack(player_card, computer_card)
    
    
