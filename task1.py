import pandas as pd
import matplotlib.pyplot as plt

data = pd.read_csv(r"C:\Users\sadhi\Downloads\worldpopulation.csv", skiprows=4)
print(data.head(20))
year = 2020
filtered_data = data[['Country Name', str(year)]].dropna()
filtered_data.columns = ['Country', 'Population']
filtered_data = filtered_data.sort_values(by='Population', ascending=False).head(20)
plt.figure(figsize=(14, 8))
plt.bar(filtered_data['Country'], filtered_data['Population'], color='red')
plt.xlabel('Country')
plt.ylabel('Population')
plt.title(f'Top 20 Countries by Population in {year}')
plt.xticks(rotation=45)
plt.show()
