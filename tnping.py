import streamlit as st
import requests
from io import BytesIO
from PIL import Image
import random

# 🟢 1. 헬로카봇 캐릭터 데이터
characters = {
    "카봇 에이스": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjQy/MDAxNDgwNTgyNDA0NzQy.RDEYrWtpvQuGX2DdLZkZf_HH-dqNRyRiksOVSG7OAE4g.sDMDm8m7oR0BB706P0DulHHHiYYL-UsJKPPbajOhFBsg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%EC%97%90%EC%9D%B4%EC%8A%A4.jpg?type=w3840",
    "카봇 호크": "https://postfiles.pstatic.net/MjAxNjEyMDFfNTcg/MDAxNDgwNTgyNzIxMTQw.KIWqLUYDjibvL9pmNKYc9rrqFdw4BHzbyKKLuSY1Z8Qg.jPStFz3Ef0LIVLjasPqqXchaiNbPEUBf_FED270zvkwg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%98%B8%ED%81%AC.jpg?type=w3840",
    "카봇 프론": "https://postfiles.pstatic.net/MjAxNjEyMDFfOTYg/MDAxNDgwNTgyNzIxMTU4.96vC8iEu5WNiBObqcH-aGrKqsvam8Qap8ofawZ1se5og.DsbQBRSfE9MgGtPglbJMTbHzQPgSfDGoJvEYzL8A_MUg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%ED%94%84%EB%A1%A0.jpg?type=w3840",
    "카봇 댄디": "https://postfiles.pstatic.net/MjAxNjEyMDFfNCAg/MDAxNDgwNTgyNzIxMTY0.j6wEK9OQaBVIZ-hUqodSe_sG7u9pUntyUteXYDswYNYg.z6QtJ0Wp63VB9mgNj26Uu7qts_iMU109ZGCaLIHDuqMg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%EB%8C%84%EB%94%94.jpg?type=w3840",
}


# 🟢 2. 네이버 이미지 Referer 우회 함수
def fetch_image(url):
    headers = {"Referer": "https://www.naver.com"}
    try:
        response = requests.get(url, headers=headers)
        image = Image.open(BytesIO(response.content))
        return image
    except Exception as e:
        st.error(f"이미지를 불러오는 데 실패했습니다: {e}")
        return None


# 🟢 3. 스트림릿 UI 설정
st.title("🚗 헬로카봇 이상형 월드컵 🚀")

# 🟢 4. 토너먼트 데이터 초기화
if "remaining" not in st.session_state:
    st.session_state.remaining = list(characters.items())  # 캐릭터 리스트
    st.session_state.round = 1  # 현재 라운드 번호

# 현재 남은 캐릭터 수 확인
num_remaining = len(st.session_state.remaining)

# 🟢 5. 게임 진행
if num_remaining == 1:
    # 🏆 최종 우승자 발표
    winner_name, winner_img_url = st.session_state.remaining[0]
    winner_img = fetch_image(winner_img_url)

    st.header(f"🏆 최종 우승: {winner_name}!")
    if winner_img:
        st.image(winner_img, use_column_width=True)

    # 다시하기 버튼
    if st.button("🔄 다시하기"):
        st.session_state.clear()
        st.rerun()  # ✅ 변경된 부분 (experimental_rerun → rerun)

else:
    st.subheader(f"⚔️ {st.session_state.round}라운드 - {num_remaining}강전 ⚔️")

    # 랜덤으로 2개의 캐릭터 선택
    pair = random.sample(st.session_state.remaining, 2)

    col1, col2 = st.columns(2)

    # 🟢 6. 캐릭터 선택 버튼
    with col1:
        img1 = fetch_image(pair[0][1])
        if img1:
            st.image(img1, caption=pair[0][0], use_column_width=True)
        if st.button(f"🛡 {pair[0][0]} 선택"):
            st.session_state.remaining = [p for p in st.session_state.remaining if p[0] != pair[1][0]]
            st.session_state.round += 1
            st.rerun()  # ✅ 변경된 부분 (experimental_rerun → rerun)

    with col2:
        img2 = fetch_image(pair[1][1])
        if img2:
            st.image(img2, caption=pair[1][0], use_column_width=True)
        if st.button(f"⚔️ {pair[1][0]} 선택"):
            st.session_state.remaining = [p for p in st.session_state.remaining if p[0] != pair[0][0]]
            st.session_state.round += 1
            st.rerun()  # ✅ 변경된 부분 (experimental_rerun → rerun)
