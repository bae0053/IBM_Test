import json
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('gB_xUdK025vo_Wa7-vKlDu38TbjG257m88qDNP_txY-p')
language_translator = LanguageTranslatorV3(
    version='2018-05-01',
    authenticator=authenticator
)

language_translator.set_service_url('https://api.kr-seo.language-translator.watson.cloud.ibm.com/instances/3bea0c22-2fe0-409c-8b91-eff613ddf055')

# 입력한 Txt 
'''translation = language_translator.translate(
    text='Hello, how are you today?',
    model_id='en-ko').get_result()
print(json.dumps(translation, indent=2, ensure_ascii=False))'''

# pdf 파일을 번역하는 코드
with open('test2.pdf','rb') as file : 
    result = language_translator.translate_document(
        file = file,
        file_content_type='application/pdf',
        filename='test2.pdf',
        model_id='en-ko'
    ).get_result()

print(json.dumps(result, indent=2))


# 위에 코드를 먼저 실행하여 Document_id를 얻은 후에 아래의 코드를 실행해야함.
with open('translated.pdf', 'wb') as f:
    result = language_translator.get_translated_document(
        document_id='9f0d1cc6-65c4-4a74-95d8-896d49a47655',
        accept='application/pdf').get_result()
    f.write(result.content)