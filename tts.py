import edge_tts
import asyncio
TEXT = ""
with open("all.txt", 'r', encoding='utf-8') as f:
    lines = f.readlines()
    for line in lines:
      line = line.strip().replace('\n', ' ') 
      TEXT += line + ' '
print(TEXT)
voice = 'zh-CN-YunjianNeural'
output = 'demo.mp3'
rate = '-4%'
volume = '+0%'
async def my_function():
    tts = edge_tts.Communicate(text = TEXT,voice = voice,rate = rate,volume=volume)
    await tts.save(output)
if __name__ == '__main__':
    asyncio.run(my_function())