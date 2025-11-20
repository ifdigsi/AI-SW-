import os
from openai import OpenAI
import streamlit as st

# ----------------------------
# ⚡ OpenAI API 키 설정 (테스트용)
# ----------------------------
os.environ["OPENAI_API_KEY"] = "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"

# OpenAI 클라이언트 생성
client = OpenAI()
print("OpenAI SDK import OK")

# ----------------------------
# Streamlit 앱
# ----------------------------
st.title("나만의 레시피 생성기")

# 사용자 입력
ingredients = st.text_input("어떤 재료를 가지고 계십니까?")

# 버튼 클릭 시 레시피 생성
if st.button("레시피 생성하기") and ingredients:
    # GPT 호출
    response = client.chat.completions.create(
        model="gpt-4o-mini",  # 필요시 다른 모델로 변경 가능
        messages=[
            {"role": "user", "content": f"이 재료들로 만들 수 있는 레시피를 알려줘: {ingredients}"}
        ]
    )
    
    # GPT가 생성한 레시피 출력
    recipe = response.choices[0].message.content
    st.markdown(f"**추천 레시피:**\n{recipe}")
