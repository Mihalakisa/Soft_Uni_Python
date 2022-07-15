days = int(input())
doctors = 7
unexamined_patients = 0
reviewed_patients = 0

for i in range(1, days + 1):
    patients = int(input())

    if i % 3 == 0:
        if unexamined_patients > doctors:
            doctors += 1

    if patients > doctors:
        patients -= doctors
        unexamined_patients += patients
        reviewed_patients += doctors
    else:
        reviewed_patients += patients

print(f"Treated patients: {reviewed_patients}.")
print(f"Untreated patients: {unexamined_patients}.")