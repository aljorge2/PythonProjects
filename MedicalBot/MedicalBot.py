#############################
#  PSEUDO CODE FOR PROJECT
############################

#  PURPOSE: To create a medical diagnosis robot that diagnoses a 
#           patient’s state of dehydration based on a short questionnaire
#           given and prints out list of all saved patients and their 
#           diagnosis.

#  METHOD: 

# string that welcomes doctor and asks whether or not to list all patients
    #  to run a new diagnosis or to quit program
welcome_prompt = "Welcome doctor! What would you like to do today?\n - To list all patients, press 1\n - To run a new diagnosis, press 2\n - To quit, press q\n"

# asking for name of the doctor
doctors_prompt = "What is name of the doctor seeing the patient?\n"

#asking for name of the patient
patient_prompt= "What is the name of the patient?\n"

# prompt asking if patient is normal or lethargic 
appearance_prompt = "How is the patient's general appearance?\n - If normal appearance, press 1\n - If irritable or lethargic, press 2\n"

#prompt asking if patient's eyes are normal or very sunken
eye_prompt = "How are the patient's eyes?\n - If eyes normal or slightly sunken, press 1\n - If eyes very sunken, press 2\n"

# prompt asking if patient's skin patch is normal or slow
skin_prompt = "How is the patient's skin when you pinch it?\n - If skin patch is normal, press 1\n - If skin pinch is slow, press 2\n"

# if incorrect inputs 
error_message = "Could not save patient and diagnosis due to invalid input"

# string variables 
severe_dehydration = "Severe dehydration"
some_dehydration = "Some dehydration"
no_dehydration = "No dehydration"

#doctors,patients, and diagnosis
doctors_patients_and_diagnoses = [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
]

# function patient list
def list_patients():
    for patient in doctors_patients_and_diagnoses:
        print(patient)

def save_new_diagnosis(doctor_name, patient_name, diagnosis):
    if doctor_name == "" or patient_name == "" or diagnosis == "":
        print(error_message)
        return
    final_diagnosis = doctor_name + " - " + patient_name + " - " + diagnosis
    doctors_patients_and_diagnoses.append(final_diagnosis)
    print("Final diagnosis:", final_diagnosis, "\n")

# function prompting doctor about skin appearance
def assess_skin(skin):
    if skin == "1": # if 1 is pressed returning diagnosis
        return some_dehydration
    elif skin == "2": # if 2 is pressed returning diagnosis
        return severe_dehydration
    
    # prompting user to try again
    else:
        return ""

# function prompting doctor about child eyes and storing input
def assess_eyes(eyes):
    if eyes == "1": # if 1 is pressed returning diagnosis
     return no_dehydration
    elif eyes == "2": # if 2 is pressed returning diagnosis
     return severe_dehydration
    
    # prompting user to try again
    else:
        return ""

# function prompting doctor about child appearance and storing input
def assess_appearance():
    appearance = input(appearance_prompt) 
    
    # if 1 assess eyes   
    if appearance == "1": 
       eyes = input(eye_prompt)
       return assess_eyes(eyes)
    
    # if 2 assess skin
    elif appearance == "2":
     skin = input(skin_prompt)
     return assess_skin(skin)
    
    # prompting user to try again
    else:
        return ""
    
def start_new_diagnosis():
    doctor_name = input(doctors_prompt)
    patient_name = input(patient_prompt)
    diagnosis= assess_appearance()
    save_new_diagnosis(doctor_name, patient_name, diagnosis)

# function that prints welcome prompt, takes users input and stores variable
    # depending on users input it prompts different strings
def main():
    #keeps program running
    while(True): 
    #outputting prompt accepting users input and storing input
        selection = input(welcome_prompt)

    #if input is 1 runs function
        if selection == "1":
            list_patients()

    # if input is 2 runs function 
        elif selection == "2":
            start_new_diagnosis()
    
    # if input is q quits program
        elif selection == "q":
            return

#executing program
main()

#testing skin prompts

# Assessing all if-then-else cases for both skin and eyes
def test_assess_eyes():
    print(assess_eyes("1") == no_dehydration)
    print(assess_eyes("2") == severe_dehydration)
    print(assess_eyes("3") == "")
    
test_assess_eyes()

def test_assess_skin():
    print(assess_skin("1") == some_dehydration)
    print(assess_skin("2") == severe_dehydration)
    print(assess_skin("3") == "")

test_assess_skin()

# Assessing all cases of entries for doctor and patient and diagnosis
def test_save_new_diagnosis():
    save_new_diagnosis("", "","")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish", "","")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])
    save_new_diagnosis("","", "No dehydration")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])
    save_new_diagnosis("Nimish","", "Some dehydration")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])

    save_new_diagnosis("","Annika", "Some dehydration")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])

    save_new_diagnosis("Nimish","Annika", "")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])

    save_new_diagnosis("Nimish","Annika", "Some dehydration")
    print(doctors_patients_and_diagnoses == [
    "Annika - Mike - Severe dehydration",
    "Annika - Sally - No dehydration",
    "Annika - Kate - Some dehydration"
    ])

test_save_new_diagnosis()