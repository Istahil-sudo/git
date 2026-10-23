#Exercise 3: Calculate average blood pressure
# Researchers measured systolic and diastolic blood pressure.
import pandas as pd

bp = pd.DataFrame({ 
    "patient_id": ["P01", "P02", "P03", "P04", "P05"], 
    "systolic": [118, 135, 142, 125, 155], 
    "diastolic": [76, 82, 91, 79, 95] 
})

mean_systolic = bp['systolic'].mean()
mean_diastolic = bp['diastolic'].mean()
print(f"Average Systolic Blood Pressure: {mean_systolic:.2f} mmHg")
print(f"Average Diastolic Blood Pressure: {mean_diastolic:.2f} mmHg")