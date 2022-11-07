import speech_recognition as sr
from gtts import gTTS
from playsound import playsound
import os

# 음성 인식 (듣기):
def listen(recognizer, audio):
    try:
        text = recognizer.recognize_google(audio, language = 'ko')
        print('[나도코딩] ' + text)
    except sr.UnknownValueError:
        print('인식 실패')
    except sr.RequestError as e:
        print('요청 실패 : {0}'.format(e))

# 대답
def answer(input_text):
    answer_text = ''
    if '안녕' in input_text:
        answer_text = '안녕하세요? 반갑습니다.'
    elif '날씨' in input_text:
        answer_text = '오늘의 서울 기온은 20도입니다. 맑은 하늘이 예상됩니다.'
    elif '환율' in input_text:
        answer_text = '원 달러 환율은 1380원입니다.'
    elif '고마워' in input_text:
        answer_text = '별 말씀을요.'
    elif '종료' in input_text:
        answer_text = '다음에 또 만나요'
        stop_listening(wait_for_stop = False)
    else:
        answer_text = '다시 한 번 말씀해주시겠어요?'

    speak(answer_text)

# 소리내어 읽기 (TTS):
def speak(text):
    print('[인공지능] ' + text)
    file_name = 'voice.mp3'
    tts = gTTS(text = text, lang = 'ko')
    tts.save(file_name)
    playsound(file_name)
    if os.path.exists(file_name):
        os.remove(file_name)

r = sr.Recognizer()
m = sr.Microphone()

speak('무엇을 도와드릴까요?')
stop_listening = r.listen_in_background(m, listen)
# stop_listening(wait_for_stop = False) # 더 이상 듣지 않음

while True:
    time.sleep(0.1)
