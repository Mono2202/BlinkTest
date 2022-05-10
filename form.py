import os, json, shutil, menu

# Constants:
FORMS_FOLDER = "forms/"
FILLED_FORMS_FOLDER = "filled_forms/"

# Gloabls:
FILLED_FORM_ID = 0

def import_form():
    # Getting the form's path from the user:
    form_path = input("enter the path to the form\n")

    # Condition: file isn't json
    if form_path[-4:] != "json":
        raise ValueError("Error: incorrect file type, not json")

    # Condition: file doesn't exist
    if not os.path.exists(form_path):
        raise ValueError("Error: file doesn't exist")
    
    # Reading the file:
    with open(form_path, "r") as json_file:
        data = json_file.read()

    # Converting string to json object:
    json_data = json.loads(data)

    # Checking whether the file is valid according
    # to the json format:
    check_file_format(json_data)

    # Adding the json file to the forms folder:
    shutil.copyfile(form_path, FORMS_FOLDER + json_data["form_name"] + ".json")


def fill_form():
    # Setting global variables:
    global FILLED_FORM_ID

    # Getting the correct form to fill:
    form_name = menu.choose_form()
    form_file_path = FORMS_FOLDER + form_name

    # Reading the form file:
    with open(form_file_path, "r") as json_file:
        data = json_file.read()

    # Converting string to json object:
    json_data = json.loads(data)
    json_filled_form = dict.fromkeys(json_data["answers"], "")
    
    # Printing the questions for the user:
    for field in json_data["questions"]:
        
        # Condition: question with no needed previous response
        if isinstance(json_data["questions"][field], str):
            
            # Getting the user's answer:
            current_field_answer = input(json_data["questions"][field][:-4])

            # Condition: answer needs to be a given option
            if isinstance(json_data["answers"][field], list):

                # Condition: user's answer isn't a given option
                if current_field_answer not in json_data["answers"][field]:
                    raise ValueError("Error: answer not a valid option")
            
            # Condition: user skipped a mandatory question
            if current_field_answer == "" and \
                json_data["questions"][field][-3:] == "[M]":
                raise ValueError("Error: question is mandatory")

            # Saving the user's answer:
            json_filled_form[field] = current_field_answer

        # Condition: question with needed previous responses
        else:

            # Getting the needed fields:
            needed_fields = json_data["questions"][field]["needed_fields"]

            for needed_field in needed_fields:
                
                # Condition: selected option doesn't relate to current question
                if json_filled_form[needed_field] not in json_data["questions"][field][needed_field].keys():
                    continue

                # Getting the user's answer:
                current_field_answer = input(json_data["questions"][field][needed_field][json_filled_form[needed_field]][:-4])

                # Condition: answer needs to be a given option
                if isinstance(json_data["answers"][field][needed_field], list):

                    # Condition: user's answer isn't a given option
                    if current_field_answer not in json_data["answers"][field]:
                        raise ValueError("Error: answer not a valid option")
                
                # Condition: user skipped a mandatory question
                if current_field_answer == "" and \
                    json_data["questions"][field][needed_field][json_filled_form[needed_field]][-3:] == "[M]":
                    raise ValueError("Error: question is mandatory")

                # Saving the user's answer:
                json_filled_form[field] = current_field_answer

    # Setting the filled from file path
    filled_form_file_path = FILLED_FORMS_FOLDER + form_name[:-5] + str(FILLED_FORM_ID) + ".json"

    # Saving the filled form to a file:
    with open(filled_form_file_path, "w") as json_file:
        json.dump(json_filled_form, json_file)
    
    # User messages:
    print("Thank you for filling the form!")
    print("Form was saved @" + filled_form_file_path)

    # Raising the filled form file ID:
    FILLED_FORM_ID += 1


def check_file_format(json_data):
    # Reading the json main keys:
    main_keys = json_data.keys()

    # Condition: no form name field
    if "form_name" not in main_keys:
        raise ValueError("Error: no \"form_name\" key")

    # Condition: no questions field
    if "questions" not in main_keys:
        raise ValueError("Error: no \"questions\" key")
    
    # Condition: no answers field
    if "answers" not in main_keys:
        raise ValueError("Error: no \"answers\" key")
    
    # Reading the answers keys:
    answer_keys = json_data["answers"].keys()

    # Reading the questions keys:
    question_keys = json_data["questions"].keys()

    # Condition: questions and answers don't match
    if answer_keys != question_keys:
        raise ValueError("Error: questions and answers don't match")