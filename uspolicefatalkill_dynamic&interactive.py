# -*- coding: utf-8 -*-
"""USpolicefatalkill_dynamic&interactive.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1xX7XYwkEUM8kEgA_aQ1R-50vi-lAqZtA
"""

import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
import folium 
from folium import plugins
import numpy as np


df = pd.read_csv("./5624.csv")
df.head(1)

import plotly.graph_objects as go

import pandas as pd

b = df.dropna()

mans = np.array(b.manner_of_death)
man, count1 = np.unique(mans, return_counts=True)

mans1 = np.array(b.signs_of_mental_illness)
man4, count2 = np.unique(mans1, return_counts=True)

mans2 = np.array(b.armed)


for i in range(len(mans2)) :
    if ( mans2[i] != "gun") and (mans2[i] != "knife") and (mans2[i] != "unarmed") and (mans2[i] != "toy weapon"):
        mans2[i] = "others"

man5, count3 = np.unique(mans2, return_counts=True)

mans3 = np.array(b.gender)
man6, count4 = np.unique(mans3, return_counts=True)

# How to change plot data using dropdowns
#
# This example shows how to manually add traces
# to the plot and configure the dropdown to only
# show the specific traces you allow.

fig = go.Figure()


fig.add_trace(
    go.Pie(labels=man, values=count1)
)
fig.add_trace(
    go.Pie(labels=man4, values=count2)
)
fig.add_trace(
    go.Pie(labels=man5, values=count3)
)
fig.add_trace(
    go.Pie(labels=man6, values=count4)
)
    
fig.update_layout(
    updatemenus=[go.layout.Updatemenu(
        active=0,
        buttons=list(
            [
                
             dict(label = 'manner of death',
                  method = 'update',
                  args = [{'visible': [True, False, False, False]}, # the index of True aligns with the indices of plot traces
                          {'title': 'Manner of death',
                           'showlegend':True}]),
             dict(label = 'mental illness',
                  method = 'update',
                  args = [{'visible': [False, True, False, False]},
                          {'title': 'The dead person has mental illness?',
                           'showlegend':True}]),
             dict(label = 'armed',
                  method = 'update',
                  args = [{'visible': [False, False, True, False]},
                          {'title': 'What kind of weapon did the dead person armed with?',
                           'showlegend':True}]),
             dict(label = 'gender',
                  method = 'update',
                  args = [{'visible': [False, False, False, True]},
                          {'title': 'Gender Distribution',
                           'showlegend':True}]),
            ])
        )
    ])

fig.show()

newmap = folium.Map([40, -90], zoom_start=4)

for (index, row) in df.dropna().iterrows():
    
    if row.loc['race'] == 'H':
                  folium.CircleMarker(location=[row.loc['latitude'],row.loc['longitude']],radius = 3,
                  tooltip='name:' + row.loc['name'][0] +'  race: '+row.loc['race']+ ' '+row.loc['date']  , color = 'blue'
                  ).add_to(newmap)
        
    if row.loc['race'] == 'W':
                  folium.CircleMarker(location=[row.loc['latitude'],row.loc['longitude']],radius = 3,
                  tooltip='name:' + row.loc['name'][0] +'  race: '+ row.loc['race']+' '+row.loc['date']  , color = 'purple'
                  ).add_to(newmap)
    if row.loc['race'] == 'A':
                  folium.CircleMarker(location=[row.loc['latitude'],row.loc['longitude']],radius = 3,
                  tooltip='name:' + row.loc['name'][0] +'  race: '+row.loc['race']+ ' '+row.loc['date']  , color = 'green'
                  ).add_to(newmap)
    if row.loc['race'] == 'B':
                  folium.CircleMarker(location=[row.loc['latitude'],row.loc['longitude']],radius = 3,
                  tooltip='name:' + row.loc['name'][0] +'  race:'+row.loc['race']+ ' '+row.loc['date']  , color = 'grey'
                  ).add_to(newmap)
            
loc = 'People killed by US Police in recent 5 years'
title_html = '''
             <h3 align="center" style="font-size:16px"><b>{}</b></h3>
             '''.format(loc)   

newmap.get_root().html.add_child(folium.Element(title_html))
    
newmap

states = np.array(df.state)
unique, counts = np.unique(states, return_counts=True)
ages = np.array(df.age)
unique2, counts2 = np.unique(ages, return_counts=True)

import plotly.graph_objects as go
from plotly.offline import iplot


trace_men = go.Bar(x=unique2,
                y=counts2,
                name='age',
                marker=dict(color='#A2D5F2'))

aos = go.Bar(x= unique, y = counts, name='States',
                  marker=dict(color='#ffcdd2'))

layout = go.Layout(title="USPolice fatal kill by states and ages")


data = [aos,trace_men]
fig = go.Figure(data=data, layout=layout)

fig.show()

