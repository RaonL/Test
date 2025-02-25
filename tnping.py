import streamlit as st
import random
from PIL import Image
import requests
from io import BytesIO

# 페이지 설정
st.set_page_config(page_title="헬로카봇 이상형월드컵", page_icon="🤖", layout="centered")

# 세션 상태 초기화
if 'stage' not in st.session_state:
    st.session_state.stage = "start"
if 'candidates' not in st.session_state:
    # 카봇 캐릭터 목록과 이미지 URL
    st.session_state.candidates = [
        {"name": "카봇 에이스",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjQy/MDAxNDgwNTgyNDA0NzQy.RDEYrWtpvQuGX2DdLZkZf_HH-dqNRyRiksOVSG7OAE4g.sDMDm8m7oR0BB706P0DulHHHiYYL-UsJKPPbajOhFBsg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%EC%97%90%EC%9D%B4%EC%8A%A4.jpg?type=w3840"},
        {"name": "카봇 호크",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfNTcg/MDAxNDgwNTgyNzIxMTQw.KIWqLUYDjibvL9pmNKYc9rrqFdw4BHzbyKKLuSY1Z8Qg.jPStFz3Ef0LIVLjasPqqXchaiNbPEUBf_FED270zvkwg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%98%B8%ED%81%AC.jpg?type=w3840"},
        {"name": "카봇 프론",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfOTYg/MDAxNDgwNTgyNzIxMTU4.96vC8iEu5WNiBObqcH-aGrKqsvam8Qap8ofawZ1se5og.DsbQBRSfE9MgGtPglbJMTbHzQPgSfDGoJvEYzL8A_MUg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%ED%94%84%EB%A1%A0.jpg?type=w3840"},
        {"name": "카봇 댄디",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfNCAg/MDAxNDgwNTgyNzIxMTY0.j6wEK9OQaBVIZ-hUqodSe_sG7u9pUntyUteXYDswYNYg.z6QtJ0Wp63VB9mgNj26Uu7qts_iMU109ZGCaLIHDuqMg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%EB%8C%84%EB%94%94.jpg?type=w3840"},
        {"name": "카봇 스카이",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfODQg/MDAxNDgwNTgyNzIxMTUx.o5Spgb1c5phhDks-bOl791qkMUFnh9y_hIIzaS2-9I4g.sgB9q-VdRg5Herj76KkaB5gaoHKNr731qQ94RUL8EX0g.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%EC%8A%A4%EC%B9%B4%EC%9D%B4.jpg?type=w3840"},
        {"name": "카봇 스톰",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTY5/MDAxNDgwNTgyNzIxMTU2.zjJ9pezbJtKfqNTbw5ee4XyMudN43e3w5EM3FAgg-Log.CJTWbBgrF7aA2z2Hm0ytsXqRRVOU1dWtk5Cp92rvVYEg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87%EC%8A%A4%ED%86%B0.jpg?type=w3840"},
        {"name": "카봇 펜타스톰",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTE1/MDAxNDgwNTgyNzIxMTQ3.X9Yevn46jj5f5YyfF9_xC8SFw0tmTyEKyIjg1nva4yMg.7td1QGgnhLXo8zywsXkyZ71wsouAtjOj3YUuNFzg06Qg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%8E%9C%ED%83%80%EC%8A%A4%ED%86%B0.jpg?type=w3840"},
        {"name": "카봇 트루",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMzYg/MDAxNDgwNTgyNzIxMzcx.xyYnOfUYnqMDOqxOGG-umC0g-hPZNJFGV63g6oAESAYg.G6vBZXu6Q3dTwkRsQYHXftZ8etWJ9w9eQLub8LzAd2Ig.PNG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%8A%B8%EB%A3%A8.png?type=w3840"},
        {"name": "카봇 아티",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTc5/MDAxNDgwNTgyNzIxMzQ3.VlLzLZwN50z8Pqz_bjQ7LGC_W6-UhvqS1nFQIRezY0Qg.KtPIHq3x8VuA--p6GMcqB-84z91VPM644OB3e7ZBKF0g.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EC%95%84%ED%8B%B0.jpg?type=w3840"},
        {"name": "카봇 본",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTE5/MDAxNDgwNTgyNzIxMzY0.fI97jpXoOEzvDlQ9bwfhPLPARm30AXj_UGDKK1y5ThEg.f6J4in-yDPm3hGzEcix3Ubf6j3yWZLGI_ZWUsiHE-Nsg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EB%B3%B8.jpg?type=w3840"},
        {"name": "카봇 마이스터",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTYx/MDAxNDgwNTgyNzIxMzU5.mb7LE6DyReJxRR1OAjFpKYNSPJXMFFa3_YqXALvvjecg.aD-NG9IMWwb8pynrhOCX4w5VIRZzYWUPdGNgqut2DIAg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EB%A7%88%EC%9D%B4%EC%8A%A4%ED%84%B0.jpg?type=w3840"},
        {"name": "카봇 나이트",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjg3/MDAxNDgwNTgyNzIxNDAx.adqX-p2K8ll7AU8tLtmqpT_cxT-VQ5VTKiaHz7zQMtYg.ZMIqVDK4zva2nmwzof9PdOVn31M2W3Sw--O0gBEe-c4g.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EB%82%98%EC%9D%B4%ED%8A%B8.jpg?type=w3840"},
        {"name": "카봇 루크",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjEx/MDAxNDgwNTgyNzIxNDAz.-CLx5xsoeDuM9oR0ABhNO3CXJRJWsP35nA5qbgOk4owg.KDsjkxtxfra0LI0H3rWGHDNXua3Ljl_UmczXcA68k3Ig.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EB%A3%A8%ED%81%AC.jpg?type=w3840"},
        {"name": "카봇 폰",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTQw/MDAxNDgwNTgyNzIxNTEz.aNJrelc3FAi7bSbTBbbcrUonXPj1-fOjUDZx_UmuvREg.dKRd8R3uPVMpCKfskxlJ6iQirFM8YZA9C0IJqRfWe08g.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%8F%B0.jpg?type=w3840"},
        {"name": "카봇 세이버",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjAw/MDAxNDgwNTgyNzIxNTM0.aPm0RNoVJf2YcejSW0QQ8nA0LbuxpIOxm2TBuUirQY4g.1LhnhQVEZMCQeqYLP3ecqkJIe4gEZpEW4J2cUCLKTDgg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EC%84%B8%EC%9D%B4%EB%B2%84.jpg?type=w3840"},
        {"name": "카봇 로드 세이버",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjAz/MDAxNDgwNTgyNzIxNTg5.VWAJwE_KovCGKqC8T_3t_bouQJHO8FzSQbllecDsAVEg.mHOFeNP1B4OO67PUKpSPcRYF29oqGJWsxkD4k9Efrukg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EB%A1%9C%EB%93%9C_%EC%84%B8%EC%9D%B4%EB%B2%84.jpg?type=w3840"},
        {"name": "카봇 마이티 가드",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTcw/MDAxNDgwNTgyNzIxNTg5.iClonGWTCv85lgHgdtrOarD52ihiOoWYRE4546x8uoYg.Cz_UePvSPlsQOeMD3_Pd4x8-v5gf4sO8dlUlyuJ7Lt0g.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EB%A7%88%EC%9D%B4%ED%8B%B0_%EA%B0%80%EB%93%9C.jpg?type=w3840"},
        {"name": "카봇 K-캅스",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfNzkg/MDAxNDgwNTgyNzIxNTY2.2w9To1VyAAfJKuPpD1uWSHn44rhNG8wUNHOFSLEwNoAg.40bIcVkkGWYyBOdkgTN8TxODqff8PgAYKGPPC_ouhjEg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_K-%EC%BA%85%EC%8A%A4.jpg?type=w3840"},
        {"name": "카봇 우가바",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTcx/MDAxNDgwNTgyNzIxNjE2.ruKQlqX7CUyqdoiNisVVRlNsNwJNhyE5A4GT7A_Khlcg.bl916w_G0i3C16gYJhrwS8u_dVDbJp0WXO7CeKoSkAcg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EC%9A%B0%EA%B0%80%EB%B0%94.jpg?type=w3840"},
        {"name": "카봇 골드렉스",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfODEg/MDAxNDgwNTgyNzIxNjY5.cODJmrON5JrWaURX5alTAktixRlO02L4O1Ly9z46aVYg.U7OX6FRDS98tODSfEkSHq1juaNb9oqOKHVkMPyaroqQg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EA%B3%A8%EB%93%9C%EB%A0%89%EC%8A%A4.jpg?type=w3840"},
        {"name": "카봇 제트렌",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMTc5/MDAxNDgwNTgyNzIxNjk3.nJpTMpSZvhVubgHIEvm8tUA5yIosh5cCNBqyrRk7Mw8g.u92ppkDspC0fiYUmZ57w0HjDX1aXFmAs14_8fufG-Msg.PNG.babyhoney007/%EC%B9%B4%EB%B4%87_%EC%A0%9C%ED%8A%B8%EB%9E%9C.png?type=w3840"},
        {"name": "카봇 킹가이즈",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMjIg/MDAxNDgwNTgyNzIxNzYz.RgA2-g8OCDwPxi4HHovlcr9d9GHpweRrK733RgkSN8cg.LLGlJfWobajVbZvSo0HdN9HfVHWzaiVEusLOFE3JB3Qg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%82%B9%EA%B0%80%EC%9D%B4%EC%A6%88.jpg?type=w3840"},
        {"name": "카봇 패트론",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfOTUg/MDAxNDgwNTgyNzIxNzY4.71j-if1e2noW5Y5jM4rR9FEPjPlUc2ZFRNsTdxCPzRgg.RKlglV9IDPZ8jAGQmkto7d6Gw8Ju1oodO08OjOJxWbUg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%ED%8C%A8%ED%8A%B8%EB%A1%A0.jpg?type=w3840"},
        {"name": "카봇 스키드",
         "img": "https://postfiles.pstatic.net/MjAxNjEyMDFfMzIg/MDAxNDgwNTgyNzIxNzgy.UoIEW2YYiD4GOzfdY2XOnkdpbnYeyoeqJCZ6hZjTDwog.UrE3UYw2pYtf1v7vSWdnO4f8d98bXVl_edPQc29OxScg.JPEG.babyhoney007/%EC%B9%B4%EB%B4%87_%EC%8A%A4%ED%82%A4%EB%93%9C.jpg?type=w3840"},
        {"name": "카봇 다이어",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMTgy/MDAxNTAzNjk4NDM2NDU5.3opynqeqT3RFEWW3OS90ayLnCIv_keE7Xw0sa_Jmzc8g.rnTm5Z7zAMsMxnM0aO_wfdCbu44pMJGB1EJxaOKoe2Ug.JPEG.babyhoney007/%EB%8B%A4%EC%9D%B4%EC%96%B4.JPG?type=w3840"},
        {"name": "카봇 슈퍼 패트론",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMTc0/MDAxNTAzNjk4NDYwNzEw.WQ2IYE2uDjia8rzT_1zCVbprRjJUwa-25NcyAUGCiyog.59cPi4x_YA_Yy7fn4DZQAlUPRxyGFTSt3vq4o0SR6KUg.JPEG.babyhoney007/%EC%8A%88%ED%8D%BC%ED%8C%A8%ED%8A%B8%EB%A1%A0s.JPG?type=w3840"},
        {"name": "카봇 프라우드제트",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMTMy/MDAxNTAzNjk4NDg2NTg3._YuuGU0Cfssqe_fDDL3Z_EiKvHaU4HUYocbAv1ZrfVIg.IXtZEzFXPRuOW08sV6VyVHHaTYmjHL4P4winNPeEzo4g.JPEG.babyhoney007/%ED%94%84%EB%9D%BC%EC%9A%B0%EB%93%9C%EC%A0%9C%ED%8A%B8.JPG?type=w3840"},
        {"name": "카봇 스타블래스터",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMTA5/MDAxNTAzNjk4NTEyMjA1.LgtfR8ajt44O4Qx3g564xSGU3_UsXC70G-l9uPAlq58g.sd-wD59u5IAUUR5T-nv1p6-8RLYJDl_3T-CyCV4eA9Ig.JPEG.babyhoney007/%EC%8A%A4%ED%83%80%EB%B8%94%EB%9E%98%EC%8A%A4%ED%84%B0.JPG?type=w3840"},
        {"name": "카봇 빌디언",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMzUg/MDAxNTAzNjk4NTM1MDIy.ZYeaZe9foH5mFrF-IhaIgPOfeq8F1AEuMiIA5Wcy4Wkg.eABmoZhFglq0xK4oa3WsaCm7uasH87uqj0Q4vP7dVvgg.JPEG.babyhoney007/%EB%8B%AC%EB%94%94%EC%96%B8.JPG?type=w3840"},
        {"name": "카봇 크랜",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMjU2/MDAxNTAzNzAyMDU5MDE2.OErYVrBANQpqOjBBVP8oH8c5VAdUGvwlrEMLvLMXKsMg.isiPWhS-Zyaz6j2Y5k5OLoXvUu-310UTZQH016UE-9gg.JPEG.babyhoney007/%ED%81%AC%EB%9E%9C.JPG?type=w3840"},
        {"name": "카봇 듀크",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfODkg/MDAxNTAzNzAyMDk0MjQ4.exGECSo9dCST621MFsdSbednjQfKm_OrkDA-D01VxMcg.X9BfkhQz0S9eMV9EQvACotEzCZup5c9HmHFIoQnzv9cg.JPEG.babyhoney007/%EB%93%80%ED%81%AC.JPG?type=w3840"},
        {"name": "카봇 비트런",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMTMw/MDAxNTAzNzAyMTE2NDcy.3eqSo0F9c1cIRrac4POeNCXRvyMr2Onk9ql6Md5KCH8g.5ZUBfng6wzp7LwnbSzdX-xWJgC98BDsR9zS5oqlc8vAg.JPEG.babyhoney007/%EB%B9%84%ED%8A%B8%EB%9F%B0.JPG?type=w3840"},
        {"name": "카봇 메가볼드",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMjEy/MDAxNTAzNzAyMTQ2MDcx.LmA83V6uzfIWA61x1bMntfK6z_DRTylRMch84SipYhgg.UXGkpmcXB4TMqE8Tbo2iq2TjaXpEL-2PRia5fXNOAnAg.JPEG.babyhoney007/%EB%A9%94%EA%B0%80%EB%B3%BC%ED%8A%B8.JPG?type=w3840"},
        {"name": "카봇 하이퍼 빌디언",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfMjQw/MDAxNTAzNzAyMTcwOTM0.Jw1whIlzZoRGQ7fd5XXLLwRSBg3ibmmc9g9DDU1a9B4g.F492koRvkYM9jHi0EBqWc7XfspES6ytgvKvM9Xr_nJQg.JPEG.babyhoney007/%ED%95%98%EC%9D%B4%ED%8D%BC%EB%B9%8C%EB%94%94%EC%96%B8.JPG?type=w3840"},
        {"name": "카봇 에반 프라임",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfNDYg/MDAxNTAzNzAyMTk2NTA2.6GE5EArPqSh_9hIY3PQejCmJ2CKgqS08LPx5kT_I51Ag.Ly0vvY3ywPxTdz0zzRl5Opyo6yqKozL3agJGEcxbgvUg.JPEG.babyhoney007/%EC%97%90%EB%B0%98%ED%94%84%EB%9D%BC%EC%9E%84.JPG?type=w3840"},
        {"name": "카봇 드라고닉스",
         "img": "https://postfiles.pstatic.net/MjAxNzA4MjZfNzMg/MDAxNTAzNzAyMjMxMzYw.-1fj9tbPt4sHuCQau0L4L6gpGWfHO_pJ0VTIW2cntnsg.rOHDPwlwUF_geLwHOggDv38L7ApcmpdZ7pvcqDJHgGwg.JPEG.babyhoney007/%EB%93%9C%EB%9D%BC%EA%B3%A0%EB%8B%89%EC%8A%A4.JPG?type=w3840"}
    ]
if 'current_round' not in st.session_state:
    st.session_state.current_round = []
if 'next_round' not in st.session_state:
    st.session_state.next_round = []
if 'winner' not in st.session_state:
    st.session_state.winner = None
if 'match_index' not in st.session_state:
    st.session_state.match_index = 0


# ✅ 이미지 불러오기 (네이버 Referer 우회)
def load_image(url):
    headers = {"Referer": "https://www.naver.com"}
    try:
        response = requests.get(url, headers=headers)
        img = Image.open(BytesIO(response.content))
        return img
    except:
        return None  # 이미지 불러오기 실패 시


# ✅ 토너먼트 시작 함수
def start_tournament():
    candidates = st.session_state.candidates.copy()
    random.shuffle(candidates)
    st.session_state.current_round = candidates[:32]  # 32강으로 시작
    st.session_state.next_round = []
    st.session_state.match_index = 0  # 경기 인덱스 초기화
    st.session_state.stage = "tournament"
    st.rerun()


# ✅ 후보 선택 함수
def select_candidate(index):
    selected = st.session_state.current_round[index]
    st.session_state.next_round.append(selected)

    # 경기 진행 후 다음 경기로 넘어가도록 인덱스 업데이트
    st.session_state.match_index += 2

    # 라운드가 끝났는지 확인
    if st.session_state.match_index >= len(st.session_state.current_round):
        # 만약 현재 라운드가 2강이면 최종 우승자 결정
        if len(st.session_state.current_round) == 2:
            st.session_state.winner = st.session_state.next_round[0]
            st.session_state.stage = "result"
        else:
            st.session_state.current_round = st.session_state.next_round
            st.session_state.next_round = []
            st.session_state.match_index = 0  # 다음 라운드 초기화

    st.rerun()


# ✅ UI 화면 설정
st.title("🚗 헬로카봇 이상형 월드컵 🚀")

if st.session_state.stage == "start":
    st.write("아래 버튼을 눌러 이상형 월드컵을 시작하세요!")
    if st.button("🎮 게임 시작"):
        start_tournament()

elif st.session_state.stage == "tournament":
    st.subheader(f"⚔️ {len(st.session_state.current_round)}강전 ⚔️")
    match = st.session_state.match_index  # 현재 경기 인덱스

    # 두 후보의 이미지와 버튼을 표시 (대진이 아직 남아있는지 확인)
    if match + 1 < len(st.session_state.current_round):
        col1, col2 = st.columns(2)
        with col1:
            img1 = load_image(st.session_state.current_round[match]["img"])
            if img1:
                st.image(img1, caption=st.session_state.current_round[match]["name"])
            if st.button(f"✅ {st.session_state.current_round[match]['name']} 선택", key=f"btn_{match}"):
                select_candidate(match)
        with col2:
            img2 = load_image(st.session_state.current_round[match + 1]["img"])
            if img2:
                st.image(img2, caption=st.session_state.current_round[match + 1]["name"])
            if st.button(f"✅ {st.session_state.current_round[match + 1]['name']} 선택", key=f"btn_{match + 1}"):
                select_candidate(match + 1)
    else:
        st.write("모든 경기가 진행되었습니다.")

elif st.session_state.stage == "result":
    st.subheader("🏆 최종 우승자!")
    winner = st.session_state.winner
    img = load_image(winner["img"])
    if img:
        st.image(img, caption=winner["name"])
    st.write(f"🎉 **{winner['name']}** 가 최종 우승했습니다!")
    if st.button("🔄 다시하기"):
        st.session_state.stage = "start"
        st.rerun()
