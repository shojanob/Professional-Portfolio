#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("C:/Users/janob/PycharmProjects/100DaysOfCode/24/Input/Names/invited_names.txt") as names:
    guests = names.readlines()
    print(guests)

with open("C:/Users/janob/PycharmProjects/100DaysOfCode/24/Input/Letters/starting_letter.txt") as letter:
    contents = letter.read()
    for name in guests:
        fixed_name = name.strip()
        new_letter = contents.replace("[name]", fixed_name)
        with open(f"C:/Users/janob/PycharmProjects/100DaysOfCode/24/Output/ReadyToSend/invite_letter_to_{fixed_name}.txt", mode="w") as invite:
            invite.write(new_letter)
