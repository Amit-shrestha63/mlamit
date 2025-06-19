import pandas as pd
from sklearn.linear_model import LinearRegression
from skops.io import dump, load

# load the data 
df=pd.read_csv ("housing_data 2.csv")

df.head()

#  separate features and target
x=df[["Area_sqft","Bedrooms","Age_years"]]
y=df["Price_$"]

# load the model
model= LinearRegression()
trained_model=model.fit(x,y)

# save the model
dump(trained_model, "model/model.skops")