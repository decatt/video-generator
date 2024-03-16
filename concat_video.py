import ffmpeg


def generate_clip(image_path,audio_path):
    input_image = ffmpeg.input(image_path)
    input_audio = ffmpeg.input(audio_path)
    audio_length=ffmpeg.probe(audio_path)["format"]["duration"]
    input_image = input_image.filter("tpad",stop_duration=float(audio_length)-1.0/25,stop_mode="clone")
    return input_image,input_audio

def main():
    num_clips=3
    clips=[]
    for i in range(1,num_clips+1):
        clips.extend(generate_clip(f"{i}.png",f"{i}.mp3"))

    full_video=ffmpeg.concat(*clips, v=1, a=1)
    full_video.output("output.mp4").run(overwrite_output=True)

main()