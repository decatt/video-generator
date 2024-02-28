from flask import Flask, render_template, request
import edge_tts
import asyncio

app = Flask(__name__)
voice = 'zh-CN-YunjianNeural'
volume = '+0%'
rate = '-4%'
text = 'default_text'
output = 'demo.mp3'

async def save_voice():
    tts = edge_tts.Communicate(text = text,voice = voice,rate = rate,volume=volume)
    await tts.save(output)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/button-clicked', methods=['GET', 'POST'])
def button_clicked():
    if request.method == 'POST':
        selected_option = request.form.get('dropdown', 'default_option')
        voice = selected_option
        volume_value = int(request.form.get('volume', '0'))
        volume = f"+{volume_value}%" if volume_value > 0 else f"{volume_value}%"
        rate_value = int(request.form.get('rate', '0'))
        rate = f"+{rate_value}%" if rate_value > 0 else f"{rate_value}%"
        text_value = request.form.get('textinput', 'default_text')
        text = text_value       

        asyncio.run(save_voice())

        return f"音色: {voice}, 音量: {volume}, 语速: {rate}, 文本: {text}"
    else:
        return "Method Not Allowed"



if __name__ == '__main__':
    app.run(debug=True)
