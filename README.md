
# 🔍 Naver News Crawler for Assigned Companies (기업 뉴스 수집기)

## 📂 Project Description | 프로젝트 설명

This project automatically collects the latest Naver News articles related to a list of Korean companies assigned to 담당 6. It uses the Naver Search Open API and processes data from a CSV file (`enterprise_df_10k_utf8_data.csv`).

이 프로젝트는 '담당'이 6번으로 지정된 한국 기업들에 대한 네이버 뉴스 기사를 자동으로 수집합니다. 네이버 오픈 API를 활용하며, 입력 데이터는 `enterprise_df_10k_utf8_data.csv` 파일에서 불러옵니다.

---

## 🛠 Features | 주요 기능

- ✅ Filter companies by 담당 = 6
- ✅ Query news from Naver Search API
- ✅ Clean HTML tags from titles/descriptions
- ✅ Save results in CSV format (UTF-8-SIG)
- ✅ Avoid API rate limits using delay

---

## 📁 Files | 파일 구성

- `thang.py` : Main Python script to run the news crawler.
- `enterprise_df_10k_utf8_data.csv` : Company data including 담당 field.
- `naver_news_담당6_YYYYMMDD_HHMMSS.csv` : Output file with collected news articles.

---

## ⚙️ How to Use | 사용 방법

### 1. Requirements | 필요한 패키지

```bash
pip install pandas requests
```

### 2. Add Your API Keys | 네이버 API 키 입력

Edit `thang.py`:

```python
client_id = "YOUR_NAVER_CLIENT_ID"
client_secret = "YOUR_NAVER_CLIENT_SECRET"
```

### 3. Run the Script | 스크립트 실행

```bash
python thang.py
```

Output will be saved as:

```bash
naver_news_담당6_YYYYMMDD_HHMMSS.csv
```

---

## 📊 Sample Output | 출력 예시

| company         | title                                               | originallink                                                | link                                                        | description                                                                                                         | pubDate                        |
|----------------|-----------------------------------------------------|-------------------------------------------------------------|-------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|--------------------------------|
| 디에스아키종합건설 | [18일 낙찰/계약 동향] 송산초등학교 공기청정기 임차 및 유지관리 용역... | http://www.fintechpost.co.kr/news/articleView.html?idxno=105434 | http://www.fintechpost.co.kr/news/articleView.html?idxno=105434 | 비산2동 행정복지센터 건립공사 건축물 전과정 평가용역 계약을 수의계약 방식으로 주식회사 아키그린... | Wed, 18 Mar 2020 20:06:00 +0900 |
| 더샵스토리       | 메이플 챌린저스 월드, 250레벨 누구나 하루면 가능                       | https://www.gameple.co.kr/news/articleView.html?idxno=213291 | https://www.gameple.co.kr/news/articleView.html?idxno=213291 | 메이플스토리가 19일, 여름 대규모 업데이트와 함께 육성 전용 서버 '챌린저스 월드 시즌2'를 선보인다.... | Mon, 16 Jun 2025 23:00:00 +0900 |
| 에스오에이치     | ㈜엘지엠, 전기차 메카 제주(우도)서 전기선박 사업 시동                   | http://bizn.donga.com/3/all/20170823/85953119/2               | https://n.news.naver.com/mnews/article/020/0003089189?sid=101 | 에스오에이치 현 대표는 “이번 체험사업을 끝으로 제주도- 우도 유람이 가능한 마리나 사업을 본격적으로... | Wed, 23 Aug 2017 17:09:00 +0900 |

---

## 📌 Notes | 참고 사항

- The input file must contain a column labeled `담당` and `기업명`.
- API call delay (`time.sleep(1)`) helps prevent request throttling.

입력 파일에는 `담당`, `기업명` 열이 반드시 포함되어야 합니다. 또한 API 요청 속도 제한을 피하기 위해 `1초 대기` 로직이 포함되어 있습니다.

---

## 📮 Contact | 문의

For issues or feature requests, please open a GitHub issue or contact the maintainer.

이슈나 요청사항은 GitHub Issue로 등록해 주세요.
