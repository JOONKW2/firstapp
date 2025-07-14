import streamlit as st

# MBTI 추천 게임 데이터
mbti_games = {
    "INFP": {
        "title": "Stardew Valley",
        "genre": "🌾 시뮬레이션 / 힐링",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6d/Stardew_Valley_cover_art.png"
    },
    "ENFP": {
        "title": "The Legend of Zelda: Breath of the Wild",
        "genre": "🗺️ 오픈월드 / 어드벤처",
        "image": "https://upload.wikimedia.org/wikipedia/en/0/0e/The_Legend_of_Zelda_Breath_of_the_Wild.jpg"
    },
    "INTJ": {
        "title": "Sid Meier's Civilization VI",
        "genre": "🧠 전략 시뮬레이션",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6a/Civilization_VI_cover_art.jpg"
    },
    "ENTJ": {
        "title": "StarCraft II",
        "genre": "⚔️ RTS / 전략 전투",
        "image": "https://upload.wikimedia.org/wikipedia/en/8/89/StarCraft_II_-_Box_Art.jpg"
    },
    "ISFP": {
        "title": "Journey",
        "genre": "🎨 감성 어드벤처",
        "image": "https://upload.wikimedia.org/wikipedia/en/b/b2/Journey_Cover.jpg"
    },
    "ISTJ": {
        "title": "Animal Crossing: New Horizons",
        "genre": "🏝️ 생활 시뮬레이션",
        "image": "https://upload.wikimedia.org/wikipedia/en/d/d6/Animal_Crossing_New_Horizons.jpg"
    },
    "ESTP": {
        "title": "Call of Duty: Modern Warfare",
        "genre": "🔫 FPS / 액션",
        "image": "https://upload.wikimedia.org/wikipedia/en/6/6c/Call_of_Duty_Modern_Warfare_cover.jpg"
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

# 추천 결과
game = mbti_games[mbti]
st.subheader(f"✨ {mbti} 유형에게 추천하는 게임은...")
st.markdown(f"### 🎮 {game['title']}")
st.image(game["image"], caption=game["genre"], use_column_width=True)
