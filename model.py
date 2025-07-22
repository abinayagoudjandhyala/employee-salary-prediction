import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error
import numpy as np
import joblib

# Load dataset
df = pd.read_csv("HRDataset_v14.csv")

# Select features and target
features = [
    'GenderID', 'DeptID', 'PerfScoreID', 'EmpSatisfaction',
    'SpecialProjectsCount', 'Absences'
]
target = 'Salary'

X = df[features]
y = df[target]

# Train/test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "salary_model.pkl")

# Calculate RMSE
preds = model.predict(X_test)
rmse = np.sqrt(mean_squared_error(y_test, preds))
print(f"Model trained. RMSE: {rmse:.2f}")
