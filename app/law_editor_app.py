import streamlit as st
from processing.law_processor import process_laws, get_law_list_from_api

st.title("📘 검색어 포함 법률 목록")
st.caption("📄 본문 중에 검색어를 포함하는 법률의 목록을 반환합니다.")

search_word = st.text_input("🔍 찾을 단어", placeholder="예: 지방법원")

if st.button("🚀 시작하기"):
    if not search_word:
        st.warning("찾을 단어를 입력해주세요.")
    else:
        with st.spinner("법령 검색 중..."):
            laws = get_law_list_from_api(search_word)
            st.success(f"✅ 총 {len(laws)}개의 법령을 찾았습니다.")
            for law in laws:
                st.markdown(f"- [{law['법령명']}]({law['URL']})", unsafe_allow_html=True)
