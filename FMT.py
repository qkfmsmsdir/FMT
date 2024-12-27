import streamlit as st
import pandas as pd

# 제목 및 설명
st.title("🛐 신앙성숙도 검사 프로그램")
st.write("""
문장을 읽고 나의 신앙을 설명하는 정도를 선택하세요. 1: 매우 그렇지 않다 ~ 5:매우 그렇다
""")

# 문항 텍스트
QUESTIONS_TEXT = {
    1: "나는 종교적 신념과 가치가 다른 사람들과도 좋은 관계를 유지하려고 노력한다.",
    2: "나는 말씀을 듣고 믿지만 일상생활에 적용하지는 않는다.",
    3: "나는 예수님의 가르침이 우리들을 새롭게 변화시킬 수 있는 신비한 능력이 있다고 확신한다.",
    4: "교회에서 예배드리는 것은 내 삶의 중요한 부분을 차지한다.",
    5: "나는 다른 사람을 돕는데 시간이나 돈을 투자한다.",
    6: "나는 다른 사람과의 관계에서 하나님의 임재하심을 느낀다.",
    7: "선포된 말씀은 내 삶의 방향을 결정하는 가장 중요한 요인이다.",
    8: "나는 정기적으로 성경을 읽고 연구하는 시간을 갖는다.",
    9: "전반적으로 볼 때 현재 하나님과 나와의 관계는 살아있고 성장하고 있다고 말할 수 있다.",
    10: "나는 다른 사람들에게 칭찬이나 인정받는 것을 기대하지 않고 봉사한다.",
    11: "나는 그리스도인으로서 다른 사람과 교제하는 법에 익숙하다.",
    12: "나는 모든 사람들의 삶은 죄에 묶여있고, 그것을 치유할 수 있는 것은 오직 예수님뿐이라는 사실을 누구에게도 자신 있게 선포할 수 있다.",
    13: "내게 당장 도움이나 이익이 되더라도 신앙의 원칙에서 벗어난다면 포기해 왔고 앞으로도 그럴 것이다.",
    14: "내가 보기에 사람들을 예배에 출석시키는 가장 중요한 동기는 의무감이다.",
    15: "나는 섬김과 봉사 활동을 통해서 살아계시는 하나님의 손길을 경험하곤 한다.",
    16: "나는 내가 속한 소그룹의 분명한 사역의 방향과 목표를 알고 있다.",
    17: "나는 사랑이 많으신 하나님께서 이 세계에 왜 그렇게 많은 고통을 허락하시는지 이해하지 못한다.",
    18: "나는 가르침을 받은 대로 교회뿐만 아니라 가정과 사회에서도 그리스도인으로서 책임감 있게 살아가고 있다.",
    19: "나에게 있어서 예배는 하나님의 임재를 경험하는 가장 강력한 수단이다.",
    20: "나는 구원을 받기 위해서는 더 많은 섬김과 봉사를 해야 한다고 생각한다.",
    21: "하나님께서 교회를 세워나가시는데 있어서 나를 도구로 사용하고 계심을 경험한다.",
    22: "나는 복음의 핵심 내용을 명확히 알고 제시할 수 있다.",
    23: "나는 예수님의 가르침이 시대에 뒤떨어진다고 가끔 생각한다.",
    24: "나는 공적인 예배뿐만 아니라 개인적으로 정기적인 기도와 예배를 드린다.",
    25: "나는 하나님 앞에 연약하고 병든 자들을 향한 긍휼의 삶을 보여줄 책임이 있다고 믿는다.",
    26: "나는 소그룹 모임을 통해서 삶이 변화되는 신비한 경험이 가능함을 믿고 있으며, 실제로 그런 경험이 있다.",
    27: "나는 내가 누구인지, 어디에서 와서 어디로 가는지 잘 모르겠다.",
    28: "나는 다른 사람의 신앙을 세우는 일에는 적극적으로 관여하고 싶지 않다.",
    29: "나는 일의 결과에 대하여 하나님께 감사하며 영광을 돌리는 일이 익숙하다.",
    30: "나는 다른 사람을 섬기는 일을 할 때 그리스도인이라는 사실에 대하여 더욱 자긍심을 느낀다.",
    31: "나는 하나님과 깊은 관계를 형성하는 법을 잘 모른다.",
    32: "예수님을 전하고 싶은 마음은 나의 대인관계를 통하여 드러난다.",
    33: "나는 예수님의 가르침과 일치하는 신념과 가치를 가진 사람들에게 가장 많은 영향을 받는다.",
    34: "나는 기도제목에 대한 하나님의 무응답에 대해서 나름의 신앙적인 해답을 가지고 있다.",
    35: "나는 상처 입은 사람들을 예수님의 사랑으로 위로하는 일에 익숙하다.",
    36: "내가 하나님의 존재를 느끼는데 다른 사람과의 관계는 전혀 도움이 되지 않는다.",
    37: "나는 하나님의 말씀대로 살아가면 좋은 일들이 일어남을 경험하곤 한다.",
    38: "나는 영적 성장을 위한 배움의 기회가 있으면 적극적으로 참여하려고 한다.",
    39: "나는 일상의 삶에서 하나님을 예배하는 예배자라는 사실을 기억하며 살고 있다.",
    40: "내 인생의 가장 중요한 목표는 예수님의 희생적인 섬김의 사랑을 닮는 것이다.",
    41: "나는 소그룹모임을 통해 그리스도인됨이 얼마나 소중한지를 경험한다.",
    42: "나는 복음이 지닌 신비한 능력을 확신하며 경험하고 있다.",
    43: "교회에서 이루어지는 다양한 형태의 가르침은 내 삶의 지표 역할을 한다.",
    44: "나는 하나님이 내 삶의 가장 어둡고 어려운 때를 당신과 더 가까워지는 기회로 삼으심을 믿는다.",
    45: "나는 세상의 빛과 소금의 역할을 하며 살기 어려울 것 같다."
}

# 🗂️ 하위요소 분류

# 신앙성숙도 하위요소
MATURITY_CATEGORIES = {
    "코이노니아": [1, 6, 11, 16, 21, 26, 31, 36, 41],
    "케리그마": [2, 7, 12, 17, 22, 27, 32, 37, 42],
    "디다케": [3, 8, 13, 18, 23, 28, 33, 38, 43],
    "레이투르기아": [4, 9, 14, 19, 24, 29, 34, 39, 44],
    "디아코니아": [5, 10, 15, 20, 25, 30, 35, 40, 45],
}

MATURITY_DESCRIPTIONS = {
    "코이노니아": "공동체 안에서의 나눔과 친교를 의미합니다.",
    "케리그마": "복음을 선포하고 전파하는 것을 의미합니다.",
    "디다케": "가르침과 교육을 통해 신앙을 성장시키는 것을 의미합니다.",
    "레이투르기아": "예배와 경배를 통해 하나님과 교제하는 것을 의미합니다.",
    "디아코니아": "섬김과 봉사를 통해 신앙을 실천하는 것을 의미합니다."
}

# 신앙생활 하위요소
LIFESTYLE_CATEGORIES = {
    "인지적 신앙생활": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 23],
    "정의적 신앙생활": [1, 18, 19, 20, 21, 22, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35],
    "의지적 신앙생활": [14, 15, 16, 17],
}

LIFESTYLE_DESCRIPTIONS = {
    "인지적 신앙생활": "신앙에 대한 이해와 지식을 바탕으로 신앙을 실천합니다.",
    "정의적 신앙생활": "감정과 공감을 통해 신앙의 가치를 경험합니다.",
    "의지적 신앙생활": "신앙의 결단과 실천을 통해 행동으로 나아갑니다."
}

# 역채점 문항
REVERSE_QUESTIONS = [2, 14, 17, 20, 23, 27, 28, 31, 36, 45]

# 사용자 응답 받기
responses = {}
st.subheader("📋 문항 응답")

for i in range(1, 46):
    # 문항과 라디오 버튼을 하나의 블록으로 통합
    responses[i] = st.radio(
        f" {i}. {QUESTIONS_TEXT.get(i, f'문항 {i}')}",
        options=[1, 2, 3, 4, 5],
        index=None,  # 초기 선택 없음
        horizontal=True,
        key=f"question_{i}"
    )
# 📝 제출 버튼
if st.button("제출하기"):
    # 모든 문항이 응답되었는지 확인
    if any(response is None for response in responses.values()):
        st.error("❗ 모든 문항에 반드시 답변해야 합니다.")
    else:
        # 🧠 하위요소별 점수 계산
        def calculate_scores(categories):
            scores = {}
            for category, items in categories.items():
                score = 0
                for item in items:
                    if item in REVERSE_QUESTIONS:
                        score += (6 - responses[item])  # 역채점
                    else:
                        score += responses[item]
                scores[category] = score
            return scores

        # 신앙성숙도 점수 계산
        maturity_scores = calculate_scores(MATURITY_CATEGORIES)
        # 신앙생활 점수 계산
        lifestyle_scores = calculate_scores(LIFESTYLE_CATEGORIES)

        # 결과 표시
        st.subheader("📝 검사 결과")

        st.write("### 📊 신앙성숙도 하위요소별 점수")
        for category, score in maturity_scores.items():
            st.write(f"**{category}:** {score}점 - {MATURITY_DESCRIPTIONS[category]}")
        st.bar_chart(pd.DataFrame.from_dict(maturity_scores, orient='index', columns=['점수']))

        st.write("### 📊 신앙생활 하위요소별 점수")
        for category, score in lifestyle_scores.items():
            st.write(f"**{category}:** {score}점 - {LIFESTYLE_DESCRIPTIONS[category]}")
        st.bar_chart(pd.DataFrame.from_dict(lifestyle_scores, orient='index', columns=['점수']))
