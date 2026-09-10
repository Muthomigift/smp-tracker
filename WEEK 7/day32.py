import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report

#features: [quotes_kes, job_type_encoded]
#job types: gate=0, window grills=1, door frame=2, roofsheet=3
#label: 1 = paid, 0 = pending/unpaid
x = np.array([
    [2800,0],[14500,1],[9800,2],[32000,0],[12000,1],
    [18500,0],[11000,2],[29500,0],[8500,3],[22000,1],
    [35000,0],[7200,2],[16000,3],[31000,0],[13500,1],
    [10500,2],[24000,0],[9000,3],[27000,1],[15000,2],
])
y = np.array([1,1,0,1,1,0,1,1,1,0,1,0,1,1,0,1,1,0,1,1])
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)

print("Job payment prediction report")
print(classification_report(y_test, y_pred, target_names=["unpaid", "paid"]))

