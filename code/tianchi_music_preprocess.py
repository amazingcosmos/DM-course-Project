#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
proprocess the data into separate file, divide by day or by artist.
"""

import time
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

# read user action file
df_user_actions = pd.read_csv('./data/mars_tianchi_user_actions.csv', 
                              header = None, 
                              names = ('user_id', 'song_id', 'gmt_create', 'action_type', 'Ds'))
# count user id number
users = list(set(df_user_actions['user_id']))
print("user number: ", len(users))

# read songs file
df_song_info = pd.read_csv('./data/mars_tianchi_songs.csv', 
                           header = None, 
                           names = ('song_id', 'artist_id', 'public_time', 'popular', 'language', 'gender'))

# count the song number and artist number.
artists = {}
for i in range(0, df_song_info.shape[0]):
    artist = df_song_info.iloc[i]['artist_id']
    song = df_song_info.iloc[i]['song_id']
    if artist not in artists:
        artists[artist] = []
    artists[artist].append(song)
print("artist number: ", len(artists))

song_id = list(set(df_song_info['song_id']))
print("song number: ", len(song_id))

# count the days to analyse.
dates =  list(set(df_user_actions['Ds']))
dates.sort()
print("day number: ", len(dates))


# analyse the data by day, save it into a file.
# record the time it cost.
time_start = time.asctime(time.localtime(time.time()))

fp = open('./data/songs_by_day.csv', 'w')
for song in song_id:
    song_list = df_user_actions[df_user_actions.song_id == song]
    content = ''
    for date in dates:
        song_today = song_list[song_list.Ds == date]
        play = len(song_today[song_today.action_type == 1])
        download = len(song_today[song_today.action_type == 2])
        like = len(song_today[song_today.action_type == 3])
        content += "%s,%d,%d,%d,%d\n" % (song,date,play,download,like)
    fp.write(content)
fp.close()
# log the runtime
time_end = time.asctime(time.localtime(time.time()))
time_stamp = str(time.time())
fp = open('./done'+time_stamp+'.txt', 'w')
fp.write(str(time_start)+'\n')
fp.write(str(time_end)+'\n')
fp.close()

# analyse the data by artist.
for artist_id in artists:
    temp = df_songs_by_day[['date', 'play', 'download', 'like']][df_songs_by_day['song_id'] == artists[artist_id][0]]
    date = temp['date']
    temp = temp[['play', 'download', 'like']]
    temp['newdate'] = pd.date_range('20150301', '20150830')
    temp = temp.set_index(['newdate'])
    for song_id in artists[artist_id][1:]:
        temp2 = df_songs_by_day[['play', 'download', 'like']][df_songs_by_day['song_id'] == song_id]
        temp2['newdate'] = pd.date_range('20150301', '20150830')
        temp2 = temp2.set_index(['newdate'])
        temp = temp.add(temp2)
    temp['artist_id'] = artist_id
    temp['date'] = date
    temp.to_csv('./data/songs_by_artist.csv', mode = 'a', encoding='utf-8', header = False)

print 'done!'




