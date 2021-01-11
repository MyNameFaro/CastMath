import sounddevice as sd
import sys
import numpy as np
from scipy.io.wavfile import write
import requests
import json
from threading import Thread
 
sp = 16000 #samplerate
sec = 5 #Seconds

convert = True 

def speech_to_text() :
    print("จะเริ่มละนะ")
    while convert :
        record = sd.rec(sec * sp, samplerate=sp, channels=1,dtype='int16') #voice
        sd.wait()
        #set wav format
        write('temp/voice.wav', sp, record)

        #To AI for thai

        url = "https://api.aiforthai.in.th/partii-webapi"
        files = {'wavfile': ('temp/voice.wav',open('temp/voice.wav', 'rb'),'audio/wav')}
        headers = {
            'Apikey': "PQ8mSRxPfybvxr7rWyfpRa36y0GkAu7l",
            'Cache-Control': "no-cache",
            'Connection': "keep-alive",
        }
        param = {"outputlevel":"--uttlevel","outputformat":"--txt"}
        response = requests.request("POST", url, headers=headers, files=files, data=param)
        data = json.loads(response.text)
        data = data["message"]
        #data = data.split(" ")
        #data = data[0]
        if data == "หยุด" :
            covert = False
            print("หยุดแล้ว")
            sys.exit()
        print(data)


Thread(target=speech_to_text).start()

