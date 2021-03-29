import json
from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

authenticator = IAMAuthenticator('ElyUdfUdF_Buwsh_cYoUgdcrOHl-rYsowwrW6wkOD33d')
text_to_speech = TextToSpeechV1(
    authenticator=authenticator
)


text_to_speech.set_service_url('https://api.kr-seo.text-to-speech.watson.cloud.ibm.com/instances/667c7efa-6b47-4282-87cf-0143e0d34598')

voice = text_to_speech.get_voice('en-US_AllisonV3Voice').get_result()

with open('holy moly.wav', 'wb') as audio_file:
    audio_file.write(
        text_to_speech.synthesize(
            '',
            voice='ja-JP_EmiV3Voice',
            accept='audio/wav'        
        ).get_result().content)