import os

# Constants:
FORMS_FOLDER = "forms/"

def choose_action():
    # Printing user instructions:
    print("\nchoose an action")
    print("1. import a form")
    print("2. fill in a form")

    # Getting the user's choice:
    user_choice = input("")

    # Condition: input isn't a number
    if not user_choice.isdigit():
        raise ValueError("Error: invalid action choice")
    
    # Condition: input is out of range
    if int(user_choice) < 1 or \
        int(user_choice) > 2:
        raise ValueError("Error: invalid action choice")
    
    return int(user_choice) - 1


def choose_form():
    # Inits:
    form_files_list = os.listdir(FORMS_FOLDER)

    # Condition: no form files
    if len(form_files_list) == 0:
        raise ValueError("Error: no form files imported")
    
    # Printing the available form files:
    print("Choose a form:")
    for i in range(len(form_files_list)):
        print(str(i + 1) + ". " + form_files_list[i][:-5])
    
    # Getting the user's input:
    user_form_choice = input("")

    # Condition: input isn't a number
    if not user_form_choice.isdigit():
        raise ValueError("Error: invalid form choice")
    
    # Condition: input is out of range
    if int(user_form_choice) < 1 or \
        int(user_form_choice) > len(form_files_list):
        raise ValueError("Error: invalid form choice")

    return form_files_list[int(user_form_choice) - 1]