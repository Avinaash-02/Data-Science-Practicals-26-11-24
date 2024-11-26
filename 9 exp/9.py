import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error,r2_score

#section 1
data=pd.read_csv(r"C:\Users\Avinaash Venkat\OneDrive\Desktop\Python Dated 12-10-24\Data Science Practical\9 exp\Housing.csv"4)
data=data.dropna()
data['furnishingstatus']=data['furnishingstatus'].map({"furnished":1,"semi-furnished":0.5,"unfurnished":0})
print(data.info())

features=['area','bedrooms','furnishingstatus']
target='price'

X=data[features]
y=data[target]
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.2,random_state=42)
model=LinearRegression()
model.fit(X_train,y_train)
y_pred=model.predict(X_test)
mse=mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)
print(f"Mean Squared Test{mse}")
print(f"r2_score{r2}")
def predict_housing_price():
    print("---------------------House Price Prediciton-------------------")
    area=float(input("Enter the area value here"))
    bedrooms=int(input("Enter the no of bedrooms"))
    furnishingstatus=float(input("Enter the furnished status value from 1 to 0"))
    user_input=pd.DataFrame({'area':[area],'bedrooms':[bedrooms],"furnishingstatus":[furnishingstatus]})
    predicted_price=model.predict(user_input)[0]
    print(f"Predicted House price{predicted_price}")
predict_housing_price()
