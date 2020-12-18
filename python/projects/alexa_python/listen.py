import speech_recognition as sr

# obtain audio from the microphone

while True:
    r = sr.Recognizer()
    with sr.Microphone(device_index = 0, sample_rate = 44100, chunk_size = 512) as source:
        print("Say something!")
        r.adjust_for_ambient_noise(source=source)
        audio = r.listen(source, timeout=3)
    
    data = ''
    try:
        data = r.recognize_google(audio)
        print(data)
    except:
        pass


