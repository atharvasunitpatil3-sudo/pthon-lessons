# Check Exam Eligibility

any_medical_cause = input("Did you have any medical cause ?(Y/N)").strip().upper()

if any_medical_cause == 'Y':
    print("You are allowed to appear for the exam...")
else:
    attendance = int(input("Enter your attendance percentage :"))

    #Nested if , inside else
    if attendance >= 75:
        print("You are allowed to appear for the exma...")
    else:
        print("You are not allowed...")