welcome_prompt = ("Welcome doctor, what would you like to do today?\n - To list all patients, press 1\n "
                  "- To run a new diagnosis, press 2\n - To Quit, press q\n")


def list_patients():
    print("Listing patients and diagnoses")


def start_new_diagnosis():
    print("Starting a new diagnosis")


def main():
    doctor_selection = input(welcome_prompt)
    if doctor_selection == "1":
        list_patients()
    elif doctor_selection == "2":
        start_new_diagnosis()
    elif doctor_selection == "q":
        return


main()
