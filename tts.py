import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voices', voices[0].id)
vol = engine.getProperty('volume')
engine.setProperty('volume', vol+0.5)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate+20)
all_text = ''
with open("all.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
      line = line.strip().replace('\n', ' ') 
      all_text += line + ' '
print(all_text)
engine.say(all_text)
engine.save_to_file(all_text, './all.mp3')
engine.runAndWait()
engine.stop()