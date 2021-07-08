from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
url = 'https://api.us-south.text-to-speech.watson.cloud.ibm.com/instances/f97ac3c4-fc3b-4b3e-9487-b0d89e11e4b5'
apikey = 'ezTC8JPerwC2DCCKBnz9O7CMf128OBBgJTqvLrar7oZY'
 
    
def main():


    authenticator = IAMAuthenticator(apikey)

    text_2_speech = TextToSpeechV1(authenticator=authenticator)

    text_2_speech.set_service_url(url)

    with open('text.txt', 'r') as f:
        text = f.read()

    with open('Voice.mp3', 'wb') as audio_file:
        r = text_2_speech.synthesize(text, accept='audio/mp3',voice='en-US_AllisonV3Voice').get_result()
        audio_file.write(r.content)

if __name__ == "__main__":
    main()
