import sounddevice as sd
import sys
import numpy as np
from scipy.io.wavfile import write
import requests
import json
from threading import Thread
 
sp = 16000 #samplerate

ANS = 0

def translate(d) :
    value = {
        "ศูนย์" : 0 ,"ซูน" : 0,"หนึ่ง" : 1,"นึง" : 1,"นึ่ง" : 1,"หนึง" : 1,
        "ซอง" : 2,"สอง" : 2,"ยี่" : 2,"ซ่อง" : 2,"สาม" : 3,"ซาม" : 3,"สี่" : 4,"ซี่" : 4,
        "ห้า" : 5,"หก" : 6,"เจ็ด" : 7,"แปด" : 8,"เก้า" : 9,"เก่า" : 9,"สิบ" : 10,"ร้อย" : 100,
        "รอย" : 100 ,"ลอย" : 100,"ล้อย" : 100,"พัน" : 1000,"หมื่น" : 10000,"แสน" : 100000 ,"ล้าน" : 1000000,"ลาน" : 1000000,
        "ต่อ" : "NEXT" ,"คับ" : "NEXT", "ย้อน" : "PREVIOUS" , "หน้า" : "MENU" , "จริง" : "T" , "เท็จ" : "F" , "TEST" : "F" , "T" : "T",
        "F" : "F" , "ทรู" : "T" , "ฟอ" : "F"
    }
    try :
        trans = value[d]
    except :
        trans = 0
    return trans

def main(time_limit) :

    sec = time_limit #1 digit for 2 minutes

    global ANS
    ANS = 0

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

    data = data.split(" ")
    
    digit = 0

    first = True
    
    for d in data:


        num = translate(d)

        print(num)

        if type(num) == str :
            ANS = num
            return 0
        if num > 9 : #10 1000 100000
            if first :
                digit = digit + num
                ANS += digit
                digit = 0
                first = False
            else :
                digit = digit * num
        elif num <= 9 and num >= 0 :
            digit = digit + num
            if first :
                first = False
            else :
                ANS += digit
                digit = 0


