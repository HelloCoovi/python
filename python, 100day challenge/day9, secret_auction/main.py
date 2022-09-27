from art import logo
from replit import clear

print(logo)

going = True

while going:
    players = {}
    name = input("What is your name?: ")
    pay = int(input("What is your bid?: $"))
    
    players[name] = pay

    player = input("Are there any other bidders? Type 'yes or 'no'.\n")
    
    clear()

    if player == "no":
        going = False

winner = ""
highest_bid = 0

for i in players:
    if players[i] > highest_bid:
        highest_bid = players[i]
        winner = i
    
print(f"The winner is {winner} with a bid of ${highest_bid}")