# import the library
import folium

import pandas as pd

# Make a data frame with dots to show on the map
data = pd.read_excel(r'C:\Users\Desktop\Sales.xlsx',sheet_name='Sheet2')
# data['I'] = ((data['Net2019']/data['Net2018']-1)*100).round(1).astype(str) + '%'
# data.to_excel(r'C:\Users\RaboshcV\Desktop\Sales.xlsx',sheet_name='Sheet2')

# Make an empty map
m = folium.Map(location=[49.5,32], tiles="Mapbox Bright", zoom_start=7)

#adding marker one by one on the map

for i in range(0,len(data)):
 if data.iloc[i]['Diff'] >0:
    folium.Circle(
      location=[data.iloc[i]['Lat'], data.iloc[i]['Long']],
      radius=data.iloc[i]['Net2019']/100,
      color='green',
      fill=True,
      fill_color='green',
   ).add_to(m)
 else:
     folium.Circle(
      location=[data.iloc[i]['Lat'], data.iloc[i]['Long']],
      radius=data.iloc[i]['Net2019']/100,
      color='crimson',
      fill=True,
      fill_color='crimson',
   ).add_to(m)

for k in range(0,len(data)):
    folium.map.Marker([data.iloc[k]['Lat']-0.27, data.iloc[k]['Long']+0.49],
    icon=folium.DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-weight:bold;font-size: 13.5pt">%s</div>' % data.iloc[k]['Net2019']
        )
    ).add_to(m)

for j in range(0,len(data)):
   folium.map.Marker(
    [data.iloc[j]['Lat'], data.iloc[j]['Long']+0.59],
    icon=folium.DivIcon(
        icon_size=(150,36),
        icon_anchor=(0,0),
        html='<div style="font-size: 13.5pt;font-weight:bold">%s</div>' % data.iloc[j]['Diff2'] ,
        )
    ).add_to(m)

# # Save it as html

m.save(r'C:\Users\Desktop\mymap.html')

