!pip install librosa

import librosa
ses = '01-01-01-01-01-01-01.wav'
x,sr = librosa.load(ses)

print("x type:", type(x),"sr type",type(sr))

x#ses zaman serisi

sr#ses frekansi(Hz)

x.shape

#x,sr = librosa.load(ses,sr =11025)

import IPython.display as ipd
ipd.Audio(ses)
ipd.Audio(x,rate=sr)#bu sekilde oynatiyor

import matplotlib.pyplot as plt
import librosa.display
plt.figure(figsize=(10,2))
librosa.display.waveplot(x,sr=sr)

X = librosa.stft(x) #stft -> Short-time Fourier transform yani ses sinyali islemek icin bir arac. zaman ve frekansa gire karmasik genligi belirten zaman frekansi dagilimini anlatir

Xdb = librosa.amplitude_to_db(abs(X)) #Genlikten desibel degerine

plt.figure(figsize=(20,8))
librosa.display.specshow(Xdb,sr=sr,x_axis="time",y_axis="hz")
plt.colorbar()

mfkk = librosa.feature.mfcc(x,sr=sr)
print(mfkk.shape)

plt.figure(figsize=(15,6))
librosa.display.specshow(mfkk,x_axis='s')
plt.colorbar()
