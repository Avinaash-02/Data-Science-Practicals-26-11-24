import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, plot_tree
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data
data = pd.read_csv(r"C:\Users\Avinaash Venkat\OneDrive\Desktop\Python Dated 12-10-24\Data Science Practical\11b\adult.csv")

# Check column names
print("Columns in the dataset:", data.columns)

# Preprocess the data
scaler = StandardScaler()

# Convert the income column to binary values (1 for >=50K, 0 for <50K)
data['income'] = data['income'].apply(lambda x: 1 if x == ">=50K" else 0)

# Drop missing values
data.dropna(inplace=True)

# Ensure correct feature names
X = data[['age', 'educational-num', 'capital-gain', 'hours-per-week']]  # Update column names as needed
y = data['income']

# Standardize the features
X_scaled = scaler.fit_transform(X)
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.5, random_state=42)

# Train the Decision Tree model
tree_model = DecisionTreeClassifier(random_state=42, class_weight='balanced')
tree_model.fit(X_train, y_train)

# Plot the Decision Tree
plt.figure(figsize=(10, 6))
plot_tree(tree_model, feature_names=['age', 'educational-num', 'capital-gain', 'hours-per-week'],
          class_names=['<=50K', '>50K'], filled=True, rounded=True)

plt.title("Decision Tree Classifier")
plt.show()

# Input for prediction
age = int(input("Enter age: "))
education_num = int(input("Enter education number: "))
capital_gain = int(input("Enter capital gain: "))
hours_per_week = int(input("Enter hours per week: "))

# Predict on new data
new_data = pd.DataFrame([[age, education_num, capital_gain, hours_per_week]],
                        columns=['age', 'education-num', 'capital-gain', 'hours-per-week'])
new_data_scaled = scaler.transform(new_data)
prediction = tree_model.predict(new_data_scaled)


