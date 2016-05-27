#!/usr/bin/env python
# -*- coding:utf-8 -*-

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

df_songs_by_artist = pd.read_csv('./data/songs_by_artist.csv', header = None, names = ['date', 'play', 'download', 'like', 'artist_id'])


# In[53]:

len(set(df_songs_by_artist['artist_id']))


# In[54]:

df_songs_by_artist.describe()


# In[55]:

df_songs_by_artist


# **分析某位歌手的播放量**

# In[60]:

a = df_songs_by_artist[['date', 'play', 'download', 'like']][df_songs_by_artist['artist_id'] == '5e2ef5473cbbdb335f6d51dc57845437']
a = a.set_index(['date'])

plt.figure()
a.plot(figsize = (10,5))
ax = a.plot.scatter(x = 'download', y = 'play', color = 'blue', label = 'download-play')
a.plot.scatter(figsize = (10,5), x = 'like', y = 'play', color = 'red', label = 'like-play', ax = ax)


# # 生成训练集&数据集

# In[7]:

df_artists = pd.read_csv('./data/artists.csv', header = None, names = ['date', 'play', 'download', 'like', 'artist_id'])


# In[10]:

df_artist_1 = df_artists[df_artists['artist_id'] == 'e087f8842fe66efa5ccee42ff791e0ca']


# In[ ]:

df_artist_1 = df_artist_1[['']]


# In[22]:

from sklearn import preprocessing


# In[48]:

import csv
reader=csv.reader(open("artist_1.csv","rb"),delimiter=',')
x=list(reader)
result=np.array(x).astype('float')


# In[36]:

X = result[:, 3:5]


# In[76]:

for i in range(0, X.shape[0]):
    for j in range(0, X.shape[1]):
        X[i][j] = int(X[i][j])


# In[78]:

type(X[0][0])


# In[ ]: