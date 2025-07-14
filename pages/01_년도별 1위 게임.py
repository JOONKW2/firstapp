import streamlit as st
import plotly.graph_objects as go

# 연도, 게임, 판매량 데이터
years = list(range(2000, 2024))
games = [
    "The Sims", "GTA III", "GTA: Vice City", "Pokémon R/S", "GTA: San Andreas", "Nintendogs",
    "New Super Mario Bros.", "Wii Sports", "Mario Kart Wii", "Wii Sports Resort",
    "CoD: Black Ops", "CoD: MW3", "CoD: Black Ops II", "GTA V", "Pokémon OR/AS",
    "CoD: Black Ops III", "Pokémon Sun/Moon", "PUBG", "Red Dead Redemption 2", 
    "CoD: MW (2019)", "Animal Crossing: NH", "Pokémon BD/SP", "Pokémon S/V", "Hogwarts Legacy"
]
sales = [
    11, 14.5, 17.5, 16.2, 27.5, 24, 30.8, 82.9, 37.4, 33.1,
    30.7, 30.7, 29.6, 185, 14.6, 26.7, 25.8, 75, 61,
    30, 43.4, 14.8, 24.9, 22
]

# 페이지 설정
st.set_page_config(page_title="🎮 연도별 베스트셀링 게임", page_icon="🎮")
st.title("📅 2000~2023 연도별 베스트셀링 게임")
st.markdown("💾 **전 세계 실제 판매량 기준**으로 연도별 가장 많이 팔린 게임을 시각화했습니다.")

# 그래프 생성
fig = go.Figure()

fig.add_trace(go.Scatter(
    x=years,
    y=sales,
    mode='lines+markers+text',
    text=games,
    textposition='top center',
    line=dict(color='royalblue', width=3),
    marker=dict(size=8)
))

fig.update_layout(
    title="🎯 연도별 베스트셀링 게임 (2000~2023)",
    xaxis_title="연도",
    yaxis_title="판매량 (백만 장)",
    height=600
)

# 출력
st.plotly_chart(fig)
