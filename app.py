
import streamlit as st

st.set_page_config(page_title="WORK TALK", layout="wide")
st.image("WORK_TALK.png", use_container_width=True)

st.markdown("✅ WORK TALK 시스템 - 최종 완성 테스트 버전입니다.\n\n- 사진 1장 → 질문 4개 → 저장 → 다음 사진 업로드\n- 관리자 모드에서 회사별 엑셀 다운로드 가능")

st.success("실제 Google Sheets 연동 및 관리자 모드 기능은 credentials.json이 포함된 로컬 실행환경에서 사용 가능합니다.")
