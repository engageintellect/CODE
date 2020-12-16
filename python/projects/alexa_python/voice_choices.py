import pyttsx3

engine = pyttsx3.init()
voices = engine.getProperty('voices')

for voice in voices:

  print("ID: %s" % voice.id)
  print("Name: %s" % voice.name)
  print("Age: %s" % voice.age)
  print("Gender: %s" % voice.gender)
  print("Languages Known: %s" % voice.languages)
  print('\n')

print(voices[16].id)
