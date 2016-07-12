#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os
import math
import pandas as pd
import numpy as np

def score_fuc(date_from, date_to, file_origin, file_predict):
    if not isinstance(date_from, int):
        date_from = int(date_from)
    if not isinstance(date_from, int):
        date_to = int(date_to)
    df_origin = pd.read_csv(file_origin, 
                             header = None, 
                             names = ['date', 'play', 'download', 'like', 'artist_id'])
    df_origin['date'] = df_origin['date'].apply(lambda x:int(x.replace('-', '')))
    df_predict = pd.read_csv(file_predict, 
                             header = None, 
                             names = ['artist_id', 'play', 'date'])
    artist_list = list(set(df_predict['artist_id']))
    F = 0
    for artist in artist_list:
        variance = 0
        weight = 0
        data_origin = df_origin[(df_origin.artist_id == artist) ]
        data_predict = df_predict[df_predict.artist_id == artist]
        data_origin = data_origin[(data_origin.date >= date_from)
                                & (data_origin.date <= date_to)]
        S = []
        T = []
        for i in range(len(data_predict)):
            S.append(data_predict.iloc[i]['play'])
            T.append(int(data_origin[data_origin.date == data_predict.iloc[i]['date']]['play']))
        for s,t in zip(S, T):
            weight += t
            variance += (((s-t)/t) * ((s-t)/t))
        weight = math.sqrt(weight)
        variance = math.sqrt(variance/len(data_predict))
        F += (1 - variance) * weight
    return F  

def main():
    file_origin = './songs_by_artist.csv'
    while not os.path.exists(file_origin):
        file_origin = input("enter the origin csv file path(e.g. './songs_by_artist.csv'): ")
    file_predict = input("enter the predict csv file path(e.g. './predict.csv'): ")
    while not os.path.exists(file_predict):
        file_predict = input("enter the origin csv file path(e.g. './predict.csv'): ")
    date_from = input("the begin of predict date(e.g. 20150801):")
    while not len(str(date_from)) == 8:
        date_from = input("Wrong date, please enter the begin of predict date(e.g. 20150801):")
    date_to = input("the end of predict date(e.g. 20150830):")
    while not len(str(date_to)) == 8:
        date_to = input("Wrong date, please enter the end of predict date(e.g. 20150830):")

    F = score_fuc(date_from, date_to, file_origin, file_predict)
    print "F score is : ", F

if __name__ == '__main__':
    main()
