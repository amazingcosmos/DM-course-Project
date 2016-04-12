#!/usr/bin/env python
# -*- coding:utf-8 -*-

import pandas as pd
import time

df_user_actions = pd.read_csv('./data/mars_tianchi_user_actions.csv', header = None, names = ('user_id', 'song_id', 'gmt_create', 'action_type', 'Ds'))
df_songs = pd.read_csv('./data/mars_tianchi_songs.csv', header = None, names = ('song_id', 'artist_id', 'public_time', 'popular', 'language', 'gender'))

# artists = df_songs['artist_id']
# artists = set(artists)
# artists = {}
# for i in range(0, df_songs.shape[0]):
#     artist = df_songs.iloc[i]['artist_id']
#     song = df_songs.iloc[i]['song_id']
#     if artist not in artists:
#         artists[artist] = []
#     artists[artist].append(song)

song_id = list(set(df_songs['song_id']))
# songs = {}
# for i in song_id:
#     songs[i] = {}

# 统计每首歌的每日播放量
dates =  list(set(df_user_actions['Ds']))
dates.sort()

time_start = time.asctime(time.localtime(time.time()))
fp = open('./songs.txt', 'w')
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
    print song
#         count = count + play + like + download
fp.write('done!\n')
fp.close()
time_end = time.asctime(time.localtime(time.time()))
time_stamp = str(time.time())
fp = open('./done'+time_stamp+'.txt', 'w')
fp.write(str(time_start)+'\n')
fp.write(str(time_end)+'\n')
fp.close()

print 'done!'

