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


@st.cache_data(ttl=3600, show_spinner="正在加載資料...")  ## Add the caching decorator
def load_data(path):
    df = pd.read_pickle(path)
    return df



######  前置作業 
###### 讀入 "實際填答名單資料" 外部excel 檔
# df_total = pd.read_excel(r'C:\Users\user\Dropbox\系務\校務研究IR\大三學生學習經驗問卷調查分析\112\112學年度大三學習經驗問卷調查(1-333).xlsx', sheet_name=0)
df_total = pd.read_excel('112學年度大三學習經驗問卷調查(1-333).xlsx', sheet_name=0)

# df_total.shape  ## (333, 56)
# df_total.columns
# '''
# Index(['ID', '開始時間', '完成時間', '電子郵件', '名稱', '語言', '上次修改時間', '請輸入學號',
#        '工讀情況:\n您三年級就學期間是否曾工讀？', '您三年級「上學期」平均每周工讀時數？', '您三年級「上學期」的工讀地點為何？',
#        '您三年級「下學期」平均每周工讀時數？', '您三年級「下學期」的工讀地點為何？',
#        '您工讀的原因為何？(直接拖拉，依原因之優先順序排列，最主要原因放在最上方)', '您認為下列哪些經驗對未來工作會有所幫助？(可複選)',
#        '參加社團', '擔任社團/系學會幹部', '志工服務', '校外實習', '企業參訪', '您是否擔任過社團/系學會幹部？',
#        '課外活動參與情況:\n上述您參與過的活動中，您認為哪些經驗對未來工作會有所幫助？(可複選)',
#        '學習情況與能力培養:\n您在專業課程學習上的投入/認真程度？ (依多數課程情況回答)\n', '請對專業課程提供意見或建議',
#        '您認為下列哪些能力有助於提升就業力？(可複選)', '專業能力', '溝通表達', '團隊合作', '問題解決能力', '自主探索學習',
#        '分析思考', '領導力', '創新能力', '人際互動', '外語能力', '專業證照考試', '校外實習2', '申請(考)研究所',
#        '外語能力鑑定考試', '公職考試', '遊留學', '學生學習輔導方案(學習輔導/自主學習/飛鷹助學)', '生活相關輔導(導師/領頭羊)',
#        '職涯輔導', '外語教學中心學習輔導', '諮商暨健康中心的諮商輔導', '國際化資源', '學校能有效輔導同學就業與生涯發展規劃',
#        '對畢業後的生涯發展有明確方向與規劃', '瞭解系上學長姐畢業後主要的就業領域與方向', '期待畢業學長姊返校與在校同學分享經驗',
#        '了解目前國內外產業發展趨勢及就業市場之形勢', '有沒有老師關心您', '有沒有老師能啟發您, 給您夢想跟動力', '有沒有老師鼓勵您',
#        '有沒有碰到專心認真上課的老師'],
#       dtype='object')
# '''
###### 讀入 "應填答名單資料" 外部 excel 檔
# df_ID = pd.read_excel(r'C:\Users\user\Dropbox\系務\校務研究IR\大三學生學習經驗問卷調查分析\112\大三學生名單_學籍正常.xlsx', sheet_name=0)
df_ID = pd.read_excel('大三學生名單_學籍正常.xlsx', sheet_name=0)
# df_ID.shape  ## (2492, 7)
# df_ID.columns
# '''
# Index(['班級', '學號', '姓名', 'email', '身分', '導師', '導師email'], dtype='object')
# '''

###### 将DataFrame存储为Pickle文件
df_total.to_pickle('df_Junior_original.pkl')
df_ID.to_pickle('df_Junior_ID.pkl')










####### 查詢沒有填問卷之各系名單
###### 讀入 "實際填答名單資料" 外部檔
df_total = load_data('df_Junior_original.pkl')
###### 讀入 "應填答名單資料" 外部檔
df_ID = load_data('df_Junior_ID.pkl')


###### 找出在df_ID中但不在df_total中的'stno'值
not_in_df_total = ~df_ID['學號'].isin(df_total['請輸入學號'])
###### 篩選出未填問卷名單
df_ID_未填問卷 = df_ID[not_in_df_total]
# df_ID_未填問卷.shape  ## (293, 7)
# ##### 輸出成外部 excel 檔
# df_ID_未填問卷.to_excel('未填問卷名單.xlsx',index=False)


####### 設定呈現標題 
html_temp = """
		<div style="background-color:#3872fb;padding:10px;border-radius:10px">
		<h1 style="color:white;text-align:center;"> 112大三學習經驗問卷調查 - 未填問卷名單 </h1>
		</div>
		"""
stc.html(html_temp)



choice = st.selectbox('選擇系級', df_ID_未填問卷['班級'].unique())
#choice = '化科系'
df_ID_未填問卷_department = df_ID_未填問卷[df_ID_未填問卷['班級']==choice]


##### 使用Streamlit展示DataFrame "df_ID_未填問卷_department"，但不显示索引
# st.write(item_name, result_df.to_html(index=False), unsafe_allow_html=True)
st.write(df_ID_未填問卷_department[['班級', '學號', '姓名']].to_html(index=False), unsafe_allow_html=True)
st.markdown("##")  ## 更大的间隔

