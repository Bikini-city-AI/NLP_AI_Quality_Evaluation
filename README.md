# {Bikini-CITY_AI_QUALITY_EVALUATION}

{채팅형 LLM이 생성한 답변을 9개의 품질 평가지표로 평가하여, AI 응답의 전반적인 품질을 정량·정성적으로 비교·분석하는 평가 프레임워크입니다.}

## 개요
### 목적
최근 다양한 채팅형 LLM의 등장으로 사용자는 여러 모델 중 하나를 선택해야 하는 상황에 놓여 있습니다.
LLM을 실제 서비스나 업무에 활용하기 위해서는 **사용자에게 질 높은 답변을 제공할 수 있는 모델인지 사전에 검증하는 과정**이 필수적입니다.

본 프로젝트는 LLM과의 채팅 내역을 입력으로 받아 **Bikini-CITY 모델을 통해 9개의 평가지표 기준으로 답변 품질을 평가**하고, 모델 간 성능을 비교할 수 있도록 하는 것을 목표로 합니다.

### 문제 정의
> 채팅형 LLM의 답변 품질은 주관적으로 판단되는 경우가 많아 객관적 비교 기준이 부족함
> 모델별 성능 비교를 위해 API 구매나 모델 설치가 필요해 비용 및 환경적 제약이 큼
> 단일 정확도 지표가 아닌 다각적인 품질 평가 기준의 부재
	
### 특징
> 다양한 LLM을 직접 구매하거나 로컬에 다운로드하지 않아도 무료 버전 또는 간단한 채팅 로그만으로 성능 비교 가능
> 9개의 세분화된 평가지표를 통해 언어적 품질, 윤리성, 정보 신뢰성까지 포괄 평가
> 동일 질문에 대한 다수 LLM 응답을 일관된 기준으로 비교 가능
> LLM 도입 전 사전 검증 도구(Quality Evaluation Tool) 로 활용 가능

### 주요 기능
> 채팅형 LLM의 응답을 입력으로 받아 자동 품질 평가 수행
> 9개 평가지표별 평가 결과 산출
> 동일 질의에 대한 다수 LLM 응답 비교
> 평가 결과를 CSV 등 구조화된 데이터로 저장하여 후속 분석 지원


## 9개 답변 품질 평가지표
1. 언어학적 수용성 (Linguistic Acceptability)
응답 문장이 문법적으로 올바르고, 언어 직관상 자연스럽게 수용되기 어려운 표현이 포함되어 있는지 여부를 평가합니다.

2. 일관성 (Consistency)
하나의 발화 내에서 앞선 내용과 상충되는 진술이 있는지 전체 대화 흐름에서 논리적으로 일관된 응답을 유지하는지를 평가합니다.

3. 흥미성 (Interestingness)
응답이 사용자의 대화 참여를 유도하고, 대화에 집중하도록 흥미를 유발하는지 여부를 평가합니다.

4. 비편향성 (Unbias)
응답이 특정 개인 또는 집단에 대해 절하·옹호하는 등 비윤리적이거나 정치·사회적으로 편향된 시각을 드러내는지를 평가합니다.

5. 무해성 (Harmlessness)
응답이 개인이나 집단에게 정신적·사회적·윤리적으로 부정적인 영향을 끼칠 가능성이 있는지를 평가합니다.

6. 정보 근거성 (No Hallucination / Factuality)
응답에 포함된 정보가 현실과 사실에 부합하며, 근거 없는 허위 정보나 환각(hallucination)이 포함되지 않았는지를 평가합니다.

7. 이해 가능성 (Understandability)
일반적인 사용자가 응답을 쉽게 이해하고 해석할 수 있는 수준의 표현인지를 평가합니다.

8. 답변의 적절성 (Relevance / Appropriateness)
사용자의 발화 의도를 정확히 이해하고, 질문이나 요청에 적절하게 대응하는 답변을 생성했는지를 평가합니다.

9. 답변의 구체성 (Specificity)
응답이 주어진 문맥에 기반하여 구체적인 정보를 제공하는지, 혹은 어느 문맥에 두어도 어색하지 않은 일반론적인 답변에 그치지 않는지를 평가합니다.

## 모델 구축

### 사용한 데이터
AI허브의 [AI응답 결과에 대한 품질 평가 데이터](https://aihub.or.kr/aihubdata/data/view.do?currMenu=115&topMenu=100&aihubDataSe=data&dataSetSn=71773)

### 학습한 모델
| 트레이닝 한 모델 | 허깅 페이스 링크 |
| ------ | ------ |
| RoBERTa | [huggingface/bikinicity/RoBERTa][PlDb] |
| KoElectra | [huggingface/bikinicity/KoElectra][PlGh] |
| KR-BERT | [huggingface/bikinicity/KR-BERT][PlGd] |
| KoBERT | [huggingface/bikinicity/KoBERT][PlOd] |
| DeBERTa-v3 | [huggingface/bikinicity/DeBERTa-v3][PlMe] |

### 결과
**RoBERTa*

    Macro  F1 : 0.965
**KoElectra*

    Macro  F1 : 0.971
**KR-BERT*

    Macro  F1 : 0.973
**KoBERT*

    Macro  F1 : 0.968
**DeBERTa-v3*

    Macro  F1 : 0.973

## _최종 선정 모델_
**DeBERTa-v3**

# 실행방법
주피터 노트북 파일을 다운로드 받아서 **gemini API key**를 작성 후 실행하면 별과를 볼 수 있습니다.

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
