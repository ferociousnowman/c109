import random
import plotly.express as px
import plotly.figure_factory as ff
import pandas as pd
import csv 
import statistics
import plotly.graph_objects as go

df=pd.read_csv("data.csv")
hlist=df["Height(Inches)"].to_list()
wlist=df["Weight(Pounds)"].to_list()


#fig=px.bar(x=diceresult,y=count)
hmean=statistics.mean(hlist)
wmean=statistics.mean(wlist)

hstdevation=statistics.stdev(hlist)
wstdevation=statistics.stdev(wlist)

hmedian=statistics.median(hlist)
hmode=statistics.mode(hlist)

wmedian=statistics.median(wlist)
wmode=statistics.mode(wlist)

print("mean for height",hmean)
print("stdevation for height ",hstdevation)
print("mode for height",hmode)
print("median for height",hmedian)



fig=ff.create_distplot([hlist],['result'],show_hist=False)
#fig.show()
fsds,fsde=hmean-hstdevation,hmean+hstdevation
ssds,ssde=hmean-(2*hstdevation),hmean+(2*hstdevation)
tsds,tsde=hmean-(3*hstdevation),hmean+(3*hstdevation)

listofdatawithin1standarddevation=[result for result in hlist if result>fsds and result<fsde]
listofdatawithin2ndstandarddevation=[result for result in hlist if result>ssds and result<ssde]
listofdatawithin3rdstandarddevation=[result for result in hlist if result>tsds and result<tsde]

print("{}% of data lies within First Standard Devation".format(len(listofdatawithin1standarddevation)*100/len(hlist)))
print("{}% of data lies within Second Standard Devation".format(len(listofdatawithin2ndstandarddevation)*100/len(hlist)))
print("{}% of data lies within Third Standard Devation".format(len(listofdatawithin3rdstandarddevation)*100/len(hlist)))

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode="lines",name="1start"))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode="lines",name="1end"))

fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode="lines",name="2start"))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode="lines",name="2end"))

fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode="lines",name="3start"))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode="lines",name="3start"))
fig.show()