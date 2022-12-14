# Target
- AI와 데이터 분석에 관심있고 배우고 싶어하는 중고등학생 대상
- 컴퓨터과학 또는 데이터과학 분야 전공이 아닌 성인 대상

# Objectives
- AI 개발에서 데이터 분석의 중요성 파악
- 데이터 분석 과정 습득
- 데이터 분석에 필요한 기본적, 필수적인 통계학 학습
- 여러가지 종류의 시각화 기법을 사용하여 코드 없이 시각화 자료를 통해 데이터 분석 방법 학습

# DA Procedures
1. Intro: Review, Overview
2. Concept
3. Examples
4. Quizzes
5. Practice
6. Challenge

# Units
**Unit 1**
- Intro
    - *데이터, 정보란 무엇인가?*
    - 데이터 분석이란, 데이터분석과 AI간의 관계, 주변에서 찾아볼 수 있는 AI의 예시
        - Netflix 관련 자료들:
            - [데이터 시각화 (설명 영문)](https://www.kaggle.com/code/gabrielko/beginners-guide-netflix-visualization-eda)
            - [추천 시스템 (코드 有, 설명 영문)](https://www.kaggle.com/code/sujalbhagathansda/netflix-recommendation-system/notebook)
            - [추천 시스템 (코드 無, 짧은 동영상 포함, 영문)](https://recoai.net/netflix-recommendation-system-how-it-works/)
        - *데이터분석과 AI의 역사? 중요한 학문으로 자리잡게 된 계기?*
    - 데이터 분석과 통계
    - Check
        - *AI 또는 데이터분석을 활용하지 않은 선택지를 골라봅시다*
        - *데이터분석에 사용되는 통계학 개념과 아닌 것을 분류해 봅시다*
- 데이터 분석 과정
    - 문제 정의: *어떠한 문제를 언제, 어떠한 방식으로 정의하고 제기하여야 하는지?*
    - 데이터 수집: *데이터 수집 방법 제시 - 직접 조사, 인터넷 활용, kaggle 등*
    - 데이터 전처리: *중요성, 필요성*
    - 탐색적 데이터분석 (Exploratory DA, EDA)
        - 시각화 포함, 가설 無, 크기가 큰 데이터, 빅데이터에 주로 활용
    - *확증적 데이터분석 (Confirmatory DA, CDA)*
        - [CDA](https://www.insilicogen.com/blog/361)
        - 가설 有, 통계적인 분석 필요, 분석 내용에 기반하여 가설 확인
    - 리포팅
    - Check
        - *데이터 분석 과정을 순서에 맞게 나열해 봅시다*
- 데이터 분류
    - 정형 (Structured)
        - 이해, 분석, 구별하기 쉬움
        - 기업에서 새로운 제품을 개발, 전환할 때 많이 사용함
        - 머신러닝과 AI 개발 및 활용에 용이함
        - 감정, 구체적인 이유나 근거, 음악, 영상 나타낼 수 없음
    - *비정형 (Unstructured)*
        - 논리적으로 저장할 수 없음, 대부분의 현대 데이터들은 비정형 데이터 형식
        - 대부분의 프로그램, 데이터 분석, 머신러닝, AI 등에서 사용하기 까다로움
        - 영상, 음악, 리포트, 주관적 설문조사, 워드 파일, 이미지, 메모 등 해당됨
    - *반정형 (Semi-structured)*
        - JSON, zip, XML, 이메일, 웹 파일, 바이너리 파일 등
        - 대부분의 프로그램에서 사용하기 까다로움
        - 특정 분석기법과 프로그램 통하여 분석 가능
    - 수치형 (Numerical)
        - 연속형: 키, 몸무게, 시간, 매출액 등
        - 이산형: 교통사고 건수, 판매 수량, 불량품 수 등
    - 범주형 (Categorical)
        - 순위형: 순위/순서가 **있음** (i.e. 선호도/만족도, 별점)
        - 명목형: 순위/순서가 **없음** (i.e. 혈액형, 성별, 지역)
- 분산과 표준편차 (Variance & Standard Deviation)
    - 분산 (Variance)
        - [분산](https://www.investopedia.com/terms/v/variance.asp)
        - 각 값이 전체 값들의 평균에서 얼마만큼 떨어져 있는지를 나타낸 값, $\sigma^2$
        - 단점: 이상치, 극단치의 값도 반영됨
    - 표준편차 (Standard Deviation)
        - [표준편차](https://www.investopedia.com/ask/answers/021915/how-standard-deviation-used-determine-risk.asp)
        - 분산의 제곱근, $\sigma$
        - 분산은 표준화된 수치를 나타내지만, 표준편차는 원본 데이터의 단위로 각 값이 평균에서 얼마만큼 떨어져 있는지를 나타내기 때문에 직관적으로 한번에 이해하기 쉬움
- Challenge
    - EDA:
        1. 조사한 데이터에 기반하여 질문/이슈를 생각하기
        2. 1번에서 생각한 질문/이슈를 답변/해결하기 위해 데이터 시각화, 변환, 모델링 기법을 사용
        3. 2번의 결과를 바탕으로 새로운 질문/이슈를 생각해보고 의문점이 완전히 해소되고 주제가 명확히 잡힐 때까지 1~3번 프로세스 반복

**Unit 2**
- Intro
    - Review & Overview
- 데이터 시각화
    - 좋은 예, 안 좋은 예
    - Check
        - *색깔과 레이블이 맞지 않는 그래프*
        - *데이터 종류에 맞지 않는 시각화 (파이 그래프)*
    - *용도, 중요성, 필요한 이유*
    - *잘못 활용되었을 때의 리스크, 시각화 도구 결정 전에 고려해야할 점*
- 그래프 구성요소
    - 축, 범례
    - *옵션: 타이틀, 색, 격자 등*
    - Check
        - *각 축에 어떠한 변수가 알맞는지 옮겨보기, 범례를 보고 어떤 색이 어떤 종류의 데이터인지 맞추기*
- 막대 그래프
    - 작성 방법: 수직/수평 막대 그래프, 각 막대 그래프의 장단점
    - *어떠한 종류의 데이터에 막대 그래프를 사용하면 좋은지*
    - Check
        - *막대 그래프와 아닌 것 구별하기*
    - Exercise 1: 어떤 대푯값을 사용할까? (휴대폰 생산자별 판매량)
        - *데이터 제공 후 살펴본 뒤 대푯값 결정 (객관식 또는 빈칸 채우기)*
    - Exercise 2: 어떤 데이터를 X축과 Y축에 놓아야 할까?
        - *각 축에 변수 이름을 옮겨와서 직접 막대 그래프 완성해보기*
- 누적 막대 그래프
    - 특징, 사용 시기, 활용도가 높은 데이터 유형 소개
    - 작성 방법: 수직/수평 누적 막대 그래프
    - Check
        - *데이터를 보여주고 일반 막대 그래프와 누적 막대 그래프를 비교하여 어떤 것이 나을 지 판단하기*
    - Exercise 1: 어떤 대푯값을 사용할까? (성별 제품 선택 이유)
        - *데이터 제공 후 살펴본 뒤 대푯값 결정 (객관식 또는 빈칸 채우기)*
    - Exercise 2: 어떤 데이터를 X축과 Y축에 놓아야 할까?
        - *각 축에 변수 이름을 옮겨와서 직접 막대 그래프 완성해보기*
- 원 그래프
    - 특징, 사용 시기, 활용도가 높은 데이터 유형 소개
    - 막대 그래프와 차이점, 비교했을 때 장단점
    - 작성 방법: X축에 범주형, Y축에 수치형
    - Check
        - *원 그래프와 원 그래프가 아닌 것 (도넛, explode가 적용된 원 그래프, waffle 차트)*
    - Exercise
        - 
- Plot vs. Bar
- Exercise, Challenge

**Unit 3**
- Intro
    - Review & Overview
- Relationships between data
    - Dependent/Independent variables
    - Check
- Scatterplot (visualization)
- Scatterplot usage
    - Correlation Analysis
    - Clustering
    - Check
- Boxplot
    - Interpretation
    - Detecting outliers
    - Check
- Handling NaNs, outliers, etc.
- *Possible useful visualization types*
    - [Data Visualization types](https://visme.co/blog/data-visualization-types/)
- Exercise, Challenge

**Unit 4**
- Project 1, 2, 3
    - Collect data, Preprocess, EDA, Reporting

# Quiz (Check) Types
- 분류: O 또는 X 자리로 맞게 옮겨봅시다.
- 빈칸 채우기: 빈칸과 같이 코드 제공. 빈칸에 알맞은 내용 옮겨서 채우기.
- 선택(객관식): 코드 보여주고 실행했을 때 결과 예측하여 맞추기.

# Challenge 진행방법
- Step으로 나누어서 진행?
- 

$$
(1500 + 1550 + ... + 1800 + 1800)~/~7 \approx 1680
$$

$$
중앙값 = \frac{(총~행의~개수 + 1)}{2}번째~값
$$