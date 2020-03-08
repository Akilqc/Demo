import speech_recognition as sr


def reco(rate=16000):  # 固定采样率
    r = sr.Recognizer()
    with sr.Microphone(sample_rate = rate) as source:
        # r.adjust_for_ambient_noise(source, duration = 0.5)
        print('开始录音！')
        audio = r.listen(source)
    # 将录音转为wav文件
    with open(r'D:\Code\Demo\VS_Code\Speech-Recognition\RecordingFile\recording.wav', 'wb') as f:
        f.write(audio.get_wav_data())