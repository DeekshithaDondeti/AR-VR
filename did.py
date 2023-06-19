import speech_recognition as sr
import openai
import requests, json, time
import sys

openai.api_key="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"

def record_audio():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Recording...")
        audio = r.listen(source)

    try:
        text = r.recognize_google(audio)
        print("Recognized text:", text)
    except sr.UnknownValueError:
        print("Speech recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service:", str(e))
        
    return text

def chatgpt_api(input_text):
    messages = [
    {"role": "system", "content": "You are a helpful assistant."}]

    if input_text:
        messages.append(
            {"role": "user", "content": input_text},
        )
        chat_completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo", messages=messages
        )

    reply = chat_completion.choices[0].message.content
    return reply

x=record_audio()
y=chatgpt_api(x)


def did(out_result):
    url = 'https://api.d-id.com/talks'
    api_key = 'c2hyZXlhY2hhbGxhZ3VsbGE2Nzg5QGdtYWlsLmNvbQ:xFejhaSSAFOh2QSaUqTRC'
    headers = {
        'Authorization': 'Basic ' + api_key,
        'Content-Type': 'application/json'
    }

    payload = {
        "source_url": "https://create-images-results.d-id.com/DefaultPresenters/Noelle_f/image.jpeg",
        "script": {
            "type": "text",
            "input": out_result,
            "provider":{
                "type": "microsoft",
                "voice_id":"en-US-DavisNeural",
                "voice_config":{
                    "style":"Cheerful"
                }
            }
        }
    }

    json_payload = json.dumps(payload)
    response = requests.post(url, data=json_payload, headers=headers)

    d = response.json()
    # print(d)
    ids = d['id']
    newurl = url +"/"+ ids
    finalresponse = requests.get(newurl,headers=headers)
    smo = finalresponse.json()
    # print(finalresponse)
    # audio = requests.get(smo[])
    return smo['audio_url']

print(did(y))

# input = sys.argv[1]
output = did(y)
sys.stdout.flush()
