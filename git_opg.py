import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "heightcm": [172, 165, 181, 158, 175], 
    "weight_kg": [68, 72, 85, 54, 91], 
    "bmi": [None, None, None, None, None]
})

patients['bmi'] = patients['weight_kg'] / (patients['heightcm'] / 100) ** 2

print("Patients with calculated BMI:")
print(patients)
