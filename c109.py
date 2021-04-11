import random
import plotly.express as px
import plotly.figure_factory as ff
import statistics
import plotly.graph_objects as go
count=[]
diceresult=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    diceresult.append(dice1+dice2)
    count.append(i)
#fig=px.bar(x=diceresult,y=count)
mean=sum(diceresult)/len(diceresult)
stdevation=statistics.stdev(diceresult)
median=statistics.median(diceresult)
mode=statistics.mode(diceresult)
print(mean)
print(stdevation)
print(mode)
print(median)
fig=ff.create_distplot([diceresult],['result'],show_hist=False)
#fig.show()
fsds,fsde=mean-stdevation,mean+stdevation
ssds,ssde=mean-(2*stdevation),mean+(2*stdevation)
tsds,tsde=mean-(3*stdevation),mean+(3*stdevation)

listofdatawithin1standarddevation=[result for result in diceresult if result>fsds and result<fsde]
listofdatawithin2ndstandarddevation=[result for result in diceresult if result>ssds and result<ssde]
listofdatawithin3rdstandarddevation=[result for result in diceresult if result>tsds and result<tsde]

print("{}% of data lies within First Standard Devation".format(len(listofdatawithin1standarddevation)*100/len(diceresult)))
print("{}% of data lies within Second Standard Devation".format(len(listofdatawithin2ndstandarddevation)*100/len(diceresult)))
print("{}% of data lies within Third Standard Devation".format(len(listofdatawithin3rdstandarddevation)*100/len(diceresult)))

fig.add_trace(go.Scatter(x=[mean,mean],y=[0,0.17],mode="lines",name="mean"))

fig.add_trace(go.Scatter(x=[fsds,fsds],y=[0,0.17],mode="lines",name="1start"))
fig.add_trace(go.Scatter(x=[fsde,fsde],y=[0,0.17],mode="lines",name="1end"))

fig.add_trace(go.Scatter(x=[ssds,ssds],y=[0,0.17],mode="lines",name="2start"))
fig.add_trace(go.Scatter(x=[ssde,ssde],y=[0,0.17],mode="lines",name="2end"))

fig.add_trace(go.Scatter(x=[tsds,tsds],y=[0,0.17],mode="lines",name="3start"))
fig.add_trace(go.Scatter(x=[tsde,tsde],y=[0,0.17],mode="lines",name="3start"))
fig.show()