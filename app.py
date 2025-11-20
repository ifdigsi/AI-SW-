import os
from openai import OpenAI

os.environ["OPENAI_API_KEY"] = "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"

import streamlit as st
import random

# 앱 제목
st.title("나만의 레시피를 소개합니다")

# 재료 입력 받기
title = st.text_input("어떤 재료를 가지고 계십니까?")

# 재료 출력
if st.button("레시피 생성하기"):
    st.write(title)
