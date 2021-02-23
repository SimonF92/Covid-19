import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv('data_2021-Feb-22.csv')

dfeng=df[df.Nation=='England']
dfeng['Rolling']=df['Normalised'].rolling(7).mean()
dfeng['num']=list(range(0,len(dfeng)))[::-1]
#dfeng['num']=dfeng['num']-7
dfeng

dfsc=df[df.Nation=='Scotland']
dfsc['Rolling']=df['Normalised'].rolling(7).mean()
dfsc['num']=list(range(0,len(dfsc)))[::-1]
#dfsc['num']=dfsc['num']-7

dfni=df[df.Nation=='Northern Ireland']
dfni['Rolling']=df['Normalised'].rolling(7).mean()
dfni['num']=list(range(0,len(dfni)))[::-1]
#dfni['num']=dfni['num']-7

dfwales=df[df.Nation=='Wales']
dfwales['Rolling']=df['Normalised'].rolling(7).mean()
dfwales['num']=list(range(0,len(dfwales)))[::-1]
#dfwales['num']=dfwales['num']-7

full=pd.concat([dfeng,dfsc,dfni,dfwales])




plt.figure(figsize=(20,8))

sns.scatterplot(full.num,full.Normalised,hue=full.Nation,size=1,legend=False)
sns.lineplot(full.num,full.Rolling,hue=full.Nation,dashes=False,linewidth=2)

plt.ylabel('Deaths Per 100,000 people',size=15)
plt.xlabel('Day after March 2nd 2020',size=15)

plt.savefig('Cov_Daily_Deaths.png')


plt.figure(figsize=(20,8))

sns.lineplot(full.num,full.Normalised_Cum,hue=full.Nation,dashes=False,linewidth=2)

plt.ylabel('Cumulative Deaths Per 100,000 people',size=15)
plt.xlabel('Day after March 16th 2020',size=15)

plt.savefig('Cov_Cumulative_Deaths.png')
