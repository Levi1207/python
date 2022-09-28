from pyexpat import model
from pyexpat.errors import messages
from gtts import gTTS
import random
import time
import playsound
import speech_recognition as sr
import os
import pyautogui as pg





def listen_command ():
    #return input('Скажите вашу команду:')
    
    r = sr.Recognizer()
    with sr.Microphone() as source:
        
        say_message('Скажите вашу команду ')
        audio = r.listen(source)

        try:
            our_speech =r.recognize_google(audio, language='ru')
            print('Вы сказали:'+our_speech)
            return our_speech
        except sr.UnknownValueError:
            return 'ERROR'
        except sr.RequestError:
            return 'ERROR'    

def do_this_command(message):
    message = message.lower()
    if "Привет" in message:
        say_message('привет друг')
    elif 'пока' in message:
        say_message('Пока и удачи вам ')
        exit()
    elif 'как дела' in message:
        say_message('хорошо, спасибо ?')
    elif 'выключи компьютер' in messages:
        say_message('выключение компьютера')
        os.system('shutdown -s')
    else:
        say_message('Команда не распознано!')

def say_message(message):
    voice = gTTS(message,lang='ru')
    file_voice_name = '_audio_'+str(time.time())+'_'+str(random.randint(0,100000))+'.mp3'
    voice.save(file_voice_name)
    playsound.playsound(file_voice_name)
    print('Голосовой Ассистент  '+ message)

if __name__=='__main__':
    while True:
        command = listen_command()
        do_this_command(command)
        

