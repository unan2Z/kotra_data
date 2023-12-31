# -*- coding: utf-8 -*-
"""외국인투자통계분석_20230712 12:35

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1NXCtVdxR87ZkI94xYShqfjMJPxJ8SaVN
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# 구글 드라이브 연동
from google.colab import drive

# 파일 경로 지정
file_path = '/외국인투자통계_국가별_산업별_투자신고도착금액(2013-2023)_비율추가.xlsx'
file_path2 = '/외국인투자통계_국가명_산업부.xlsx'
file_path3 = '/산업분류_대분류_수정.xlsx'
file_path4 = '/산업분류_대_중_결합.xlsx'

# xlsx 파일 불러오기
# df_iv = 산업부 통계 , #df_cn = 국가명, #df_in = 산업별 대분류(이름), # df_in_cn = df_in + df_cn
df_iv = pd.read_excel(file_path)
df_cn = pd.read_excel(file_path2)
df_in = pd.read_excel(file_path3)
df_in_cm = pd.read_excel(file_path4)

df_cn

df_iv

df_in

# 키워드를 포함하는 행 추출
# 이를 통해 전체, 제조업, 서비스업 등의 통계를 추출하면 됨
#isins(['전체'])에서 '전체' 부분에 원하는 산업군 입력
filtered_rows2 = df_iv[df_iv['KSIC분류'].isin(['전체'])]

filtered_rows2

# 드라이브 마운트
drive.mount('/content/drive')

# 데이터프레임을 엑셀로 저장
file_path2 = '/content/drive/MyDrive/국가별_산업별(대)_투자신고도착금액2.xlsx'  # 저장할 엑셀 파일 경로
filtered_rows2.to_excel(file_path2, index=False)  # index=False로 설정하여 인덱스를 엑셀 파일에 포함하지 않음