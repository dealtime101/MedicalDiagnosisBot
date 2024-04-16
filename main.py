welcome_prompt = ("Welcome doctor, what would you like to do today?\n "
                  "- To list all patients, press 1\n "
                  "- To run a new diagnosis, press 2\n "
                  "- To Quit, press q\n")


name_prompt = "What is the patient's name?\n"
appearance_prompt = ("How is the patient's general appearance?\n"
                     "- 1: Normal appearance\n"
                     "- 2: Irritable or lethargic\n")


def list_patients():
    print("Listing patients and diagnoses")


def assess_skin():
    print("Assessing skin")


def assess_eyes():
    print("Assessing eyes")


def start_new_diagnosis():
    print("Starting a new diagnosis")
    name = input(name_prompt)
    appearance = input(appearance_prompt)
    if appearance == "1":
        assess_eyes()
    elif appearance == "2":
        assess_skin()


def main():
    while True:
        doctor_selection = input(welcome_prompt)
        if doctor_selection == "1":
            list_patients()
        elif doctor_selection == "2":
            start_new_diagnosis()
        elif doctor_selection == "q":
            return


main()
