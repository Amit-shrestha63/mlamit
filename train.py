import pandas as pd
from sklearn.linear_model import LinearRegression
from skops.models import dump, load

# load the data 
df=pd.read_csv ("data/housing_data 2.csv")

df.head()

#  separate features and target
x=df[('Area_sqft','Beadrooms','Age_years')]
y=df['Price']

# load the model
model= LinearRegression()
trained_model=model.fit(x,y)

# save the model
dump(trained_model, "model.skops")