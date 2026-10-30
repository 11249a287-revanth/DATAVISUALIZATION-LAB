import pandas as pd
import numpy as np

data = {
    "Student": [
        "Srinivas", "Siva", "Naveen", "Srinath", "Ganesh",
        "Anil", "Deep", "Radhakrishna", "Kiran", "Harsha"
    ],
    "Math": [82, 72, 91, 65, 78, 85, 60, 95, 70, 83],
    "Science": [90, 82, 76, 88, 72, 80, 91, 85, 94, 80],
    "English": [91, 78, 89, 88, 86, 87, 83, 92, 97, 90],
    "Age": [17, 18, 16, 19, 17, 18, 16, 19, 17, 18],
    "Hours_Studied": [3, 4, 5, 7, 8, 10, 2, 4, 5, 6]
}

df = pd.DataFrame(data)
print(df)
