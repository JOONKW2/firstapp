import streamlit as st

# MBTI별 게임 추천 데이터 (안정적 이미지 URL)
mbti_games = {
    "INFP": {
        "title": "Stardew Valley",
        "genre": "🌾 시뮬레이션 / 힐링",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg"
    },
    "ENFP": {
        "title": "The Legend of Zelda: Breath of the Wild",
        "genre": "🗺️ 오픈월드 / 어드벤처",
        "image": "https://assets1.ignimgs.com/2017/02/23/zelda-breath-of-the-wild-button-fin-1487898804511_160w.jpg"
    },
    "INTJ": {
        "title": "Civilization VI",
        "genre": "🧠 전략 시뮬레이션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/289070/header.jpg"
    },
    "ENTJ": {
        "title": "StarCraft II",
        "genre": "⚔️ RTS / 전략 전투",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/17890/header.jpg"
    },
    "ISFP": {
        "title": "Journey",
        "genre": "🎨 감성 어드벤처",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/638230/header.jpg"
    },
    "ISTJ": {
        "title": "Animal Crossing: New Horizons",
        "genre": "🏝️ 생활 시뮬레이션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1705800/header.jpg"
    },
    "ESTP": {
        "title": "Call of Duty: Modern Warfare",
        "genre": "🔫 FPS / 액션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1938090/header.jpg"
    },
    "ESFP": {
        "title": "Just Dance",
        "genre": "💃 리듬 / 파티",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/83/Just_Dance_2020_cover_art.jpg"
    }
}

# 페이지 설정
st.set_page_config(page_title="🎮 MBTI 게임 추천", page_icon="🧠")
st.title("🎮 MBTI별 어울리는 게임 추천")
st.markdown("당신의 MBTI 성격에 어울리는 게임을 추천해드릴게요!")

# MBTI 선택
mbti = st.selectbox("🧬 MBTI를 선택하세요:", list(mbti_games.keys()))

# 추천 게임 정보 출력
game = mbti_games[mbti]
st.subheader(f"✨ {mbti} 유형에게 추천하는 게임은...")
st.markdown(f"### 🎮 {game['title']}")
st.image(game["image"], caption=game["genre"], use_container_width=True)
