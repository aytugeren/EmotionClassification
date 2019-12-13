import os,sys
import glob
from zipfile import ZipFile #To unzip all folders of dataset
from moviepy.editor import * #There are movies as mp4. We will change them .wav with this library

zip_files = glob.glob('/Users/aytug/Desktop/DataSets/V*.zip') #There are zip folders. You need to change direction of the folder to see zip folders

#For each zip files you need to change SpeechActor and SongActor
for i in zip_files:
    zip_file = os.path.splitext(i)[0] + '.zip'
    list = zip_file[33:]
    with ZipFile('/Users/aytug/Desktop/DataSets/'+list,'r') as zipObj:
        zipObj.extractall('/Users/aytug/Desktop/UnZipFolders/SpeechActor')
        
for i in range(1,25):#Architecture of folders are builted according to this loop Actor_01,Actor_02 ...
    if(i<10):
        directionSong = glob.glob('/Users/aytug/Desktop/UnZipFolders/SongActor/Actor_0'+str(i)+'/*.mp4')
        directionSpeech = glob.glob('/Users/aytug/Desktop/UnZipFolders/SpeechActor/Actor_0'+str(i)+'/*.mp4')
        for l in directionSong:
          directory = '/Users/aytug/Desktop/ConvertedFolder/SongActor/Actor_0'+str(i)
          files = os.path.splitext(l)[0] + '.mp4'
          video = VideoFileClip(os.path.join(files[:53] + '/',files[53:]))
          if not os.path.exists(directory):
                 os.makedirs(directory)
          video.audio.write_audiofile(os.path.join(directory+"/",files[53:73] + '.wav'))
        for l in directionSpeech:
          directory = '/Users/aytug/Desktop/ConvertedFolder/SpeechActor/Actor_0'+str(i)
          files = os.path.splitext(l)[0] + '.mp4'
          video = VideoFileClip(os.path.join(files[:55] + '/',files[55:]))
          if not os.path.exists(directory):
                os.makedirs(directory)
          video.audio.write_audiofile(os.path.join(directory+"/",files[55:75] + '.wav'))
    else:
       directionSong = glob.glob('/Users/aytug/Desktop/UnZipFolders/SongActor/Actor_'+str(i)+'/*.mp4')
       directionSpeech = glob.glob('/Users/aytug/Desktop/UnZipFolders/SpeechActor/Actor_'+str(i)+'/*.mp4')
       for l in directionSong:
          directory = '/Users/aytug/Desktop/ConvertedFolder/SongActor/Actor_'+str(i)
          files = os.path.splitext(l)[0] + '.mp4'
          video = VideoFileClip(os.path.join(files[:53] + '/',files[53:]))
          if not os.path.exists(directory):
                os.makedirs(directory)
          video.audio.write_audiofile(os.path.join(directory+"/",files[53:73] + '.wav'))
       for l in directionSpeech:
          directory = '/Users/aytug/Desktop/ConvertedFolder/SpeechActor/Actor_'+str(i)
          files = os.path.splitext(l)[0] + '.mp4'
          video = VideoFileClip(os.path.join(files[:55] + '/',files[55:]))
          if not os.path.exists(directory):
                os.makedirs(directory)
          video.audio.write_audiofile(os.path.join(directory+"/",files[55:75] + '.wav'))
