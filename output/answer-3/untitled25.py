# -*- coding: utf-8 -*-
"""Untitled25.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gimMZMH_-WA7ZmU35dGvBbfPwzomvsVA
"""

import pandas as pd
team = pd.read_csv("main.csv")
team.head()

disk = team[['Team','Yellow Cards','Red Cards']]
disk

fg=disk.sort_values(['Red Cards', 'Yellow Cards'], ascending=False)
fg

fg.to_csv('main.csv',index=False)