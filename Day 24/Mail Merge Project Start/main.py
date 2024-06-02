with open("/100 Days Challenge/Day 24/Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    names = file.readlines()
with open("/100 Days Challenge/Day 24/Mail Merge Project Start/Input/Letters/starting_letter.txt") as mail_file:
    txt = mail_file.read()
    for item in names:
        x = txt.replace('[name]', item.strip())
        with open(f"./Output/ReadyToSend/letter_for_{item.strip()}",mode="w") as new_file:
            new_file.write(x)


