import requests
import urllib.parse
import json
import pandas as pd
import re
from datetime import datetime
import time

# CSV 파일 로드 (동일 디렉토리에 있어야 함)
df = pd.read_csv("enterprise_df_10k_utf8_data.csv")  # 경로 수정 가능

# '담당'이 6번인 기업 리스트 추출
company_list = df[df['담당'] == '6번']['기업명'].dropna().tolist()

# API 인증 정보
client_id = "JvIG9LnXxkLyb5Cysjwo"
client_secret = "dGy7jCjQtK"

# 결과 저장용 리스트
all_news = []

# 기업별 뉴스 수집
for idx, company in enumerate(company_list, start=1):
    print(f"[{idx}/{len(company_list)}] ⏳ Searching news for: {company}")
    
    # 검색어 인코딩
    encoded_query = urllib.parse.quote(company)
    url = f"https://openapi.naver.com/v1/search/news.json?query={encoded_query}&display=10&start=1&sort=sim"

    # API 헤더
    headers = {
        "X-Naver-Client-Id": client_id,
        "X-Naver-Client-Secret": client_secret,
        "User-Agent": "Mozilla/5.0"
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            items = json.loads(response.text)["items"]
            for item in items:
                title = re.sub(r"<.*?>", "", item["title"])
                desc = re.sub(r"<.*?>", "", item["description"])
                all_news.append({
                    "company": company,
                    "title": title,
                    'originallink': item['originallink'],
                    "link": item["link"],
                    "description": desc,
                    "pubDate": item["pubDate"]
                })
            print(f"✅ {company}: {len(items)} news found.")
        else:
            print(f"❌ {company}: API Error {response.status_code} - {response.text}")
        time.sleep(1)  # 요청 간격 1초 (Rate limit 방지)
    except Exception as e:
        print(f"⚠️ Exception for {company}: {e}")

# 데이터프레임으로 변환 후 저장
df_news = pd.DataFrame(all_news)
current_time = datetime.now().strftime("%Y%m%d_%H%M%S")
output_file = f"naver_news_담당6_{current_time}.csv"
df_news.to_csv(output_file, index=False, encoding="utf-8-sig")

print(f"\n🎉 완료! 총 {len(df_news)}건 뉴스가 수집되어 저장되었습니다: {output_file}")
