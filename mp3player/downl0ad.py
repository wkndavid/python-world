import pytube from YouTube
import os
yt = YouTube(str('URL do vídeo: '))
###### Extraindo áudio ######
video = yt.streams.filter(only.audio=tTrue).first()
