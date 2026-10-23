#Exercise 5: Find the largest change in oxygen saturation - Patients had their oxygen saturation (SpO2) measured before and after treatment.

import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05"], 
    "spo2before": [94, 91, 96, 89, 93], 
    "spo2_after": [97, 95, 97, 94, 96], 
    "spo2_change": [None, None, None, None, None]
})

patients['spo2_change'] = patients['spo2_after'] - patients['spo2before']

print("Patients with SPO2 changes:")
print(patients)