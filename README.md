
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

| company         | title                                   | originallink      | link              | description             | pubDate          |
|----------------|-----------------------------------------|-------------------|-------------------|--------------------------|-------------------|
| 디에스아키종합건설 | [18일 낙찰/계약 동향] 송산초등학교 공기... | fintechpost.co.kr | fintechpost.co.kr | 비산2동 행정복지센터 건립... | Wed, 18 Mar 2020 |
| 더샵스토리       | 메이플 챌린저스 월드, 250레벨 누구나 하루... | gameple.co.kr     | gameple.co.kr     | 여름 대규모 업데이트와 함... | Mon, 16 Jun 2025 |
| 에스오에이치     | ㈜엘지엠, 전기차 메카 제주(우도)서 전기선... | bizn.donga.com    | n.news.naver.com  | 제주도- 우도 유람이 가능한... | Wed, 23 Aug 2017 |

---

## 📌 Notes | 참고 사항

- The input file must contain a column labeled `담당` and `기업명`.
- API call delay (`time.sleep(1)`) helps prevent request throttling.

입력 파일에는 `담당`, `기업명` 열이 반드시 포함되어야 합니다. 또한 API 요청 속도 제한을 피하기 위해 `1초 대기` 로직이 포함되어 있습니다.

---

## 📮 Contact | 문의

For issues or feature requests, please open a GitHub issue or contact the maintainer.

이슈나 요청사항은 GitHub Issue로 등록해 주세요.
