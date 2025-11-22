import os
import streamlit as st
from openai import OpenAI

# 🔐 API KEY
os.environ["OPENAI_API_KEY"] = st.secrets['API_KEY']
client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"),)

st.title("🎓 맞춤형 대학생활 정보 추천 플랫폼 (Prototype)")
st.write("원하는 정보를 입력하면 AI가 최신 정보 요약 및 맞춤 추천을 제공합니다.")

user_query = st.text_input("찾고 싶은 대학생활 정보 주제를 입력하세요 (예: 공모전, 장학금, 교내 행사 등)")

if st.button("정보 추천 생성"):

    # --- 1) 텍스트 생성 ---
    chat_response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content":
                """
                당신은 대학생 삶에 필요한 정보를 추천해주는 전문가입니다.
                사용자가 원하는 주제를 아래 요소 중심으로 정리하세요:

                - 최신 정보 요약
                - 일정(기간, 마감일 등)
                - 참여/신청 방법
                - 준비 팁
                - 맞춤형 추천
                """
            },
            {"role": "user", "content": user_query}
        ]
    )

    result_text = chat_response.choices[0].message.content

    st.subheader("📌 AI 정보 요약 및 추천")
    st.write(result_text)
