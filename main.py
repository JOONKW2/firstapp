import streamlit as st
st.title('나의 첫 번째 웹앱(by권준성)')
st.write('이게 된다고?!!!')
import streamlit as st

# MBTI별 직업 추천 데이터
mbti_jobs = {
    "INTJ": ["전략 컨설턴트", "데이터 과학자", "연구 개발자"],
    "INTP": ["이론 물리학자", "프로그래머", "기술 분석가"],
    "ENTJ": ["CEO", "프로젝트 매니저", "기업 전략가"],
    "ENTP": ["창업가", "기획자", "마케팅 전략가"],
    "INFJ": ["상담심리사", "작가", "NGO 활동가"],
    "INFP": ["예술가", "카피라이터", "사회복지사"],
    "ENFJ": ["교사", "HR 매니저", "홍보 담당자"],
    "ENFP": ["방송 PD", "크리에이터", "브랜드 매니저"],
    "ISTJ": ["회계사", "행정 공무원", "품질 관리자"],
    "ISFJ": ["간호사", "초등 교사", "도서관 사서"],
    "ESTJ": ["군 간부", "경영 관리자", "은행원"],
    "ESFJ": ["서비스 매니저", "사회복지사", "고객 상담원"],
    "ISTP": ["정비사", "파일럿", "보안 전문가"],
    "ISFP": ["패션 디자이너", "조경사", "사진작가"],
    "ESTP": ["영업사원", "소방관", "응급 구조사"],
    "ESFP": ["배우", "이벤트 플래너", "쇼호스트"]
}

st.title("💼 MBTI 기반 직업 추천기")

# 사용자 입력 받기
selected_mbti = st.selectbox("당신의 MBTI를 선택하세요:", list(mbti_jobs.keys()))

# 결과 출력
if selected_mbti:
    st.subheader(f"✨ {selected_mbti} 유형에게 추천되는 직업:")
    for job in mbti_jobs[selected_mbti]:
        st.write(f"- {job}")
