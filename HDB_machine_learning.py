import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestRegressor
import datetime as dt
import matplotlib.pyplot as plt

df = pd.read_csv('/Users/aa/Desktop/hdb_cooling_analysis/data/raw/ResaleflatpricesbasedonregistrationdatefromJan2017onwards.csv')


print("Data from Jan 2017 to Sep 2025")
print(f"Total records: {len(df)}")

df['remaining_lease'] = 99 - (2025 - df['lease_commence_date'])
print(df.head())
simple_df = df[['town', 'flat_type', 'floor_area_sqm', 'remaining_lease', 'resale_price']]
simple_df = simple_df.dropna()

#Categorising town and bedroom size into numerical values
simple_df['town_code'] = simple_df['town'].astype('category').cat.codes
simple_df['flat_type_code'] = simple_df['flat_type'].astype('category').cat.codes

#Separating into X and Y variables, where X is are independent (factors) and Y is dependent (price of flat)
X = simple_df[['town_code', 'flat_type_code', 'floor_area_sqm', 'remaining_lease']]
Y = simple_df['resale_price']

#Model training
model = RandomForestRegressor(n_estimators = 50, random_state = 42)
model.fit(X, Y)

feature_names = ['Town', 'Flat Type', 'Floor Area', 'Remaining Lease']
importances = model.feature_importances_

print("Factors that affect the price and by how much:")
for name, impt in zip(feature_names, importances):
    print(f"{name}:{impt:.1%}")


#Edit and filter as you please over here! Fascinating insights can be drawn from this. Please ensure that the town and flat type exist in the dataset and are capitalised. 
test_houses = [
    ('BISHAN', '3 ROOM', 100, 1990),
    ('BUKIT TIMAH', '3 ROOM', 100, 1980),
    ('TAMPINES', '5 ROOM', 120, 2000),
    ('JURONG WEST', '2 ROOM', 50, 2010),
    ('MARINE PARADE', '4 ROOM', 890, 1995)
]

for town, flat_type, floor_area, lease_year in test_houses:
    town_code = simple_df[simple_df['town'] == town]['town_code'].iloc[0]
    flat_type_code = simple_df[simple_df['flat_type'] == flat_type]['flat_type_code'].iloc[0]
    remaining_lease = 99 - (2025 - lease_year)

    features = [[town_code, flat_type_code, floor_area, remaining_lease]]
    predicted_price = model.predict(features)[0]
    print(f"Predicted price for a {flat_type} in {town} with {floor_area} sqm and {remaining_lease} years remaining lease: ${predicted_price:,.2f}")





