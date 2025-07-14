import streamlit as st

mbti_games = {
    "INFP": {
        "title": "Stardew Valley",
        "genre": "🌾 시뮬레이션 / 힐링",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/413150/header.jpg"
    },
    "ENFP": {
        "title": "The Legend of Zelda: Breath of the Wild",
        "genre": "🗺️ 오픈월드 / 어드벤처",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1174180/header.jpg"
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
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/681290/header.jpg"
    },
    "INFJ": {
        "title": "Firewatch",
        "genre": "🔥 어드벤처 / 스토리",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/383870/header.jpg"
    },
    "INTP": {
        "title": "Portal 2",
        "genre": "🧩 퍼즐 / FPS",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/620/header.jpg"
    },
    "ISFJ": {
        "title": "Spiritfarer",
        "genre": "🌟 힐링 / 시뮬레이션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/972660/header.jpg"
    },
    "ISTP": {
        "title": "DOOM Eternal",
        "genre": "🔫 FPS / 액션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/782330/header.jpg"
    },
    "ESFJ": {
        "title": "The Sims 4",
        "genre": "🏠 시뮬레이션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/1222670/header.jpg"
    },
    "ENFJ": {
        "title": "Life is Strange",
        "genre": "🎭 어드벤처 / 스토리",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/319630/header.jpg"
    },
    "ENTP": {
        "title": "Fortnite",
        "genre": "⚔️ 배틀로얄 / 액션",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/218620/header.jpg"
    },
    "ESTJ": {
        "title": "Rainbow Six Siege",
        "genre": "🎯 FPS / 전략",
        "image": "https://cdn.cloudflare.steamstatic.com/steam/apps/359550/header.jpg"
    }
}

st.set_page_config(page_title="🎮 MBTI 게임 추천", page_icon="🧠")
st.title("🎮 MBTI별 어울리는 게임 추천")
st.markdown("당신의 MBTI 성격에 어울리는 게임을 추천해드릴게요!")

mbti = st.selectbox("🧬 MBTI를 선택하세요:", list(mbti_games.keys()))

game = mbti_games[mbti]
st.subheader(f"✨ {mbti} 유형에게 추천하는 게임은...")
st.markdown(f"### 🎮 {game['title']}")
st.image(game["image"], caption=game["genre"], use_container_width=True)
