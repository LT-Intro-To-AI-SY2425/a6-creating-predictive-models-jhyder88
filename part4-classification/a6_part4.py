import pandas as pd
from sklearn import linear_model
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

data = pd.read_csv("part4-classification/suv_data.csv")
data['Gender'].replace(['Male','Female'],[0,1],inplace=True)

x = data[["Age", "EstimatedSalary", "Gender"]].values
y = data["Purchased"].values

# Step 1: Print the values for x and y
print(data)
# Step 2: Standardize the data using StandardScaler, 
scaler = StandardScaler().fit(x)
x = scaler.transform(x)
# Step 3: Transform the data
x = scaler.transform(x)
# Step 4: Split the data into training and testing data
x_train, x_test, y_train, y_test = train_test_split(x, y)
# Step 5: Fit the data
model = linear_model.LogisticRegression().fit(xTraining,yTraining)
# Step 6: Create a LogsiticRegression object and fit the data
model = linear_model.LogisticRegression().fit(x_train, y_train)
# Step 7: Print the score to see the accuracy of the model
print("Model Score:", model.score(xTest, yTest))
# Step 8: Print out the actual ytest values and predicted y values
# based on the xtest data
for index in range(len(xTest)):
    obs_x = xTest[index]
    obs_x = obs_x.reshape(-1,3)
    print("Personal Information:", obs_x)
    
    if model.predict(obs_x) == 1:
        pred = True
    else:
        pred = False
    if pred:
        print("Prediction: Purchased")
    else:
        print("Prediction: Not Purchased")

    if yTest[index] == 1:
        acc = True
    else:
        acc = False
    if acc:
        print("Actual: Purchased")
    else:
        print("Actual: Not Purchased")
    
    if pred == acc:
        print("The Model is Correct")
    else:
        print("The Model is not Correct")