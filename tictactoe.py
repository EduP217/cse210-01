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
        
        if result[0]:
            user_has_win = result[1]
            if user_has_win: 
                break
            
            if result[0] == "X":
                current_user = "Y"
            else:
                current_user = "X"
        else:
            current_user = result[0]
            user_has_win = True
    
    display_table()
    if current_user:
        print(f"The user {current_user} has won.")
    else:
        print("It was a draw!")
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
    if user_choice not in tics:
        tics[user_choice] = user
    else:
        print("Error - your choice has already been picked.")

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
    
    if '1' in user_choices and '2' in user_choices and '3' in user_choices:
        user_has_win = True
    
    if '4' in user_choices and '5' in user_choices and '6' in user_choices:
        user_has_win = True
    
    if '7' in user_choices and '8' in user_choices and '9' in user_choices:
        user_has_win = True
    
    if '1' in user_choices and '4' in user_choices and '7' in user_choices:
        user_has_win = True
        
    if '2' in user_choices and '5' in user_choices and '8' in user_choices:
        user_has_win = True
            
    if '3' in user_choices and '6' in user_choices and '9' in user_choices:
        user_has_win = True
        
    if '1' in user_choices and '5' in user_choices and '9' in user_choices:
        user_has_win = True
    
    if '3' in user_choices and '5' in user_choices and '7' in user_choices:
        user_has_win = True

    if not user_has_win:
        if len(tics) == 9:
            return None, None
        
    return user,user_has_win
    
if __name__ == "__main__":
    main()