#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("./input/Letters/starting_letter.txt", "r") as letter_file:
    base_letter = letter_file.read()

with open("./input/Names/invited_names.txt", "r") as name_file:
    names = name_file.readlines()
    for i in range(len(names)):
        names[i] = names[i].strip()


for name in names:
    file = open(f"./Output/ReadyToSend/letter_for_{name}.txt", "w")
    text = base_letter.replace("[name]", name)
    file.write(text)

file.close()

