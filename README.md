# 소개
여러 Crew 내의 각 Chatbot에 역할, 목표, 배경을 부여하고,
각각의 연쇄 작용을 통해 원하는 결과를 도출

## 1. Stock crew
특정 회사의 주가 추이, 소득 명세서, 대차 대조표, 내부자 거래 내역과
최근 관련 뉴스 정보 등을 활용해 매수, 매도, 홀딩 추천

# Version
1. python 3.11.9 ( >= 3.10)
2. pip 24.1
3. crewai 0.1.7

# 사용법
1. **가상환경 생성** - python -m venv venv 
2. **가상환경 실행** - (windows cmd 기준) cd venv/Scripts -> activate.bat
3. **pip 다운로드** - cd ../.. 커맨드 실행해 root 폴더로 돌아온 후, pip install -r requirements.txt
4. **pip 다운로드2** - 위 방법이 안되면 수동 설치 -> pip install crewai crewai[tools] python-dotenv yfinance
5. **Api key 추가** - source 폴더에 '.env' 파일 생성 후 OPENAI_API-KEY='본인 api key' 추가
6. **gpt version 변경** - venv/crewai 폴더의 agent.py에서 'OPENAI_MODEL_NAME'를 검색해 gpt-4.0o version에서 gpt-3.5-turbo 로 변경
7. **실행** - __main__.py의 result에서 원하는 회사명을 추가한 뒤 실행