streamlit>=3.13
openai>=2.8.1
import os
from openai import OpenAI
import streamlit as st

# ⚡ OpenAI API 키 설정
os.environ["OPENAI_API_KEY"] = "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"

# OpenAI 클라이언트 생성
client = OpenAI()
print("OpenAI SDK import OK")

# ----------------------------
# Streamlit 앱
# ----------------------------
st.title("나만의 레시피를 소개합니다")

# 사용자로부터 재료 입력 받기
ingredients = st.text_input("어떤 재료를 가지고 계십니까?")

# 버튼 클릭 시 레시피 생성
if st.button("레시피 생성하기") and ingredients:
    # OpenAI GPT 호출 예제 (간단)
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 필요에 따라 모델 변경
        messages=[
            {"role": "user", "content": f"이 재료들로 만들 수 있는 레시피를 알려줘: {ingredients}"}
        ]
    )
    
    # GPT가 생성한 레시피 출력
    recipe = response.choices[0].message.content
    st.write(recipe)

