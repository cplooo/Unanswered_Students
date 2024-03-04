# -*- coding: utf-8 -*-
"""
查詢沒有填問卷之名單
"""

import pandas as pd
import os
import matplotlib.pyplot as plt
import matplotlib
import numpy as np
import re
import seaborn as sns
import streamlit as st 
import streamlit.components.v1 as stc 


####### 查詢沒有填問卷之各系名單
###### 讀入 "實際填答名單資料" 外部excel 檔
df_total = pd.read_excel(r'C:\Users\user\Dropbox\系務\校務研究IR\大一新生學習適應調查分析\112\final\df_freshman_original.xlsx', sheet_name=0)
# df_total.shape  ## (1674, 186)
# df_total.columns
# '''
# Index(['帳號', '1性別', '2身分別', '3經濟不利背景（可複選）', '4文化不利背景（可複選）', '5原畢業學校之類型',
#        '6原畢業學校所在地區', '7大學「學費」主要來源（可複選）', '8學習及生活費（書籍、住宿、交通、伙食等開銷）主要來源（可複選）',
#        '9我的入學管道',
#        ...
#        '35其他建議事項（如有其他建議學校改善的事項，敬請提出）', '完成時間', '科目名稱', '開課班級', '系級', 'stno',
#        'name', '密碼', '學系', '學院'],
#       dtype='object', length=186)
# '''
###### 讀入 "應填答名單資料" 外部 excel 檔
df_ID = pd.read_excel(r'C:\Users\user\Dropbox\系務\校務研究IR\大一新生學習適應調查分析\112\final\df_ID.xlsx', sheet_name=0)
# df_ID.shape  ## (2002, 7)
# df_ID.columns
# '''
# Index(['科目名稱', '開課班級', '系級', 'stno', 'name', '帳號', '密碼'], dtype='object')
# '''

###### 找出在df_ID中但不在df_total中的'stno'值
not_in_df_total = ~df_ID['stno'].isin(df_total['stno'])
###### 篩選出未填問卷名單
df_ID_未填問卷 = df_ID[not_in_df_total]
df_ID_未填問卷.shape  ## (293, 7)
##### 輸出成外部 excel 檔
df_ID_未填問卷.to_excel(r'C:\Users\user\Dropbox\系務\校務研究IR\大一新生學習適應調查分析\112\final\未填問卷名單.xlsx',index=False)


