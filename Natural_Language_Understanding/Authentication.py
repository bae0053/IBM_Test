import json
from ibm_watson import NaturalLanguageUnderstandingV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from ibm_watson.natural_language_understanding_v1 \
    import Features, EmotionOptions, ConceptsOptions, CategoriesOptions, EntitiesOptions, KeywordsOptions
    
# 서비스 시작이 얻는 API Key 입력
authenticator = IAMAuthenticator('Ad_Q-VvVr7jsg4Q-4Uxm6ZgBMEsay7-X9QovXDpo_q_F')
natural_language_understanding = NaturalLanguageUnderstandingV1(
    version='2020-08-01',          # API 문서 참조
    authenticator=authenticator
)


# 서비스 시작이 얻는 URL 입력
natural_language_understanding.set_service_url('https://api.kr-seo.natural-language-understanding.watson.cloud.ibm.com/instances/e9d7070c-b625-475a-b47c-7df4003b71f6')


# IBM Cloud API 문서 참고

# 카테고리 예제
# response = natural_language_understanding.analyze(
#     url='www.ibm.com',
#     features=Features(categories=CategoriesOptions(limit=3))
#     ).get_result()

# print(json.dumps(response, indent=2))

# 개념 분석 예제
# response = natural_language_understanding.analyze(
#     url='www.ibm.com',
#     features=Features(concepts=ConceptsOptions(limit=3))).get_result()

# print(json.dumps(response, indent=2))


# 감정 분석 예제
# 콘텐츠의 감정을 분석
# response = natural_language_understanding.analyze(
#     html="<html><head><title>Fruits</title></head><body><h1>Apples and Oranges</h1><p>I love apples! I don't like oranges.</p></body></html>",
#     features=Features(emotion=EmotionOptions(targets=['apples','oranges']))).get_result()

# print(json.dumps(response, indent=2))

# Entity 분석 예제
# 콘텐츠에서 사람, 도시, 조직과 같은 분류를 분석
# response = natural_language_understanding.analyze(
#     url='www.cnn.com',
#     features=Features(entities=EntitiesOptions(sentiment=True,limit=1))).get_result()

# print(json.dumps(response, indent=2))


# 키워드 분석 예제
# 콘텐츠에서 중요한 키워드를 분석
response = natural_language_understanding.analyze(
    url='www.ibm.com',
    features=Features(keywords=KeywordsOptions(sentiment=True,emotion=True,limit=2))).get_result()

print(json.dumps(response, indent=2))