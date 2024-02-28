from flask import Flask, render_template, request, send_from_directory
import edge_tts
import asyncio
import os

app = Flask(__name__)
voice = 'zh-CN-YunjianNeural'
volume = '+0%'
rate = '-4%'
text = 'default_text'
output = 'static\demo.mp3'

async def save_voice(text, voice, rate, volume, output):
    tts = edge_tts.Communicate(text = text,voice = voice,rate = rate,volume=volume)
    await tts.save(output)

@app.route('/')
def home():
    message_content = "Please upload a file."
    return render_template('upload.html', message_content=message_content)

@app.route('/button-clicked', methods=['GET', 'POST'])
def button_clicked():
    if request.method == 'POST':
        selected_option = request.form.get('dropdown', 'default_option')
        voice = selected_option
        volume_value = int(request.form.get('volume', '0'))
        volume = f"+{volume_value}%" if volume_value >= 0 else f"{volume_value}%"
        rate_value = int(request.form.get('rate', '0'))
        rate = f"+{rate_value}%" if rate_value >= 0 else f"{rate_value}%"
        
        text = ""
        # for each .txt file in the uploads folder, read the text
        for filename in os.listdir('uploads'):
            if filename.endswith('.txt'):
                with open(f'uploads/{filename}', 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    for line in lines:
                        line = line.strip().replace('\n', ' ') 
                        text += line + ' '
            
            output = f'static/{filename}.mp3'

            asyncio.run(save_voice(text, voice, rate, volume, output))

            text = ""

        message_content = f"音色: {voice}, 音量: {volume}, 语速: {rate}, 文件已生成."
    else:
        message_content = "Method Not Allowed"

    return render_template('upload.html', message_content=message_content)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file and file.filename.endswith('.txt'):
        filename = file.filename
        file.save(os.path.join('uploads', filename))
        message_content = 'File has been uploaded and renamed to text.txt'
    else:
        message_content = 'Invalid file type, please upload a .txt file.'

    return render_template('upload.html', message_content=message_content)

if __name__ == '__main__':
    app.run(debug=True)
