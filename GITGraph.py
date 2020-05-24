
#Issac Rodriguez, Sprint 4.
import pandas as pd
from urllib import urlopen
import plotly.express as px



us_cities = pd.read_csv("https://raw.githubusercontent.com/Istackz/API-Database-Project/master/GITHUB.csv") #MAP of Data


fig = px.scatter_mapbox(us_cities, lat="lat ", lon="long", hover_name="title", hover_data=["location","url","created_at","how_to_apply"],
                        color_discrete_sequence=["blue"], zoom=2, height=900)

fig.update_layout(mapbox_style="open-street-map")
fig.update_layout(margin={"r":10,"t":30,"l":10,"b":10})
fig.update_layout(title="<b>GITHUB JOBS<b>")
fig.show()