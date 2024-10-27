import streamlit as st
import time

print("page reloaded")
st.set_page_config(
    page_title="KBO선수 도감",
    page_icon="kbo.noimage.png"
)
st.markdown("""
    <style>
    img {
        max-height: 300px;
        max-width: 100%;
        text-align: center;
        height: auto;
    }
    .streamlit-expanderContent div{
        display: flex;
        justify-content: center;
        font-size: 50px;
    }
    [data-testid="stExpanderToggleIcon"] {
        visibility: hidden;
    }
    .streamlit-expanderHeader {
        pointer-events: none;
    }

    [data-testid="StyledFullScreenButton] {
        visibility: hidden;
    }
    </style>
""", unsafe_allow_html=True)


with st.spinner("데이터를  불러오는 중..."):
    time.sleep(7)

st.title('KBO 선수 도감')
st.write('**현역 국내 KBO 선수를 찾을 수 있습니다! (24/10/28 Ver.)**')
st.text('24년 입단한 현역 선수까지의 검색을 지원하고 있습니다.')
st.text("고령은퇴자가 포함되어 있습니다. (박경수, 추신수, 김강민 등등을 포함함)")
st.text("")
st.write("**데이터 누락만 수정문의 부탁드립니다.**")
st.text("(예시: xxx선수 누락, xxx선수 프로필사진 있습니다.(사진첨부) 등등..)")
st.text("※단, 이미지 파일은 KBO 공식 홈페이지 프로필 파일만 지원합니다.")
st.text("")
st.write("**★수정문의: Instagram DM(@___hwjk)★**")
st.success("옵션을 바꿀 시 다시 검색을 눌러주세요!")

@st.cache_data(ttl=3600)
def load_data():
    return initial_players
def update_player_data(new_data):
    st.session_state.players = new_data

initial_players = [
    {
        "name": "강건",
        "types": ["KT", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53006.jpg"
    },
    {
        "name": "강동훈",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54607.jpg"
    },
    {
        "name": "강민",
        "types": ["LG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50105.jpg"
    },
    {
        "name": "강민성",
        "types": ["KT", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69064.jpg"
    },
    {
        "name": "강민제",
        "types": ["기아", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54613.jpg"
    },
    {
        "name": "강민호",
        "types": ["삼성", "포수", "2004년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/74540.jpg"
    },
    {
        "name": "강백호",
        "types": ["KT", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68050.jpg"
    },{
        "name": "강병우",
        "types": ["기아", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52659.jpg"
    },{
        "name": "강석현",
        "types": ["LG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54104.jpg"
    },{
        "name": "강성우",
        "types": ["롯데", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54567.jpg"
    },{
        "name": "강승구",
        "types": ["롯데", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54506.jpg"
    },
    {
        "name": "강승호",
        "types": ["두산", "내야수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63123.jpg"
    },
    {
        "name": "강이준",
        "types": ["기아", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67604.jpg"
    },
    {
        "name": "강재민",
        "types": ["한화", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50705.jpg"
    },
    {
        "name": "강준서",
        "types": ["삼성", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53460.jpg"
    },
    {
        "name": "강진성",
        "types": ["키움", "외야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62925.jpg"
    },
    {
        "name": "강태완",
        "types": ["두산", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54268.jpg"
    },
    {
        "name": "강태율",
        "types": ["롯데", "포수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65514.jpg"
    },
    {
        "name": "강한울",
        "types": ["삼성", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64610.jpg"
    },
    {
        "name": "강현구",
        "types": ["두산", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51269.jpg"
    },
    {
        "name": "강현우",
        "types": ["KT", "포수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50066.jpg"
    },
    {
        "name": "강효종",
        "types": ["LG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51143.jpg"
    },
    {
        "name": "고명준",
        "types": ["SSG", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51868.jpg"
    },
    {
        "name": "고승민",
        "types": ["롯데", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69517.jpg"
    },
    {
        "name": "고승완",
        "types": ["NC", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54908.jpg"
    },
    {
        "name": "고영우",
        "types": ["키움", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54344.jpg"
    },
    {
        "name": "고영표",
        "types": ["KT", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64001.jpg"
    },
    {
        "name": "고종욱",
        "types": ["기아", "외야수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61353.jpg"
    },
    {
        "name": "고효준",
        "types": ["SSG", "투수", "2002년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/72523.jpg"
    },
    {
        "name": "공민규",
        "types": ["삼성", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68407.jpg"
    },
    {
        "name": "곽도규",
        "types": ["기아", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53609.jpg"
    },
    {
        "name": "곽빈",
        "types": ["두산", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68220.jpg"
    },
    {
        "name": "구본혁",
        "types": ["LG", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69100.jpg"
    },
    {
        "name": "구승민",
        "types": ["롯데", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63543.jpg"
    },
    {
        "name": "구자욱",
        "types": ["삼성", "외야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62404.jpg"
    },
    {
        "name": "구창모",
        "types": ["NC", "투수", "2015년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "권광민",
        "types": ["한화", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52769.jpg"
    },
    {
        "name": "권동진",
        "types": ["KT", "주포", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51003.jpg"
    },
    {
        "name": "권동혁",
        "types": ["LG", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53168.jpg"
    },
    {
        "name": "권혁경",
        "types": ["기아", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51640.jpg"
    },
    {
        "name": "권현",
        "types": ["한화", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54708.jpg"
    },
    {
        "name": "권휘",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50203.jpg"
    },
    {
        "name": "권희동",
        "types": ["NC", "외야수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63963.jpg"
    },
    {
        "name": "김강률",
        "types": ["두산", "투수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77263.jpg"
    },
    {
        "name": "김강민",
        "types": ["한화", "외야수", "2001년 데뷔, KBO 은퇴"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/71837.jpg"
    },
    {
        "name": "김강현",
        "types": ["롯데", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65522.jpg"
    },
    {
        "name": "김건",
        "types": ["한화", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69702.jpg"
    },
    {
        "name": "김건국",
        "types": ["기아", "투수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76225.jpg"
    },
    {
        "name": "김건우",
        "types": ["SSG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51867.jpg"
    },
    {
        "name": "김건웅",
        "types": ["KT", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53049.jpg"
    },
    {
        "name": "김건웅",
        "types": ["SSG", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53844.jpg"
    },
    {
        "name": "김건형",
        "types": ["KT", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51005.jpg"
    },
    {
        "name": "김건희",
        "types": ["키움", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53312.jpg"
    },
    {
        "name": "김관우",
        "types": ["한화", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53701.jpg"
    },
    {
        "name": "김광현",
        "types": ["SSG", "투수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77829.jpg"
    },
    {
        "name": "김규민",
        "types": ["SSG", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54810.jpg"
    },
    {
        "name": "김규성",
        "types": ["기아", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66614.jpg"
    },
    {
        "name": "김규연",
        "types": ["한화", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51713.jpg"
    },
    {
        "name": "김기연",
        "types": ["두산", "포수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66112.jpg"
    },
    {
        "name": "김기중",
        "types": ["한화", "한화", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51715.jpg"
    },
    {
        "name": "김기훈",
        "types": ["기아", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69620.jpg"
    },
    {
        "name": "김녹원",
        "types": ["NC", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52995.jpg"
    },
    {
        "name": "김대우",
        "types": ["삼성", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61365.jpg"
    },
    {
        "name": "김대원",
        "types": ["LG", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54164.jpg"
    },
    {
        "name": "김대유",
        "types": ["기아", "투수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60337.jpg"
    },
    {
        "name": "김대한",
        "types": ["두산", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69238.jpg"
    },
    {
        "name": "김대현",
        "types": ["LG", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66145.jpg"
    },
    {
        "name": "김대현",
        "types": ["롯데", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54511.jpg"
    },
    {
        "name": "김대호",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54401.jpg"
    },
    {
        "name": "김도규",
        "types": ["롯데", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68585.jpg"
    },
    {
        "name": "김도빈",
        "types": ["한화", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54705.jpg"
    },
    {
        "name": "김도영",
        "types": ["기아", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52605.jpg"
    },
    {
        "name": "김도윤",
        "types": ["LG", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54107.jpg"
    },
    {
        "name": "김도윤",
        "types": ["두산", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51294.jpg"
    },
    {
        "name": "김도현",
        "types": ["SSG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52844.jpg"
    },
    {
        "name": "김도현",
        "types": ["기아", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69745.jpg"
    },
    {
        "name": "김도환",
        "types": ["삼성", "포수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69442.jpg"
    },
    {
        "name": "김동규",
        "types": ["롯데", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69592.jpg"
    },
    {
        "name": "김동규",
        "types": ["키움", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53164.jpg"
    },
    {
        "name": "김동엽",
        "types": ["삼성", "외야수", "2009년 데뷔(MiLB)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66838.jpg"
    },
    {
        "name": "김동욱",
        "types": ["키움", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50393.jpg"
    },
    {
        "name": "김동주",
        "types": ["두산", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51230.jpg"
    },
    {
        "name": "김동준",
        "types": ["두산", "외야수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "김동진",
        "types": ["삼성", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51403.jpg"
    },
    {
        "name": "김동헌",
        "types": ["키움", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53344.jpg"
    },
    {
        "name": "김동혁",
        "types": ["롯데", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52504.jpg"
    },
    {
        "name": "김동혁",
        "types": ["키움", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50360.jpg"
    },
    {
        "name": "김동현",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54402.jpg"
    },
    {
        "name": "김두현",
        "types": ["기아", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54614.jpg"
    },
    {
        "name": "김명신",
        "types": ["두산", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67246.jpg"
    },
    {
        "name": "김무빈",
        "types": ["두산", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54215.jpg"
    },
    {
        "name": "김문수",
        "types": ["두산", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53205.jpg"
    },
    {
        "name": "김민",
        "types": ["KT", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68043.jpg"
    },
    {
        "name": "김민규",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54913.jpg"
    },
    {
        "name": "김민규",
        "types": ["두산", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68200.jpg"
    },
    {
        "name": "김민균",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54901.jpg"
    },
    {
        "name": "김민기",
        "types": ["한화", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68707.jpg"
    },
    {
        "name": "김민석",
        "types": ["KT", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54097.jpg"
    },
    {
        "name": "김민석",
        "types": ["롯데", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53554.jpg"
    },
    {
        "name": "김민성",
        "types": ["KT", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54094.jpg"
    },
    {
        "name": "김민성",
        "types": ["롯데", "내야수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77564.jpg"
    },
    {
        "name": "김민수",
        "types": ["LG", "내야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67504.jpg"
    },
    {
        "name": "김민수",
        "types": ["KT", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65048.jpg"
    },
    {
        "name": "김민수",
        "types": ["기아", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69627.jpg"
    },
    {
        "name": "김민수",
        "types": ["삼성", "포수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64793.jpg"
    },
    {
        "name": "김민식",
        "types": ["SSG", "포수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62864.jpg"
    },
    {
        "name": "김민우",
        "types": ["한화", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65764.jpg"
    },
    {
        "name": "김민재",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54608.jpg"
    },
    {
        "name": "김민주",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54645.jpg"
    },
    {
        "name": "김민준",
        "types": ["SSG", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53893.jpg"
    },
    {
        "name": "김민혁",
        "types": ["KT", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64004.jpg"
    },
    {
        "name": "김민혁",
        "types": ["두산", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65269.jpg"
    },
    {
        "name": "김범석",
        "types": ["LG", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53144.jpg"
    },
    {
        "name": "김범수",
        "types": ["한화", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65769.jpg"
    },
    {
        "name": "김범준",
        "types": ["NC", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69980.jpg"
    },
    {
        "name": "김범준",
        "types": ["한화", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50710.jpg"
    },
    {
        "name": "김병준",
        "types": ["KT", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52002.jpg"
    },
    {
        "name": "김병휘",
        "types": ["키움", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50304.jpg"
    },
    {
        "name": "김사윤",
        "types": ["기아", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63894.jpg"
    },
    {
        "name": "김상민",
        "types": ["삼성", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52402.jpg"
    },
    {
        "name": "김상수",
        "types": ["KT", "내야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79402.jpg"
    },
    {
        "name": "김상수",
        "types": ["롯데", "투수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76430.jpg"
    },
    {
        "name": "김서준",
        "types": ["삼성", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52460.jpg"
    },
    {
        "name": "김서현",
        "types": ["한화", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53754.jpg"
    },
    {
        "name": "김석환",
        "types": ["기아", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67610.jpg"
    },
    {
        "name": "김선기",
        "types": ["키움", "투수", "2009년 데뷔(MiLB)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66018.jpg"
    },
    {
        "name": "김선빈",
        "types": ["기아", "내야수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78603.jpg"
    },
    {
        "name": "김선우",
        "types": ["기아", "포수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "김성경",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54403.jpg"
    },
    {
        "name": "김성민",
        "types": ["SSG", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50848.jpg"
    },
    {
        "name": "김성민",
        "types": ["키움", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67828.jpg"
    },
    {
        "name": "김성우",
        "types": ["LG", "포수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52105.jpg"
    },
    {
        "name": "김성욱",
        "types": ["NC", "외야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62934.jpg"
    },
    {
        "name": "김성윤",
        "types": ["삼성", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67449.jpg"
    },
    {
        "name": "김성진",
        "types": ["LG", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69105.jpg"
    },
    {
        "name": "김성진",
        "types": ["키움", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/51301.jpg"
    },
    {
        "name": "김성현",
        "types": ["SSG", "내야수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76802.jpg"
    },
    {
        "name": "김세민",
        "types": ["롯데", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52514.jpg"
    },
    {
        "name": "김세일",
        "types": ["기아", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53637.jpg"
    },
    {
        "name": "김세훈",
        "types": ["NC", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54905.jpg"
    },
    {
        "name": "김수인",
        "types": ["LG", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50115.jpg"
    },
    {
        "name": "김승일",
        "types": ["한화", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50711.jpg"
    },
    {
        "name": "김승현",
        "types": ["기아", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66492.jpg"
    },
    {
        "name": "김시앙",
        "types": ["키움", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51303.jpg"
    },
    {
        "name": "김시온",
        "types": ["삼성", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53464.jpg"
    },
    {
        "name": "김시현",
        "types": ["삼성", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67467.jpg"
    },
    {
        "name": "김시훈",
        "types": ["NC", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68928.jpg"
    },
    {
        "name": "김연주",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54368.jpg"
    },
    {
        "name": "김영규",
        "types": ["NC", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68900.jpg"
    },
    {
        "name": "김영웅",
        "types": ["삼성", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52430.jpg"
    },
    {
        "name": "김영준",
        "types": ["LG", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68130.jpg"
    },
    {
        "name": "김영현",
        "types": ["KT", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51097.jpg"
    },
    {
        "name": "김웅빈",
        "types": ["키움", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65898.jpg"
    },
    {
        "name": "김원중",
        "types": ["롯데", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62528.jpg"
    },
    {
        "name": "김유성",
        "types": ["두산", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53262.jpg"
    },
    {
        "name": "김유영",
        "types": ["LG", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64596.jpg"
    },
    {
        "name": "김윤수",
        "types": ["삼성", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68403.jpg"
    },
    {
        "name": "김윤식",
        "types": ["LG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50157.jpg"
    },
    {
        "name": "김윤하",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54319.jpg"
    },
    {
        "name": "김의준",
        "types": ["LG", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68109.jpg"
    },
    {
        "name": "김인범",
        "types": ["키움", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69367.jpg"
    },
    {
        "name": "김인태",
        "types": ["두산", "외야수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63257.jpg"
    },
    {
        "name": "김인환",
        "types": ["한화", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66715.jpg"
    },
    {
        "name": "김재민",
        "types": ["NC", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54909.jpg"
    },
    {
        "name": "김재상",
        "types": ["삼성", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53400.jpg"
    },
    {
        "name": "김재성",
        "types": ["삼성", "포수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65132.jpg"
    },
    {
        "name": "김재열",
        "types": ["NC", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64580.jpg"
    },
    {
        "name": "김재웅",
        "types": ["키움", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67391.jpg"
    },
    {
        "name": "김재윤",
        "types": ["삼성", "투수", "2009년 데뷔(MiLB)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65062.jpg"
    },
    {
        "name": "김재혁",
        "types": ["삼성", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52424.jpg"
    },
    {
        "name": "김재현",
        "types": ["기아", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53619.jpg"
    },
    {
        "name": "김재현",
        "types": ["키움", "포수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62332.jpg"
    },
    {
        "name": "김재형",
        "types": ["삼성", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54407.jpg"
    },
    {
        "name": "김재호",
        "types": ["두산", "내야수", "2004년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/74206.jpg"
    },
    {
        "name": "김재환",
        "types": ["두산", "외야수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78224.jpg"
    },
    {
        "name": "김정민",
        "types": ["SSG", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53865.jpg"
    },
    {
        "name": "김정우",
        "types": ["두산", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68830.jpg"
    },
    {
        "name": "김정운",
        "types": ["KT", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53029.jpg"
    },
    {
        "name": "김종수",
        "types": ["한화", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63765.jpg"
    },
    {
        "name": "김종우",
        "types": ["LG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54103.jpg"
    },
    {
        "name": "김주성",
        "types": ["LG", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66162.jpg"
    },
    {
        "name": "김주온",
        "types": ["LG", "투수", "2015년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "김주완",
        "types": ["LG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52140.jpg"
    },
    {
        "name": "김주원",
        "types": ["NC", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51907.jpg"
    },
    {
        "name": "김주훈",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54302.jpg"
    },
    {
        "name": "김준원",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54910.jpg"
    },
    {
        "name": "김준태",
        "types": ["KT", "포수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62558.jpg"
    },
    {
        "name": "김준형",
        "types": ["키움", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51393.jpg"
    },
    {
        "name": "김지성",
        "types": ["키움", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54397.jpg"
    },
    {
        "name": "김지찬",
        "types": ["삼성", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50458.jpg"
    },
    {
        "name": "김진성",
        "types": ["LG", "투수", "2004년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/75867.jpg"
    },
    {
        "name": "김진수",
        "types": ["LG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51154.jpg"
    },
    {
        "name": "김진욱",
        "types": ["롯데", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51516.jpg"
    },
    {
        "name": "김진호",
        "types": ["NC", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67954.jpg"
    },
    {
        "name": "김찬민",
        "types": ["기아", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52661.jpg"
    },
    {
        "name": "김찬형",
        "types": ["SSG", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66917.jpg"
    },
    {
        "name": "김창평",
        "types": ["SSG", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69825.jpg"
    },
    {
        "name": "김창훈",
        "types": ["롯데", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/51586.jpg"
    },
    {
        "name": "김철호",
        "types": ["KT", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68906.jpg"
    },
    {
        "name": "김태경",
        "types": ["NC", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50992.jpg"
    },
    {
        "name": "김태군",
        "types": ["기아", "포수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78122.jpg"
    },
    {
        "name": "김태근",
        "types": ["두산", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69207.jpg"
    },
    {
        "name": "김태연",
        "types": ["한화", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66704.jpg"
    },
    {
        "name": "김태오",
        "types": ["KT", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66064.jpg"
    },
    {
        "name": "김태완",
        "types": ["두산", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54217.jpg"
    },
    {
        "name": "김태우",
        "types": ["삼성", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68454.jpg"
    },
    {
        "name": "김태윤",
        "types": ["SSG", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52803.jpg"
    },
    {
        "name": "김태윤",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54609.jpg"
    },
    {
        "name": "김태진",
        "types": ["키움", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64984.jpg"
    },
    {
        "name": "김태현",
        "types": ["NC", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67956.jpg"
    },
    {
        "name": "김태호",
        "types": ["NC", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54912.jpg"
    },
    {
        "name": "김태훈(외)",
        "types": ["삼성", "외야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65040.jpg"
    },
    {
        "name": "김태훈(투)",
        "types": ["삼성", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62360.jpg"
    },
    {
        "name": "김택연",
        "types": ["두산", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54263.jpg"
    },
    {
        "name": "김택형",
        "types": ["SSG", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65343.jpg"
    },
    {
        "name": "김한별",
        "types": ["NC", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50902.jpg"
    },
    {
        "name": "김해찬",
        "types": ["한화", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53702.jpg"
    },
    {
        "name": "김헌곤",
        "types": ["삼성", "외야수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61404.jpg"
    },
    {
        "name": "김현수",
        "types": ["LG", "외야수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76290.jpg"
    },
    {
        "name": "김현수",
        "types": ["기아", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69516.jpg"
    },
    {
        "name": "김현종",
        "types": ["LG", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54166.jpg"
    },
    {
        "name": "김현준",
        "types": ["삼성", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51417.jpg"
    },
    {
        "name": "김형욱",
        "types": ["LG", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51103.jpg"
    },
    {
        "name": "김형준",
        "types": ["NC", "포수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68912.jpg"
    },
    {
        "name": "김혜성",
        "types": ["키움", "내야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67304.jpg"
    },
    {
        "name": "김호령",
        "types": ["기아", "외야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65653.jpg"
    },
    {
        "name": "김호준",
        "types": ["두산", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68269.jpg"
    },
    {
        "name": "김호진",
        "types": ["삼성", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54460.jpg"
    },
    {
        "name": "김휘건",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54959.jpg"
    },
    {
        "name": "김휘집",
        "types": ["NC", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51344.jpg"
    },
    {
        "name": "나균안",
        "types": ["롯데", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67539.jpg"
    },
    {
        "name": "나성범",
        "types": ["기아", "외야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62947.jpg"
    },
    {
        "name": "나승엽",
        "types": ["롯데", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51551.jpg"
    },
    {
        "name": "남지민",
        "types": ["한화", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50720.jpg"
    },
    {
        "name": "남호",
        "types": ["두산", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69104.jpg"
    },
    {
        "name": "노경은",
        "types": ["SSG", "투수", "2003년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/73211.jpg"
    },
    {
        "name": "노시환",
        "types": ["한화", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69737.jpg"
    },
    {
        "name": "노재원",
        "types": ["NC", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53914.jpg"
    },
    {
        "name": "노진혁",
        "types": ["롯데", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62931.jpg"
    },
    {
        "name": "도태훈",
        "types": ["NC", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66965.jpg"
    },
    {
        "name": "류승민",
        "types": ["삼성", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53404.jpg"
    },
    {
        "name": "류지혁",
        "types": ["삼성", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62234.jpg"
    },
    {
        "name": "류진욱",
        "types": ["NC", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65949.jpg"
    },
    {
        "name": "류현곤",
        "types": ["SSG", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53806.jpg"
    },
    {
        "name": "류현인",
        "types": ["KT", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53036.jpg"
    },
    {
        "name": "류현준",
        "types": ["두산", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54219.jpg"
    },
    {
        "name": "류현진",
        "types": ["한화", "투수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76715.jpg"
    },
    {
        "name": "류효승",
        "types": ["SSG", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50868.jpg"
    },
    {
        "name": "목지훈",
        "types": ["NC", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53973.jpg"
    },
    {
        "name": "문동주",
        "types": ["한화", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52701.jpg"
    },
    {
        "name": "문보경",
        "types": ["LG", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69102.jpg"
    },
    {
        "name": "문상준",
        "types": ["KT", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/50007.jpg"
    },
    {
        "name": "문상철",
        "types": ["KT", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64007.jpg"
    },
    {
        "name": "문성주",
        "types": ["LG", "외야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68119.jpg"
    },
    {
        "name": "문성현",
        "types": ["키움", "투수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60336.jpg"
    },
    {
        "name": "문승원",
        "types": ["SSG", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62869.jpg"
    },
    {
        "name": "문승진",
        "types": ["한화", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51705.jpg"
    },
    {
        "name": "문용익",
        "types": ["KT", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67419.jpg"
    },
    {
        "name": "문현빈",
        "types": ["한화", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53764.jpg"
    },
    {
        "name": "박건우",
        "types": ["NC", "외야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79215.jpg"
    },
    {
        "name": "박건우",
        "types": ["기아", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51645.jpg"
    },
    {
        "name": "박경수",
        "types": ["KT", "내야수", "2003년 데뷔(KBO은퇴)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/73113.jpg"
    },
    {
        "name": "박계범",
        "types": ["두산", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64468.jpg"
    },
    {
        "name": "박권후",
        "types": ["삼성", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53469.jpg"
    },
    {
        "name": "박기호",
        "types": ["SSG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54802.jpg"
    },
    {
        "name": "박대온",
        "types": ["SSG", "포수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64944.jpg"
    },
    {
        "name": "박동수",
        "types": ["NC", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52994.jpg"
    },
    {
        "name": "박동원",
        "types": ["LG", "포수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79365.jpg"
    },
    {
        "name": "박명근",
        "types": ["LG", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53139.jpg"
    },
    {
        "name": "박민",
        "types": ["기아", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50657.jpg"
    },
    {
        "name": "박민석",
        "types": ["KT", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69056.jpg"
    },
    {
        "name": "박민우",
        "types": ["NC", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62907.jpg"
    },
    {
        "name": "박민준",
        "types": ["두산", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53204.jpg"
    },
    {
        "name": "박민호",
        "types": ["LG", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51112.jpg"
    },
    {
        "name": "박범준",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54304.jpg"
    },
    {
        "name": "박병호",
        "types": ["삼성", "내야수", "2005년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/75125.jpg"
    },
    {
        "name": "박상언",
        "types": ["한화", "포수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66707.jpg"
    },
    {
        "name": "박상원",
        "types": ["한화", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67703.jpg"
    },
    {
        "name": "박상후",
        "types": ["SSG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54807.jpg"
    },
    {
        "name": "박성빈",
        "types": ["SSG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54807.jpg"
    },
    {
        "name": "박성빈",
        "types": ["키움", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53305.jpg"
    },
    {
        "name": "박성웅",
        "types": ["한화", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68703.jpg"
    },
    {
        "name": "박성재",
        "types": ["두산", "포수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "박성준",
        "types": ["롯데", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54502.jpg"
    },
    {
        "name": "박성한",
        "types": ["SSG", "내야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67893.jpg"
    },
    {
        "name": "박세웅",
        "types": ["롯데", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64021.jpg"
    },
    {
        "name": "박세직",
        "types": ["SSG", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53800.jpg"
    },
    {
        "name": "박세진",
        "types": ["KT", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66047.jpg"
    },
    {
        "name": "박세혁",
        "types": ["NC", "포수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62244.jpg"
    },
    {
        "name": "박수종",
        "types": ["키움", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52305.jpg"
    },
    {
        "name": "박승규",
        "types": ["삼성", "외야수", "2019년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "박승욱",
        "types": ["롯데", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62802.jpg"
    },
    {
        "name": "박승주",
        "types": ["키움", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66305.jpg"
    },
    {
        "name": "박승호",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54350.jpg"
    },
    {
        "name": "박시원",
        "types": ["NC", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50996.jpg"
    },
    {
        "name": "박시원",
        "types": ["삼성", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53409.jpg"
    },
    {
        "name": "박시후",
        "types": ["SSG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50812.jpg"
    },
    {
        "name": "박신지",
        "types": ["두산", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68249.jpg"
    },
    {
        "name": "박영빈",
        "types": ["NC", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50906.jpg"
    },
    {
        "name": "박영완",
        "types": ["롯데", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69507.jpg"
    },
    {
        "name": "박영현",
        "types": ["KT", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52060.jpg"
    },
    {
        "name": "박웅",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "박윤성",
        "types": ["키움", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53301.jpg"
    },
    {
        "name": "박인우",
        "types": ["NC", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54911.jpg"
    },
    {
        "name": "박장민",
        "types": ["삼성", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53416.jpg"
    },
    {
        "name": "박재민",
        "types": ["롯데", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50563.jpg"
    },
    {
        "name": "박정빈",
        "types": ["SSG", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51860.jpg"
    },
    {
        "name": "박정수",
        "types": ["두산", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65639.jpg"
    },
    {
        "name": "박정우",
        "types": ["기아", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67609.jpg"
    },
    {
        "name": "박정현",
        "types": ["KT", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54008.jpg"
    },
    {
        "name": "박정현",
        "types": ["한화", "내야수", "2020년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "박종훈",
        "types": ["SSG", "투수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60841.jpg"
    },
    {
        "name": "박주성",
        "types": ["키움", "투수", "2019년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "박주찬",
        "types": ["NC", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69900.jpg"
    },
    {
        "name": "박주혁",
        "types": ["삼성", "투수", "2020년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "박주현",
        "types": ["NC", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68097.jpg"
    },
    {
        "name": "박주홍",
        "types": ["키움", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50357.jpg"
    },
    {
        "name": "박준영",
        "types": ["두산", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66928.jpg"
    },
    {
        "name": "박준영",
        "types": ["한화", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52731.jpg"
    },
    {
        "name": "박준용",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54466.jpg"
    },
    {
        "name": "박준우",
        "types": ["롯데", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54503.jpg"
    },
    {
        "name": "박준표",
        "types": ["기아", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63638.jpg"
    },
    {
        "name": "박준형",
        "types": ["키움", "포수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69363.jpg"
    },
    {
        "name": "박지한",
        "types": ["NC", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69994.jpg"
    },
    {
        "name": "박지호",
        "types": ["두산", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54213.jpg"
    },
    {
        "name": "박지환",
        "types": ["SSG", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54805.jpg"
    },
    {
        "name": "박지훈",
        "types": ["두산", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50204.jpg"
    },
    {
        "name": "박진",
        "types": ["롯데", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69594.jpg"
    },
    {
        "name": "박진우",
        "types": ["삼성", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53411.jpg"
    },
    {
        "name": "박진형",
        "types": ["롯데", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63512.jpg"
    },
    {
        "name": "박찬혁",
        "types": ["키움", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52348.jpg"
    },
    {
        "name": "박찬호",
        "types": ["기아", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64646.jpg"
    },
    {
        "name": "박채울",
        "types": ["키움", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54303.jpg"
    },
    {
        "name": "박치국",
        "types": ["두산", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67266.jpg"
    },
    {
        "name": "박태완",
        "types": ["KT", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54009.jpg"
    },
    {
        "name": "박한결",
        "types": ["NC", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53992.jpg"
    },
    {
        "name": "박해민",
        "types": ["LG", "외야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62415.jpg"
    },
    {
        "name": "배강",
        "types": ["LG", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54116.jpg"
    },
    {
        "name": "배동현",
        "types": ["한화", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51761.jpg"
    },
    {
        "name": "배민서",
        "types": ["한화", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69974.jpg"
    },
    {
        "name": "배상호",
        "types": ["NC", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53988.jpg"
    },
    {
        "name": "배세종",
        "types": ["롯데", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54504.jpg"
    },
    {
        "name": "배재준",
        "types": ["LG", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63145.jpg"
    },
    {
        "name": "배재환",
        "types": ["NC", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64995.jpg"
    },
    {
        "name": "배정대",
        "types": ["KT", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64166.jpg"
    },
    {
        "name": "배제성",
        "types": ["KT", "투수", "2015년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "백두산",
        "types": ["롯데", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54507.jpg"
    },
    {
        "name": "백선기",
        "types": ["LG", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68096.jpg"
    },
    {
        "name": "백승건",
        "types": ["SSG", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69839.jpg"
    },
    {
        "name": "백승우",
        "types": ["두산", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53298.jpg"
    },
    {
        "name": "백승현",
        "types": ["LG", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65109.jpg"
    },
    {
        "name": "백정현",
        "types": ["삼성", "투수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77446.jpg"
    },
    {
        "name": "백준서",
        "types": ["SSG", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54814.jpg"
    },
    {
        "name": "변건우",
        "types": ["SSG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54808.jpg"
    },
    {
        "name": "변상권",
        "types": ["키움", "외야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68305.jpg"
    },
    {
        "name": "변우혁",
        "types": ["기아", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69727.jpg"
    },
    {
        "name": "서건창",
        "types": ["기아", "내야수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78168.jpg"
    },
    {
        "name": "서동욱",
        "types": ["NC", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53999.jpg"
    },
    {
        "name": "서동욱",
        "types": ["롯데", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53569.jpg"
    },
    {
        "name": "서예일",
        "types": ["두산", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66203.jpg"
    },
    {
        "name": "서유신",
        "types": ["키움", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53309.jpg"
    },
    {
        "name": "서의태",
        "types": ["NC", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66068.jpg"
    },
    {
        "name": "서준교",
        "types": ["NC", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52906.jpg"
    },
    {
        "name": "서진용",
        "types": ["SSG", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61895.jpg"
    },
    {
        "name": "서현원",
        "types": ["삼성", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53428.jpg"
    },
    {
        "name": "서호철",
        "types": ["NC", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69995.jpg"
    },
    {
        "name": "석상호",
        "types": ["롯데", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53560.jpg"
    },
    {
        "name": "석정우",
        "types": ["SSG", "내야수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "성동현",
        "types": ["LG", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68159.jpg"
    },
    {
        "name": "성영탁",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54610.jpg"
    },
    {
        "name": "성재헌",
        "types": ["KT", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50109.jpg"
    },
    {
        "name": "성지훈",
        "types": ["한화", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53711.jpg"
    },
    {
        "name": "소이현",
        "types": ["NC", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67962.jpg"
    },
    {
        "name": "소한빈",
        "types": ["롯데", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54512.jpg"
    },
    {
        "name": "소형준",
        "types": ["KT", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50030.jpg"
    },
    {
        "name": "손동현",
        "types": ["KT", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69041.jpg"
    },
    {
        "name": "손민석",
        "types": ["KT", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53057.jpg"
    },
    {
        "name": "손성빈",
        "types": ["롯데", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51528.jpg"
    },
    {
        "name": "손아섭",
        "types": ["NC", "외야수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77532.jpg"
    },
    {
        "name": "손용준",
        "types": ["LG", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54156.jpg"
    },
    {
        "name": "손율기",
        "types": ["두산", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54216.jpg"
    },
    {
        "name": "손주영",
        "types": ["LG", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67143.jpg"
    },
    {
        "name": "손주환",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54904.jpg"
    },
    {
        "name": "손현기",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54363.jpg"
    },
    {
        "name": "손호영",
        "types": ["롯데", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50150.jpg"
    },
    {
        "name": "송대현",
        "types": ["LG", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53105.jpg"
    },
    {
        "name": "송명기",
        "types": ["NC", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69962.jpg"
    },
    {
        "name": "송민섭",
        "types": ["KT", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64012.jpg"
    },
    {
        "name": "송성문",
        "types": ["키움", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65357.jpg"
    },
    {
        "name": "송성훈",
        "types": ["한화", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53704.jpg"
    },
    {
        "name": "송승기",
        "types": ["LG", "투수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "송승환",
        "types": ["NC", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69203.jpg"
    },
    {
        "name": "송영진",
        "types": ["SSG", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53898.jpg"
    },
    {
        "name": "송재영",
        "types": ["롯데", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51594.jpg"
    },
    {
        "name": "송정인",
        "types": ["키움", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52391.jpg"
    },
    {
        "name": "송지후",
        "types": ["키움", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54394.jpg"
    },
    {
        "name": "송찬의",
        "types": ["LG", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68110.jpg"
    },
    {
        "name": "송호정",
        "types": ["한화", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51767.jpg"
    },
    {
        "name": "승지환",
        "types": ["한화", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54701.jpg"
    },
    {
        "name": "신경민",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54405.jpg"
    },
    {
        "name": "신민재",
        "types": ["LG", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65207.jpg"
    },
    {
        "name": "신민혁",
        "types": ["NC", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68902.jpg"
    },
    {
        "name": "신범수",
        "types": ["SSG", "포수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66662.jpg"
    },
    {
        "name": "신범준",
        "types": ["KT", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51057.jpg"
    },
    {
        "name": "신병률",
        "types": ["롯데", "투수", "2018년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "신본기",
        "types": ["KT", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62556.jpg"
    },
    {
        "name": "신성호",
        "types": ["NC", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53989.jpg"
    },
    {
        "name": "신영우",
        "types": ["NC", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53919.jpg"
    },
    {
        "name": "신용석",
        "types": ["NC", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53991.jpg"
    },
    {
        "name": "신우재",
        "types": ["한화", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53717.jpg"
    },
    {
        "name": "신윤호",
        "types": ["삼성", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53415.jpg"
    },
    {
        "name": "신윤후",
        "types": ["롯데", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69508.jpg"
    },
    {
        "name": "신정환",
        "types": ["삼성", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52440.jpg"
    },
    {
        "name": "신헌민",
        "types": ["SSG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52873.jpg"
    },
    {
        "name": "신호준",
        "types": ["KT", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54007.jpg"
    },
    {
        "name": "심규빈",
        "types": ["LG", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54108.jpg"
    },
    {
        "name": "심우준",
        "types": ["KT", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64006.jpg"
    },
    {
        "name": "심재민",
        "types": ["롯데", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64017.jpg"
    },
    {
        "name": "심휘윤",
        "types": ["키움", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54306.jpg"
    },
    {
        "name": "안상현",
        "types": ["SSG", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66864.jpg"
    },
    {
        "name": "안승한",
        "types": ["두산", "포수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64011.jpg"
    },
    {
        "name": "안우진",
        "types": ["롯데", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54509.jpg"
    },
    {
        "name": "안우진",
        "types": ["키움", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/68341.jpg"
    },
    {
        "name": "안익훈",
        "types": ["LG", "외야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65115.jpg"
    },
    {
        "name": "안인산",
        "types": ["NC", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50901.jpg"
    },
    {
        "name": "안재석",
        "types": ["두산", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/51203.jpg"
    },
    {
        "name": "안주형",
        "types": ["삼성", "내야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66406.jpg"
    },
    {
        "name": "안중열",
        "types": ["NC", "포수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64022.jpg"
    },
    {
        "name": "안진",
        "types": ["한화", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51704.jpg"
    },
    {
        "name": "안치영",
        "types": ["KT", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67006.jpg"
    },
    {
        "name": "안치홍",
        "types": ["한화", "내야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79608.jpg"
    },
    {
        "name": "안현민",
        "types": ["KT", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52001.jpg"
    },
    {
        "name": "양경모",
        "types": ["한화", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52702.jpg"
    },
    {
        "name": "양도근",
        "types": ["삼성", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54408.jpg"
    },
    {
        "name": "양석환",
        "types": ["두산", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64153.jpg"
    },
    {
        "name": "양우현",
        "types": ["삼성", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69403.jpg"
    },
    {
        "name": "양의지",
        "types": ["두산", "포수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76232.jpg"
    },
    {
        "name": "양지율",
        "types": ["키움", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67365.jpg"
    },
    {
        "name": "양찬열",
        "types": ["두산", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50293.jpg"
    },
    {
        "name": "양창섭",
        "types": ["삼성", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/68415.jpg"
    },
    {
        "name": "양현",
        "types": ["삼성", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61268.jpg"
    },
    {
        "name": "양현종",
        "types": ["기아", "투수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77637.jpg"
    },
    {
        "name": "양현진",
        "types": ["두산", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51200.jpg"
    },
    {
        "name": "엄상백",
        "types": ["KT", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65056.jpg"
    },
    {
        "name": "여동건",
        "types": ["두산", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54205.jpg"
    },
    {
        "name": "예진원",
        "types": ["기아", "외야수", "2018년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "오규석",
        "types": ["기아", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50622.jpg"
    },
    {
        "name": "오명진",
        "types": ["두산", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50208.jpg"
    },
    {
        "name": "오상원",
        "types": ["키움", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53300.jpg"
    },
    {
        "name": "오석주",
        "types": ["키움", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67116.jpg"
    },
    {
        "name": "오선우",
        "types": ["기아", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69636.jpg"
    },
    {
        "name": "오선진",
        "types": ["롯데", "내야수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78756.jpg"
    },
    {
        "name": "오세훈",
        "types": ["한화", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51202.jpg"
    },
    {
        "name": "오승윤",
        "types": ["LG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54105.jpg"
    },
    {
        "name": "오승환",
        "types": ["삼성", "투수", "2005년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/75421.jpg"
    },
    {
        "name": "오영수",
        "types": ["NC", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68904.jpg"
    },
    {
        "name": "오원석",
        "types": ["SSG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50859.jpg"
    },
    {
        "name": "오윤석",
        "types": ["KT", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64504.jpg"
    },
    {
        "name": "오장한",
        "types": ["NC", "외야수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "오재일",
        "types": ["KT", "내야수", "2005년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/75334.jpg"
    },
    {
        "name": "오정환",
        "types": ["기아", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68614.jpg"
    },
    {
        "name": "오지환",
        "types": ["LG", "내야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79109.jpg"
    },
    {
        "name": "오태곤",
        "types": ["SSG", "외야수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60558.jpg"
    },
    {
        "name": "오태양",
        "types": ["NC", "내야수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "오현석",
        "types": ["삼성", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51466.jpg"
    },
    {
        "name": "우강훈",
        "types": ["LG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51526.jpg"
    },
    {
        "name": "우규민",
        "types": ["KT", "투수", "2003년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/73117.jpg"
    },
    {
        "name": "원상현",
        "types": ["KT", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54063.jpg"
    },
    {
        "name": "원성준",
        "types": ["키움", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54307.jpg"
    },
    {
        "name": "원종해",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54906.jpg"
    },
    {
        "name": "원종혁",
        "types": ["한화", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54702.jpg"
    },
    {
        "name": "원종현",
        "types": ["키움", "투수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76118.jpg"
    },
    {
        "name": "원태인",
        "types": ["삼성", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69446.jpg"
    },
    {
        "name": "유강남",
        "types": ["롯데", "포수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61102.jpg"
    },
    {
        "name": "유로결",
        "types": ["한화", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69766.jpg"
    },
    {
        "name": "유민",
        "types": ["한화", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52765.jpg"
    },
    {
        "name": "유병선",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54406.jpg"
    },
    {
        "name": "유승철",
        "types": ["기아", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67640.jpg"
    },
    {
        "name": "유영찬",
        "types": ["LG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50106.jpg"
    },
    {
        "name": "유제모",
        "types": ["롯데", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54513.jpg"
    },
    {
        "name": "유준규",
        "types": ["KT", "내야수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "유지성",
        "types": ["기아", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50604.jpg"
    },
    {
        "name": "육선엽",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54404.jpg"
    },
    {
        "name": "육청명",
        "types": ["KT", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54064.jpg"
    },
    {
        "name": "윤대경",
        "types": ["한화", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63464.jpg"
    },
    {
        "name": "윤도현",
        "types": ["기아", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52667.jpg"
    },
    {
        "name": "윤동희",
        "types": ["롯데", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52591.jpg"
    },
    {
        "name": "윤산흠",
        "types": ["한화", "투수", "2019년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "윤석원",
        "types": ["키움", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52395.jpg"
    },
    {
        "name": "윤성보",
        "types": ["SSG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54809.jpg"
    },
    {
        "name": "윤성빈",
        "types": ["롯데", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67588.jpg"
    },
    {
        "name": "윤수녕",
        "types": ["롯데", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53505.jpg"
    },
    {
        "name": "윤영철",
        "types": ["기아", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53613.jpg"
    },
    {
        "name": "윤정빈",
        "types": ["삼성", "외야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68463.jpg"
    },
    {
        "name": "윤준혁",
        "types": ["KT", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50092.jpg"
    },
    {
        "name": "윤준호",
        "types": ["두산", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53296.jpg"
    },
    {
        "name": "윤중현",
        "types": ["기아", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68619.jpg"
    },
    {
        "name": "윤태현",
        "types": ["SSG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52867.jpg"
    },
    {
        "name": "윤태호",
        "types": ["두산", "투수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이강준",
        "types": ["키움", "투수", "2020년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이건욱",
        "types": ["SSG", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64861.jpg"
    },
    {
        "name": "이교훈",
        "types": ["두산", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69205.jpg"
    },
    {
        "name": "이근혁",
        "types": ["KT", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54010.jpg"
    },
    {
        "name": "이기순",
        "types": ["SSG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52868.jpg"
    },
    {
        "name": "이기창",
        "types": ["한화", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54703.jpg"
    },
    {
        "name": "이도윤",
        "types": ["한화", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65703.jpg"
    },
    {
        "name": "이도현",
        "types": ["기아", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53615.jpg"
    },
    {
        "name": "이로운",
        "types": ["SSG", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53892.jpg"
    },
    {
        "name": "이명기",
        "types": ["키움", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69366.jpg"
    },
    {
        "name": "이명종",
        "types": ["키움", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52397.jpg"
    },
    {
        "name": "이민석",
        "types": ["두산", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52209.jpg"
    },
    {
        "name": "이민석",
        "types": ["롯데", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52530.jpg"
    },
    {
        "name": "이민우",
        "types": ["한화", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65616.jpg"
    },
    {
        "name": "이민준",
        "types": ["한화", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53795.jpg"
    },
    {
        "name": "이민호",
        "types": ["LG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/50126.jpg"
    },
    {
        "name": "이믿음",
        "types": ["LG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51110.jpg"
    },
    {
        "name": "이병준",
        "types": ["롯데", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51592.jpg"
    },
    {
        "name": "이병헌",
        "types": ["두산", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52204.jpg"
    },
    {
        "name": "이병헌",
        "types": ["삼성", "포수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69428.jpg"
    },
    {
        "name": "이상규",
        "types": ["한화", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65117.jpg"
    },
    {
        "name": "이상동",
        "types": ["KT", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69054.jpg"
    },
    {
        "name": "이상민",
        "types": ["삼성", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63960.jpg"
    },
    {
        "name": "이상영",
        "types": ["LG", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69168.jpg"
    },
    {
        "name": "이상준",
        "types": ["기아", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54644.jpg"
    },
    {
        "name": "이상혁",
        "types": ["한화", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52704.jpg"
    },
    {
        "name": "이선우",
        "types": ["KT", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69068.jpg"
    },
    {
        "name": "이선우",
        "types": ["롯데", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54595.jpg"
    },
    {
        "name": "이성규",
        "types": ["삼성", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66409.jpg"
    },
    {
        "name": "이송찬",
        "types": ["기아", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53663.jpg"
    },
    {
        "name": "이승민",
        "types": ["SSG", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54806.jpg"
    },
    {
        "name": "이승민",
        "types": ["삼성", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50464.jpg"
    },
    {
        "name": "이승언",
        "types": ["KT", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54012.jpg"
    },
    {
        "name": "이승원",
        "types": ["키움", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53302.jpg"
    },
    {
        "name": "이승재",
        "types": ["기아", "투수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이승진",
        "types": ["두산", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64805.jpg"
    },
    {
        "name": "이승헌",
        "types": ["롯데", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68529.jpg"
    },
    {
        "name": "이승현",
        "types": ["KT", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54011.jpg"
    },
    {
        "name": "이승현",
        "types": ["한화", "포수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54706.jpg"
    },
    {
        "name": "이승현(우)",
        "types": ["삼성", "투수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60146.jpg"
    },
    {
        "name": "이승현(좌)",
        "types": ["삼성", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51454.jpg"
    },
    {
        "name": "이승호",
        "types": ["키움", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/67603.jpg"
    },
    {
        "name": "이승훈",
        "types": ["SSG", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53809.jpg"
    },
    {
        "name": "이영빈",
        "types": ["LG", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51100.jpg"
    },
    {
        "name": "이영하",
        "types": ["두산", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66291.jpg"
    },
    {
        "name": "이용규",
        "types": ["키움", "외야수", "2004년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/74163.jpg"
    },
    {
        "name": "이용준",
        "types": ["NC", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51948.jpg"
    },
    {
        "name": "이용찬",
        "types": ["NC", "투수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77211.jpg"
    },
    {
        "name": "이우성",
        "types": ["기아", "내야수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63260.jpg"
    },
    {
        "name": "이우찬",
        "types": ["LG", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61145.jpg"
    },
    {
        "name": "이우현",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54301.jpg"
    },
    {
        "name": "이원석",
        "types": ["한화", "외야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68700.jpg"
    },
    {
        "name": "이원석",
        "types": ["키움", "내야수", "2005년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/75566.jpg"
    },
    {
        "name": "이원재",
        "types": ["두산", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52295.jpg"
    },
    {
        "name": "이유찬",
        "types": ["두산", "내야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67207.jpg"
    },
    {
        "name": "이의리",
        "types": ["기아", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51648.jpg"
    },
    {
        "name": "이인복",
        "types": ["롯데", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64565.jpg"
    },
    {
        "name": "이재상",
        "types": ["키움", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54305.jpg"
    },
    {
        "name": "이재원",
        "types": ["LG", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68106.jpg"
    },
    {
        "name": "이재원",
        "types": ["한화", "포수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76812.jpg"
    },
    {
        "name": "이재익",
        "types": ["삼성", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63492.jpg"
    },
    {
        "name": "이재학",
        "types": ["NC", "투수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60263.jpg"
    },
    {
        "name": "이재현",
        "types": ["삼성", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52415.jpg"
    },
    {
        "name": "이재호",
        "types": ["삼성", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54410.jpg"
    },
    {
        "name": "이재희",
        "types": ["삼성", "투수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이정범",
        "types": ["SSG", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67807.jpg"
    },
    {
        "name": "이정용",
        "types": ["LG", "투수", "2019년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이정현",
        "types": ["KT", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67048.jpg"
    },
    {
        "name": "이정훈",
        "types": ["롯데", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67644.jpg"
    },
    {
        "name": "이종민",
        "types": ["키움", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50354.jpg"
    },
    {
        "name": "이종준",
        "types": ["LG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50904.jpg"
    },
    {
        "name": "이종혁",
        "types": ["KT", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67066.jpg"
    },
    {
        "name": "이주엽",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50262.jpg"
    },
    {
        "name": "이주찬",
        "types": ["롯데", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51560.jpg"
    },
    {
        "name": "이주헌",
        "types": ["LG", "포수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이주형(01)",
        "types": ["키움", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50167.jpg"
    },
    {
        "name": "이주형(02)",
        "types": ["키움", "외야수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이준명",
        "types": ["KT", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53005.jpg"
    },
    {
        "name": "이준서",
        "types": ["LG", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53160.jpg"
    },
    {
        "name": "이준영",
        "types": ["기아", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65665.jpg"
    },
    {
        "name": "이준호",
        "types": ["NC", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53996.jpg"
    },
    {
        "name": "이준희",
        "types": ["KT", "포수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53001.jpg"
    },
    {
        "name": "이지강",
        "types": ["LG", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69108.jpg"
    },
    {
        "name": "이지영",
        "types": ["SSG", "포수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79456.jpg"
    },
    {
        "name": "이진영",
        "types": ["한화", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66657.jpg"
    },
    {
        "name": "이진하",
        "types": ["롯데", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53562.jpg"
    },
    {
        "name": "이창용",
        "types": ["삼성", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51407.jpg"
    },
    {
        "name": "이창진",
        "types": ["기아", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64560.jpg"
    },
    {
        "name": "이채호",
        "types": ["KT", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68896.jpg"
    },
    {
        "name": "이충호",
        "types": ["한화", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63749.jpg"
    },
    {
        "name": "이태규",
        "types": ["KT", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69623.jpg"
    },
    {
        "name": "이태양",
        "types": ["한화", "투수", "2010년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60768.jpg"
    },
    {
        "name": "이태연",
        "types": ["롯데", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53594.jpg"
    },
    {
        "name": "이학주",
        "types": ["롯데", "내야수", "2009년 데뷔(MiLB)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69453.jpg"
    },
    {
        "name": "이해승",
        "types": ["삼성", "내야수", "2019년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "이현준",
        "types": ["삼성", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54411.jpg"
    },
    {
        "name": "이형범",
        "types": ["기아", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62951.jpg"
    },
    {
        "name": "이형종",
        "types": ["키움", "외야수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78135.jpg"
    },
    {
        "name": "이호성",
        "types": ["삼성", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53455.jpg"
    },
    {
        "name": "이호연",
        "types": ["KT", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68504.jpg"
    },
    {
        "name": "이호준",
        "types": ["롯데", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54598.jpg"
    },
    {
        "name": "임기영",
        "types": ["기아", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62754.jpg"
    },
    {
        "name": "임병욱",
        "types": ["키움", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64346.jpg"
    },
    {
        "name": "임상현",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54900.jpg"
    },
    {
        "name": "임서준",
        "types": ["두산", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53293.jpg"
    },
    {
        "name": "임정호",
        "types": ["NC", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63959.jpg"
    },
    {
        "name": "임종성",
        "types": ["두산", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54236.jpg"
    },
    {
        "name": "임종찬",
        "types": ["한화", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50704.jpg"
    },
    {
        "name": "임준섭",
        "types": ["롯데", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62611.jpg"
    },
    {
        "name": "임준형",
        "types": ["LG", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69113.jpg"
    },
    {
        "name": "임지민",
        "types": ["NC", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52902.jpg"
    },
    {
        "name": "임지열",
        "types": ["키움", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64340.jpg"
    },
    {
        "name": "임찬규",
        "types": ["LG", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61101.jpg"
    },
    {
        "name": "임창민",
        "types": ["삼성", "투수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78352.jpg"
    },
    {
        "name": "임형원",
        "types": ["NC", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50900.jpg"
    },
    {
        "name": "장규빈",
        "types": ["두산", "포수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50244.jpg"
    },
    {
        "name": "장규현",
        "types": ["한화", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51762.jpg"
    },
    {
        "name": "장두성",
        "types": ["롯데", "외야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68507.jpg"
    },
    {
        "name": "장민기",
        "types": ["기아", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51665.jpg"
    },
    {
        "name": "장민재",
        "types": ["한화", "투수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79764.jpg"
    },
    {
        "name": "장성우",
        "types": ["KT", "포수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78548.jpg"
    },
    {
        "name": "장세진",
        "types": ["롯데", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53596.jpg"
    },
    {
        "name": "장승현",
        "types": ["두산", "포수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63202.jpg"
    },
    {
        "name": "장시현",
        "types": ["기아", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51603.jpg"
    },
    {
        "name": "장시환",
        "types": ["한화", "투수", "2007년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77318.jpg"
    },
    {
        "name": "장우진",
        "types": ["두산", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53267.jpg"
    },
    {
        "name": "장재영",
        "types": ["키움", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51359.jpg"
    },
    {
        "name": "장재혁",
        "types": ["기아", "투수", "2020년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "장준원",
        "types": ["KT", "내야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64115.jpg"
    },
    {
        "name": "장지수",
        "types": ["한화", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69645.jpg"
    },
    {
        "name": "장지훈",
        "types": ["SSG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51895.jpg"
    },
    {
        "name": "장진혁",
        "types": ["한화", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66706.jpg"
    },
    {
        "name": "장필준",
        "types": ["삼성", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/77927.jpg"
    },
    {
        "name": "장현식",
        "types": ["기아", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63950.jpg"
    },
    {
        "name": "전다민",
        "types": ["두산", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54214.jpg"
    },
    {
        "name": "전루건",
        "types": ["NC", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69204.jpg"
    },
    {
        "name": "전미르",
        "types": ["롯데", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54561.jpg"
    },
    {
        "name": "전민재",
        "types": ["두산", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68205.jpg"
    },
    {
        "name": "전병우",
        "types": ["삼성", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65586.jpg"
    },
    {
        "name": "전사민",
        "types": ["NC", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69969.jpg"
    },
    {
        "name": "전상현",
        "types": ["기아", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66609.jpg"
    },
    {
        "name": "전영준",
        "types": ["SSG", "투수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "전용주",
        "types": ["KT", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69047.jpg"
    },
    {
        "name": "전의산",
        "types": ["SSG", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50820.jpg"
    },
    {
        "name": "전준우",
        "types": ["롯데", "외야수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78513.jpg"
    },
    {
        "name": "전준표",
        "types": ["키움", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54362.jpg"
    },
    {
        "name": "전준호",
        "types": ["LG", "포수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67123.jpg"
    },
    {
        "name": "전하원",
        "types": ["롯데", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54505.jpg"
    },
    {
        "name": "정구범",
        "types": ["NC", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/50995.jpg"
    },
    {
        "name": "정대선",
        "types": ["롯데", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53568.jpg"
    },
    {
        "name": "정동윤",
        "types": ["SSG", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66858.jpg"
    },
    {
        "name": "정민규",
        "types": ["한화", "내야수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "정민성",
        "types": ["삼성", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54467.jpg"
    },
    {
        "name": "정보근",
        "types": ["롯데", "포수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68518.jpg"
    },
    {
        "name": "정성종",
        "types": ["롯데", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68556.jpg"
    },
    {
        "name": "정수빈",
        "types": ["두산", "외야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79231.jpg"
    },
    {
        "name": "정안석",
        "types": ["한화", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54794.jpg"
    },
    {
        "name": "정우람",
        "types": ["한화", "투수", "2004년 데뷔(KBO은퇴)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/74857.jpg"
    },
    {
        "name": "정우영",
        "types": ["LG", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69159.jpg"
    },
    {
        "name": "정우준",
        "types": ["롯데", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51546.jpg"
    },
    {
        "name": "정은원",
        "types": ["한화", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68743.jpg"
    },
    {
        "name": "정이황",
        "types": ["한화", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69767.jpg"
    },
    {
        "name": "정주영",
        "types": ["NC", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53995.jpg"
    },
    {
        "name": "정준영",
        "types": ["KT", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53058.jpg"
    },
    {
        "name": "정준재",
        "types": ["SSG", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54812.jpg"
    },
    {
        "name": "정지헌",
        "types": ["LG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54149.jpg"
    },
    {
        "name": "정진호",
        "types": ["KT", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53004.jpg"
    },
    {
        "name": "정철원",
        "types": ["두산", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68242.jpg"
    },
    {
        "name": "정해영",
        "types": ["기아", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50662.jpg"
    },
    {
        "name": "정해원",
        "types": ["기아", "내야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53659.jpg"
    },
    {
        "name": "정현수",
        "types": ["롯데", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54537.jpg"
    },
    {
        "name": "정현승",
        "types": ["SSG", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54815.jpg"
    },
    {
        "name": "정훈",
        "types": ["롯데", "내야수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/60523.jpg"
    },
    {
        "name": "제환유",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50211.jpg"
    },
    {
        "name": "조건희",
        "types": ["LG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51163.jpg"
    },
    {
        "name": "조경민",
        "types": ["롯데", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/53504.jpg"
    },
    {
        "name": "조대현",
        "types": ["KT", "포수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68089.jpg"
    },
    {
        "name": "조대현",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54667.jpg"
    },
    {
        "name": "조동욱",
        "types": ["한화", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54768.jpg"
    },
    {
        "name": "조민석",
        "types": ["NC", "투수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "조민성",
        "types": ["삼성", "내야수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "조병현",
        "types": ["SSG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51897.jpg"
    },
    {
        "name": "조상우",
        "types": ["키움", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63342.jpg"
    },
    {
        "name": "조성훈",
        "types": ["키움", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68848.jpg"
    },
    {
        "name": "조세진",
        "types": ["롯데", "외야수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "조수행",
        "types": ["두산", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66209.jpg"
    },
    {
        "name": "조영건",
        "types": ["키움", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69360.jpg"
    },
    {
        "name": "조요한",
        "types": ["SSG", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51809.jpg"
    },
    {
        "name": "조원태",
        "types": ["LG", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/52149.jpg"
    },
    {
        "name": "조은",
        "types": ["한화", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51796.jpg"
    },
    {
        "name": "조이현",
        "types": ["KT", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64768.jpg"
    },
    {
        "name": "조제영",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50296.jpg"
    },
    {
        "name": "조한민",
        "types": ["한화", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69705.jpg"
    },
    {
        "name": "조현민",
        "types": ["NC", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54907.jpg"
    },
    {
        "name": "조현진",
        "types": ["NC", "내야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51701.jpg"
    },
    {
        "name": "조형우",
        "types": ["SSG", "포수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51865.jpg"
    },
    {
        "name": "주권",
        "types": ["KT", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65060.jpg"
    },
    {
        "name": "주성원",
        "types": ["키움", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69332.jpg"
    },
    {
        "name": "주승빈",
        "types": ["키움", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52396.jpg"
    },
    {
        "name": "주승우",
        "types": ["키움", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52330.jpg"
    },
    {
        "name": "주한울",
        "types": ["삼성", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51468.jpg"
    },
    {
        "name": "주현상",
        "types": ["한화", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65707.jpg"
    },
    {
        "name": "주효상",
        "types": ["기아", "포수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66354.jpg"
    },
    {
        "name": "지명성",
        "types": ["KT", "투수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "진승현",
        "types": ["롯데", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52558.jpg"
    },
    {
        "name": "진우영",
        "types": ["LG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54148.jpg"
    },
    {
        "name": "진해수",
        "types": ["롯데", "투수", "2005년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76650.jpg"
    },
    {
        "name": "차동영",
        "types": ["삼성", "포수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "채은성",
        "types": ["한화", "외야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79192.jpg"
    },
    {
        "name": "채현우",
        "types": ["SSG", "외야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69804.jpg"
    },
    {
        "name": "천성호",
        "types": ["KT", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50054.jpg"
    },
    {
        "name": "천재환",
        "types": ["NC", "외야수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67905.jpg"
    },
    {
        "name": "최명경",
        "types": ["LG", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54112.jpg"
    },
    {
        "name": "최민준",
        "types": ["SSG", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68856.jpg"
    },
    {
        "name": "최민창",
        "types": ["SSG", "외야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65157.jpg"
    },
    {
        "name": "최보성",
        "types": ["NC", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68909.jpg"
    },
    {
        "name": "최상민",
        "types": ["SSG", "외야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68805.jpg"
    },
    {
        "name": "최성민",
        "types": ["KT", "외야수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51007.jpg"
    },
    {
        "name": "최성영",
        "types": ["NC", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66920.jpg"
    },
    {
        "name": "최성훈",
        "types": ["삼성", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62146.jpg"
    },
    {
        "name": "최세창",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50298.jpg"
    },
    {
        "name": "최수호",
        "types": ["SSG", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69893.jpg"
    },
    {
        "name": "최승민",
        "types": ["LG", "외야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65905.jpg"
    },
    {
        "name": "최승용",
        "types": ["두산", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51264.jpg"
    },
    {
        "name": "최용준",
        "types": ["KT", "투수", "2021년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "최용하",
        "types": ["LG", "투수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "최우석",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54903.jpg"
    },
    {
        "name": "최우인",
        "types": ["롯데", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51564.jpg"
    },
    {
        "name": "최원영",
        "types": ["LG", "외야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52103.jpg"
    },
    {
        "name": "최원준",
        "types": ["두산", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67263.jpg"
    },
    {
        "name": "최원준",
        "types": ["기아", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66606.jpg"
    },
    {
        "name": "최원태",
        "types": ["LG", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65320.jpg"
    },
    {
        "name": "최윤서",
        "types": ["KT", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54006.jpg"
    },
    {
        "name": "최이준",
        "types": ["롯데", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68036.jpg"
    },
    {
        "name": "최인호",
        "types": ["한화", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50707.jpg"
    },
    {
        "name": "최재훈",
        "types": ["한화", "포수", "2008년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/78288.jpg"
    },
    {
        "name": "최정",
        "types": ["SSG", "내야수", "2005년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/75847.jpg"
    },
    {
        "name": "최정용",
        "types": ["기아", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65464.jpg"
    },
    {
        "name": "최정원",
        "types": ["NC", "내야수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69992.jpg"
    },
    {
        "name": "최종인",
        "types": ["두산", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50206.jpg"
    },
    {
        "name": "최주환",
        "types": ["키움", "내야수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76267.jpg"
    },
    {
        "name": "최준서",
        "types": ["한화", "외야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54710.jpg"
    },
    {
        "name": "최준용",
        "types": ["롯데", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50556.jpg"
    },
    {
        "name": "최준우",
        "types": ["SSG", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68868.jpg"
    },
    {
        "name": "최준호",
        "types": ["두산", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53259.jpg"
    },
    {
        "name": "최지강",
        "types": ["두산", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52206.jpg"
    },
    {
        "name": "최지광",
        "types": ["삼성", "투수", "2017년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/67421.jpg"
    },
    {
        "name": "최지민",
        "types": ["기아", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52639.jpg"
    },
    {
        "name": "최지웅",
        "types": ["기아", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54611.jpg"
    },
    {
        "name": "최지훈",
        "types": ["SSG", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50854.jpg"
    },
    {
        "name": "최채흥",
        "types": ["삼성", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68419.jpg"
    },
    {
        "name": "최충연",
        "types": ["삼성", "투수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66451.jpg"
    },
    {
        "name": "최하늘",
        "types": ["삼성", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68501.jpg"
    },
    {
        "name": "최항",
        "types": ["롯데", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62884.jpg"
    },
    {
        "name": "최현석",
        "types": ["SSG", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54803.jpg"
    },
    {
        "name": "최형우",
        "types": ["기아", "외야수", "2002년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/72443.jpg"
    },
    {
        "name": "추신수",
        "types": ["SSG", "외야수", "2000년 데뷔(MLB), KBO은퇴"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51817.jpg"
    },
    {
        "name": "추재현",
        "types": ["롯데", "외야수", "2018년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "하영민",
        "types": ["키움", "투수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64350.jpg"
    },
    {
        "name": "하영진",
        "types": ["LG", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50107.jpg"
    },
    {
        "name": "하재훈",
        "types": ["SSG", "외야수", "2009년 데뷔(MiLB)"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69813.jpg"
    },
    {
        "name": "하주석",
        "types": ["한화", "내야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62700.jpg"
    },
    {
        "name": "하준영",
        "types": ["NC", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2023/68639.jpg"
    },
    {
        "name": "한경빈",
        "types": ["한화", "내야수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52710.jpg"
    },
    {
        "name": "한동희",
        "types": ["롯데", "내야수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68525.jpg"
    },
    {
        "name": "한두솔",
        "types": ["SSG", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68092.jpg"
    },
    {
        "name": "한석현",
        "types": ["NC", "외야수", "2014년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/64101.jpg"
    },
    {
        "name": "한승주",
        "types": ["한화", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50726.jpg"
    },
    {
        "name": "한승택",
        "types": ["기아", "포수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63722.jpg"
    },
    {
        "name": "한승혁",
        "types": ["한화", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61666.jpg"
    },
    {
        "name": "한유섬",
        "types": ["SSG", "외야수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62895.jpg"
    },
    {
        "name": "한재승",
        "types": ["NC", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51994.jpg"
    },
    {
        "name": "한재환",
        "types": ["NC", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50903.jpg"
    },
    {
        "name": "한준수",
        "types": ["기아", "포수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68646.jpg"
    },
    {
        "name": "한지웅",
        "types": ["KT", "투수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "한태양",
        "types": ["롯데", "내야수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "한현희",
        "types": ["롯데", "투수", "2012년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/62363.jpg"
    },
    {
        "name": "함덕주",
        "types": ["LG", "투수", "2013년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/63248.jpg"
    },
    {
        "name": "함창건",
        "types": ["LG", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50108.jpg"
    },
    {
        "name": "허경민",
        "types": ["두산", "내야수", "2009년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/79240.jpg"
    },
    {
        "name": "허관회",
        "types": ["한화", "포수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69706.jpg"
    },
    {
        "name": "허용주",
        "types": ["LG", "투수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53102.jpg"
    },
    {
        "name": "허윤동",
        "types": ["삼성", "투수", "2020년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "허인서",
        "types": ["한화", "포수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "허준혁",
        "types": ["LG", "투수", "2022년 데뷔"],
        "image_url": "default.png"
    },
    {
        "name": "허진",
        "types": ["SSG", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54813.jpg"
    },
    {
        "name": "현도훈",
        "types": ["롯데", "투수", "2018년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/68260.jpg"
    },
    {
        "name": "현원회",
        "types": ["SSG", "포수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50840.jpg"
    },
    {
        "name": "홍건희",
        "types": ["두산", "투수", "2011년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/61643.jpg"
    },
    {
        "name": "홍무원",
        "types": ["삼성", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51462.jpg"
    },
    {
        "name": "홍민기",
        "types": ["롯데", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50596.jpg"
    },
    {
        "name": "홍성호",
        "types": ["두산", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66233.jpg"
    },
    {
        "name": "홍승원",
        "types": ["삼성", "투수", "2021년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/51408.jpg"
    },
    {
        "name": "홍원빈",
        "types": ["기아", "투수", "2019년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/69643.jpg"
    },
    {
        "name": "홍원표",
        "types": ["삼성", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50430.jpg"
    },
    {
        "name": "홍유원",
        "types": ["NC", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54902.jpg"
    },
    {
        "name": "홍정우",
        "types": ["삼성", "투수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65496.jpg"
    },
    {
        "name": "홍종표",
        "types": ["기아", "내야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50600.jpg"
    },
    {
        "name": "홍창기",
        "types": ["LG", "외야수", "2016년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/66108.jpg"
    },
    {
        "name": "황대인",
        "types": ["기아", "내야수", "2015년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/65610.jpg"
    },
    {
        "name": "황동재",
        "types": ["삼성", "투수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50441.jpg"
    },
    {
        "name": "황동하",
        "types": ["기아", "투수", "2022년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/52641.jpg"
    },
    {
        "name": "황성빈",
        "types": ["롯데", "외야수", "2020년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/50500.jpg"
    },
    {
        "name": "황영묵",
        "types": ["한화", "내야수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54795.jpg"
    },
    {
        "name": "황의준",
        "types": ["KT", "외야수", "2023년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/53003.jpg"
    },
    {
        "name": "황재균",
        "types": ["KT", "내야수", "2006년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/76313.jpg"
    },
    {
        "name": "황준서",
        "types": ["한화", "투수", "2024년 데뷔"],
        "image_url": "https://lgcxydabfbch3774324.cdn.ntruss.com/KBO_IMAGE/person/middle/2024/54729.jpg"
    }
]

player = initial_players

data = load_data()

if "players" not in st.session_state:
    st.session_state.players = data



search_query = st.text_input('KBO 선수 검색')


team_options = st.multiselect('선수 팀 선택', ['기아', '삼성', 'LG', '두산', 'KT', 'SSG', '롯데', '한화', 'NC', '키움'])

options = st.multiselect('선수 포지션 선택', ['투수', '포수', '내야수', '외야수'])


if st.button('검색'):
    if not team_options and not options:  
        st.warning("검색하려면 최소한 두개 이상의 필터를 선택해야 합니다.")
    else:
        with st.spinner('검색 중...'):
            filtered_players = st.session_state.players.copy()
            if search_query:
                filtered_players = [player for player in filtered_players if search_query in player['name']]
            if options:
                filtered_players = [player for player in filtered_players if any(option in player['types'] for option in options)]
            if team_options:
                filtered_players = [player for player in filtered_players if player['types'][0] in team_options]

        filtered_players = [
            player for player in filtered_players
            if (not options or any(option in player['types'] for option in options)) and
            (not team_options or player['types'][0] in team_options)
            ]

    
        if filtered_players:
            st.write("### 검색 결과")
            st.write(f"조건에 부합하는 선수: **{len(filtered_players)}명**")
            st.warning("선수의 소속 팀이 없을 경우 데이터가 나오지 않을 수 있습니다.")
            st.text("일부 선수는 이미지가 없을 수 있습니다. (현 상무 소속 선수들 등등)")
            st.text("현재 소속 팀 기준입니다!")

            for i in range(0, len(filtered_players), 2):
                row_players = filtered_players[i:i+2]
                cols = st.columns(2)
                for j, col in enumerate(cols):
                    if j < len(row_players):
                        player = row_players[j]
                        with col:
                            st.image(player['image_url'], use_column_width=False)
                            st.subheader(player['name'])
                            st.text(f"정보: {' / '.join(player['types'])}") 
        else:
            st.warning("해당 선수 없음")


sorted_players = sorted(st.session_state.players, key=lambda x: x['name'])  
for i in range(0, len(sorted_players), 4):
    row_players = sorted_players[i:i + 4]  
    cols = st.columns(4)  
    for j in range(len(row_players)):
        with cols[j]:
            player = row_players[j]
            with st.expander(label=f"**{player['name']}**", expanded=True):
                st.image(player["image_url"], use_column_width=True)
