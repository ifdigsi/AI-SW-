import os
import streamlit as st
import openai

# 🔐 API KEY
openai.api_key = "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"

# 앱 제목
st.title("🎓 맞춤형 대학생활 정보 추천 플랫폼 (Prototype)")
st.write("원하는 정보를 입력하면 AI가 요약, 추천, 일정, 신청 방법 등을 자동으로 정리해드립니다.")

# 사용자 입력
user_query = st.text_input("찾고 싶은 대학생활 정보 주제를 입력하세요 (예: 공모전, 장학금, 교내 행사, 진로, 자격증 등)")
generate_image = st.checkbox("AI 이미지(포스터)도 함께 생성할까요?")

# 버튼 클릭
if st.button("정보 추천 및 요약 생성"):

    # --- 1) AI 정보 요약 + 추천 ---
    chat_response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {
                "role": "system",
                "content":
                """
                당신은 대학생들에게 필요한 정보를 요약하고 추천해주는 AI 어시스턴트입니다.
                사용자가 입력한 주제에 대해:

                - 최신 흐름에 맞는 정보 요약
                - 일정 안내(예정일, 모집 기간)
                - 신청 또는 참여 방법
                - 준비 팁
                - 맞춤 추천

                위 내용을 명확하게 정리하세요.
                """
            },
            {"role": "user", "content": user_query}
        ]
    )

    result_text = chat_response["choices"][0]["message"]["content"]

    st.subheader("📌 AI 추천 & 정보 요약")
    st.write(result_text)

    # --- 2) AI 포스터 생성 ---
    if generate_image:
        st.subheader("🖼️ AI 생성 포스터")

        image_prompt = f"{user_query} 관련 대학생 홍보용 포스터, 심플한 디자인, 깔끔한 구성"

        image_response = openai.Image.create(
            prompt=image_prompt,
            n=1,
            size="1024x1024"
        )

        image_url = image_response["data"][0]["url"]
        st.image(image_url, caption="AI 생성 포스터")
