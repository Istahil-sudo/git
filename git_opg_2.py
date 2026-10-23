#Exercise 2: Find patients with high heart rate - A nurse records resting heart rate during a clinical visit.

import pandas as pd

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05", "P06"], 
    "heartrate": [72, 88, 105, 64, 112, 79] 
})

high_heart_rate_patients = patients[patients['heartrate'] > 100]
print("Patients with high heart rate:")
print(high_heart_rate_patients)
