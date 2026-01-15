from google import genai  # import 방식 변경

import os

# API 키 설정
API_KEY = "AIzaSyB6qOuVbsdTtMTbquRoBuYiiuEz4PxCZBg"
client = genai.Client(api_key=API_KEY)  # Client 객체 생성 방식으로 변경

# 카테고리 목록
CATEGORIES = [
    "경제활동 · 상품 · 상거래",
    "기술 · 과학",
    "미용 · 관광 · 식음료",
    "엔터테이먼트 · 오락",
    "여행 · 여가 · 취미",
    "인문 · 사회",
    "주거 · 생활 · 사람관계"
]


def classify_text(text):
    """
    AI 답변을 Gemini API를 사용하여 카테고리로 분류합니다.
    """
    try:
        # 프롬프트 구성
        prompt = f"""다음 텍스트를 아래 7가지 카테고리 중 가장 적합한 하나로 분류해주세요.
반드시 카테고리 이름만 정확히 출력하고, 다른 설명은 추가하지 마세요.

카테고리 목록:
1. 경제활동 · 상품 · 상거래
2. 기술 · 과학
3. 미용 · 관광 · 식음료
4. 엔터테이먼트 · 오락
5. 여행 · 여가 · 취미
6. 인문 · 사회
7. 주거 · 생활 · 사람관계

분류할 텍스트:
{text}

가장 적합한 카테고리:"""

        # API 호출 방식 변경 (models.generate_content 사용)
        response = client.models.generate_content(
            model="gemini-2.5-flash-lite",  # 최신 모델 권장
            contents=prompt
        )

        category = response.text.strip()

        # 응답 확인 로직 (기존과 동일)
        if category in CATEGORIES:
            return category
        else:
            for cat in CATEGORIES:
                if cat in category or category in cat:
                    return cat
            return f"분류 실패: {category}"

    except Exception as e:
        return f"오류 발생: {str(e)}"


def classify_batch(texts):
    results = []
    for i, text in enumerate(texts):
        category = classify_text(text)
        results.append({
            "index": i,
            "text": text[:100] + "..." if len(text) > 100 else text,
            "category": category
        })
    return results


if __name__ == "__main__":
    print("분류할 텍스트를 입력하세요:")
    sample_text = input()

    print("=" * 60)
    print("단일 텍스트 분류 예시")
    print("=" * 60)
    print(f"텍스트: {sample_text}")
    print(f"분류 결과: {classify_text(sample_text)}")
    print()

    results = classify_batch(sample_text)
    for result in results:
        print(f"[{result['index'] + 1}] {result['text']}")
        print(f"    → 카테고리: {result['category']}\n")
