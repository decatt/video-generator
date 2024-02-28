import edge_tts
import asyncio
class MyTTS:
    def __init__(self, text_path, output_name, voice = 'zh-CN-YunjianNeural', rate = '-4%', volume = '+0%'):
        text = ""
        with open(text_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()
            for line in lines:
                line = line.strip().replace('\n', ' ') 
                text += line + ' '
        self.text = text
        self.voice = voice
        self.rate = rate
        self.volume = volume
        self.output = output_name+'.mp3'
      
    def set_rate(self, rate):
        self.rate = rate

    def set_volume(self, volume):
        self.volume = volume
    
    def set_voice(self, voice):
        self.voice = voice

    async def save_voice(self):
        tts = edge_tts.Communicate(text = self.text,voice = self.voice,rate = self.rate,volume=self.volume)
        await tts.save(self.output)

if __name__ == '__main__':
    my_tts = MyTTS('all.txt', 'demo')
    #save voice
    asyncio.run(my_tts.save_voice())
    print('done')