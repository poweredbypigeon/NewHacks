# Note: you need to be using OpenAI Python v0.27.0 for the code below to work
import whisper


model = whisper.load_model('base')
result = model.transcribe('video_sound.mp3')

with open('transcript.txt', 'w') as f:
    f.write(result["text"])