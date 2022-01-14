# Tic-Tac-Toe
# Author: Eduardo Prieto

tics = dict()

def main():
    user_has_win = False
    current_user = "X"
    while not user_has_win:
        display_table()
        ask_user_choice(current_user)
        result = check_result(current_user)
        
        user_has_win = result[1]
        if user_has_win: 
            break
        
        if result[0] == "X":
            current_user = "Y"
        else:
            current_user = "X"
    
    display_table()
    print(f"The user {current_user} has won.")
    print("Good game. Thanks for playing!")

# display_table():
# process: print the table structure of tic tac toe
def display_table():
    print()
    row_line = ""
    for x in range(1,10):
        if x in tics:
            el = f"{tics[x]}"
        else:
            el = f"{x}"
        
        if x == 2 or x == 5 or x == 8:
            el = f" | {el} | "
            
        row_line += el
        
        if x % 3 == 0:
            print(row_line)
            row_line = ""
            if x <= 6:
                print("- + - + -")
    print()

# ask_user_choice(user):
# input: the user's code
# process: get the user's choice and set it to the global dict
def ask_user_choice(user):
    user_choice = int(input(f"{user}'s turn to choose a square (1-9): "))
    tics[user_choice] = user

# check_result(user):
# input: the user's code
# process: the process checks if user choices matches with pattern
# output: return user's code and user_has_win boolean
def check_result(user):
    user_choices = ""
    user_has_win = False
    for tac in tics:
        toe = tics[tac]
        if toe == user:
            user_choices += str(tac)
    
    if '159' in user_choices or '591' in user_choices or '951' in user_choices:
        user_has_win = True
    elif '915' in user_choices or '195' in user_choices or '519' in user_choices:
        user_has_win = True
    
    if '258' in user_choices or '582' in user_choices or '852' in user_choices:
        user_has_win = True
    elif '285' in user_choices or '528' in user_choices or '825' in user_choices:
        user_has_win = True
    
    if '357' in user_choices or '573' in user_choices or '753' in user_choices:
        user_has_win = True
    elif '375' in user_choices or '537' in user_choices or '735' in user_choices:
        user_has_win = True
    
    if '147' in user_choices or '471' in user_choices or '714' in user_choices:
        user_has_win = True
    elif '174' in user_choices or '417' in user_choices or '741' in user_choices:
        user_has_win = True
    
    if '369' in user_choices or '693' in user_choices or '936' in user_choices:
        user_has_win = True
    elif '396' in user_choices or '639' in user_choices or '963' in user_choices:
        user_has_win = True

    return user,user_has_win
    
if __name__ == "__main__":
    main()