welcome_prompt = ("Welcome doctor, what would you like to do today?\n "
                  "- To list all patients, press 1\n "
                  "- To run a new diagnosis, press 2\n "
                  "- To Quit, press q\n")

name_prompt = "What is the patient's name?\n"
appearance_prompt = ("How is the patient's general appearance?\n"
                     "- 1: Normal appearance\n"
                     "- 2: Irritable or lethargic\n")
eye_prompt = ("How are the patient's eyes?\n"
              "- 1: Eyes normal or slightly sunken\n"
              "- 2: Eyes very sunken\n")
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"


def list_patients():
    print("Listing patients and diagnoses")


def assess_skin():
    print("Assessing skin")


def assess_eyes():
    eyes = input(eye_prompt)
    if eyes == "1":
        return no_dehydration
    elif eyes == "2":
        return severe_dehydration


def assess_appearance():
    appearance = input(appearance_prompt)
    if appearance == "1":
        diagnosis = assess_eyes()
    elif appearance == "2":
        assess_skin()


def start_new_diagnosis():
    print("Starting a new diagnosis")
    name = input(name_prompt)
    assess_appearance()


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
