import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


st.header('TASK - 5')
st.subheader('Brazil Forest')

df = pd.read_csv("E:\pythonProject\SANTHOSH.csv", encoding = "ISO-8859-1",
                index_col = ['date'],
                parse_dates = ['date'])
months = df.month.unique()
months_num = np.arange(1,13)
months_transform = {mon:mon_num for mon, mon_num in zip(months, months_num)}
df['month_num']= df['month'].map(months_transform)
df['new_date'] = pd.to_datetime(df.year.astype('str') + "-" + df.month_num.astype('str'))
#df.set_index('new_date', inplace = True)
df.sort_index(inplace=True)
df_grouped = df.groupby(df.index).sum()[['number']]
df




df.set_index('new_date', inplace = True)
df.sort_index(inplace=True)

df.groupby(df.index).sum()[['number']].plot(figsize=(15,6))
plt.style.use('ggplot')
#plt.show()
#st.pyplot(df.head)




fig, ax = plt.subplots(figsize=(15,8))
sns.barplot(data= df.sort_values(by='number', ascending=False), x = 'number', y= 'state', ci=None, ax=ax)
ax.set_xticks(ticks=[])
ax.bar_label(ax.containers[0])
plt.title('Fires per state from 1998 to 2017', fontdict={'fontsize':20})
plt.ylabel('')
plt.style.use('ggplot')
#plt.show()
st.pyplot(fig)







