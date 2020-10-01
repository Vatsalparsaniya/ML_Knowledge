# Import required libraries
import pandas as pd 
import numpy as np 
import numpy as np
import matplotlib.pyplot as plt  
pd.set_option('display.max_rows', 500)
pd.set_option('display.max_columns', 500)
pd.set_option('display.width', 1000)

data = pd.read_csv('path/filename.csv') # read the csv or excel file here
#display(data.sample(5))

df1 = data[['colName1', 'colName2']] 
#display(df1.sample(5))

'''Outlier Detection using Z-Score method'''

# Z-Score Outlier detection
def find_outliers(df):
    flag = 3 # 3rd std daviation
    mean = np.mean(df)
    std = np.std(df)
    for i in df:
        z_score = (i-mean)/std
        if np.abs(z_score)>flag:
            outliers.append(i)
    return outliers  

container = {}
    
for i in cols:
    df = df1[i]
    #print(len(df))
    flag = 3 # 3rd std deviation
    container['lst_%s' % i] = []
    mean = np.mean(df)
    std = np.std(df)
    for j in df:
        z_score = (j-mean)/std
        if np.abs(z_score)>flag:
            container['lst_%s' % i].append(j)

print(container.keys())
for k, v in container.items():
    print(k,v,len(v))
    
'''IQR -  Inter Quartile Range outlier Detection '''
# InterQuartile Range outlier detection
df2 = data[['colName1', 'colName2']]
#display(df2.sample(5))

df2.info()
df2 = pd.DataFrame(df2)
cols = df2.columns.to_list()
#df2.describe()

#quantiles = {}
iqrLimits = {}
for i in cols:
    df = df2[i]
    df = pd.DataFrame(df)
    iqrLimits['lowerIQR-%s' % i] = []
    iqrLimits['upperIQR-%s' % i] = []
    x = df[i].quantile(0.25)
    y = df[i].quantile(0.75)
    iqr = y - x
    lowerIQR = x - 1.5*iqr 
    upperIQR = y + 1.5*iqr
    iqrLimits['lowerIQR-%s' % i].append(lowerIQR)
    iqrLimits['upperIQR-%s' % i].append(upperIQR)
    
arr = [] 

for k,v in iqrLimits.items():
    arr.append(v[0])
#print(len(arr))
var1 = arr[0]
var2 = arr[1]
#print("Shaft_Power_kW: ", len(df2[(df2.Shaft_Power_kW<var1)|(df2.Shaft_Power_kW>var2)].index))
#print("Shaft_Power_kW: \n",df2[(df2.Shaft_Power_kW<var1)|(df2.Shaft_Power_kW>var2)].index)
col1 = df2[(df2.Shaft_Power_kW<var1)|(df2.Shaft_Power_kW>var2)].index
col1= list(col1)
var1 = arr[2]
var2 = arr[3]
#print("SFOC_g_kWh: ",len(df2[(df2.SFOC_g_kWh<var1)|(df2.SFOC_g_kWh>var2)].index))
#print("SFOC_g_kWh: ",df2[(df2.SFOC_g_kWh<var1)|(df2.SFOC_g_kWh>var2)].index)
col2 = df2[(df2.SFOC_g_kWh<var1)|(df2.SFOC_g_kWh>var2)].index
col2 = list(col2)
var1 = arr[4]
var2 = arr[5]
#print('RPM', len(df2[(df2.RPM<var1)|(df2.RPM>var2)].index))
#print('RPM',df2[(df2.RPM<var1)|(df2.RPM>var2)].index)
col3 = df2[(df2.RPM<var1)|(df2.RPM>var2)].index
col3= list(col3)
var1 = arr[6]
var2 = arr[7]
#print('ME total Const t: ', len(df2[(df2.ME_Total_Cons_t<var1)|(df2.ME_Total_Cons_t>var2)].index))
#print('ME total Const t: ',df2[(df2.ME_Total_Cons_t<var1)|(df2.ME_Total_Cons_t>var2)].index)
col4 = df2[(df2.ME_Total_Cons_t<var1)|(df2.ME_Total_Cons_t>var2)].index
col4 = list(col4)
var1 = arr[8]
var2 = arr[9]
#print("STW KN: ",len(df2[(df2.STW_kn<var1)|(df2.STW_kn>var2)].index))
#print("STW KN: ",df2[(df2.STW_kn<var1)|(df2.STW_kn>var2)].index)
col5= df2[(df2.STW_kn<var1)|(df2.STW_kn>var2)].index
col5 = list(col5)
var1 = arr[10]
var2 = arr[11]
#print("SOG KN: ", len(df2[(df2.SOG_kn<var1)|(df2.SOG_kn>var2)].index))
#print("SOG KN: ",df2[(df2.SOG_kn<var1)|(df2.SOG_kn>var2)].index)
col6 = df2[(df2.SOG_kn<var1)|(df2.SOG_kn>var2)].index
col6 = list(col6)
var1 = arr[12]
var2 = arr[13]
#print("Deadweight_t : ",len(df2[(df2.Deadweight_t<var1)|(df2.Deadweight_t>var2)].index))
#print("Deadweight_t : ",df2[(df2.Deadweight_t<var1)|(df2.Deadweight_t>var2)].index)
col7 = df2[(df2.Deadweight_t<var1)|(df2.Deadweight_t>var2)].index
col7 = list(col7)
var1 = arr[14]
var2 = arr[15]
#print("Draft_Aft_m : ", len(df2[(df2.Draft_Aft_m<var1)|(df2.Draft_Aft_m>var2)].index))
#print("Draft_Aft_m : ",df2[(df2.Draft_Aft_m<var1)|(df2.Draft_Aft_m>var2)].index)
col8 =df2[(df2.Draft_Aft_m<var1)|(df2.Draft_Aft_m>var2)].index
col8 = list(col8)
var1 = arr[16]
var2 = arr[17]
#print("MCR : ", len(df2[(df2.MCR<var1)|(df2.MCR>var2)].index))
#print("MCR : ",df2[(df2.MCR<var1)|(df2.MCR>var2)].index)
col9= df2[(df2.MCR<var1)|(df2.MCR>var2)].index
col9 = list(col9)
#df2.index[df2['Shaft_Power_kW'] == 714].values
#print("Shaft_Power_kW : ", len(df2[(df2.Shaft_Power_kW<var1)|(df2.Shaft_Power_kW>var2)].index))
#print(df2['Shaft_Power_kW'][179])
row_nums = col1+ col2+ col3+col4+ col5+col6+col7+col8+col9
print("after concat: ",len(row_nums))
set_row_nums = set(row_nums)
print("after set:",len(set_row_nums))
d = {x:row_nums.count(x) for x in set_row_nums}
print(d)

# displaying the BoxPlot for coliumns to visualize outliers

import plotly.graph_objects as go
import plotly.express as px
x_data = df2.columns 
y0 = df2['']
y1 = df2['']
y2 = df2['']
y3 = df2['']
y4 = df2['']
y5 = df2['']
y6 = df2['']
y7 = df2['']
y8 = df2['']
y_data = [y0, y1, y2, y3, y4, y5, y6, y7, y8]
colors = ['rgba(93, 164, 214, 0.5)', 'rgba(255, 144, 14, 0.5)', 'rgba(44, 160, 101, 0.5)',
          'rgba(255, 65, 54, 0.5)', 'rgba(207, 114, 255, 0.5)', 'rgba(127, 96, 0, 0.5)', 'rgba(242, 129, 129, 0.5)', 'rgba(181, 218, 31, .5)', 'rgba(237, 84, 198 ,0.5)']
fig = go.Figure()
for xd, yd, cls in zip(x_data, y_data, colors):
        fig.add_trace(go.Box(
            y=yd,
            name=xd,
            boxpoints='all',
            jitter=0.5,
            whiskerwidth=0.2,
            fillcolor=cls,
            marker_size=2,
            line_width=1)
        )

fig.update_layout(
    title='MSC shipping 9 cols outliers',
    yaxis=dict(
        autorange=True,
        showgrid=True,
        zeroline=True,
        dtick=5,
        gridcolor='rgb(255, 255, 255)',
        gridwidth=1,
        zerolinecolor='rgb(255, 255, 255)',
        zerolinewidth=2,
    ),
    margin=dict(
        l=40,
        r=30,
        b=80,
        t=100,
    ),
    paper_bgcolor='rgb(243, 243, 243)',
    plot_bgcolor='rgb(243, 243, 243)',
    showlegend=False
)
fig.show()
fig.write_html("boxplot.html")
