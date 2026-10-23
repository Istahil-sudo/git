#Exercise 4: Classify patients by blood glucose - Scenario: Blood glucose was measured during a screening study


import pandas as pd 
import numpy as np

patients = pd.DataFrame({ 
    "patientid": ["P01", "P02", "P03", "P04", "P05", "P06"], 
    "glucosemmol_l": [4.8, 6.1, 8.4, 5.2, 7.2, 3.9],
    "glucose_level": [None, None, None, None, None, None]
})
#Use these categories: below 4.0 -> “low” 4.0 to 6.9 -> “normal” 7.0 or higher -> “high”

low_glucose_threshold = 4.0
normal_glucose_threshold = 6.9
high_glucose_threshold = 7.0

patients['glucose_level'] = np.where(patients['glucosemmol_l'] < low_glucose_threshold, 'low',
                            np.where(patients['glucosemmol_l'] <= normal_glucose_threshold, 'normal', 'high'))
print("Patients classified by blood glucose level:")
print(patients)

