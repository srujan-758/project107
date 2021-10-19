import csv
import pandas as pd
import plotly.express as px

df=pd.read_csv("pixel_math_game.csv")
#student_df=df.loc[df['student_id']=="TRL_zet"]

mean_levels=df.groupby("level",as_index=False)["attempt"].mean()
print(mean_levels)

fig=px.scatter(mean_levels,x="attempt",y="level",color="attempt",size="attempt")
fig.show()
