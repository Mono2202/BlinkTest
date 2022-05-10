import menu, form

# Constants:
FUNCTION_LIST = [form.import_form, form.fill_form]

def main():
    # Printing welcome message:
    print("Welcome, ", end="")

    while True:

        try:
            # Getting action:
            FUNCTION_LIST[menu.choose_action()]()

        # Catching value errors:
        except ValueError as e:
            print(e)

        # Catching other exceptions:
        except Exception as e:
            print(e)


if __name__ == "__main__":
    main()