import pytube 
from pytube import YouTube
import os
yt = YouTube(str(input('URL do vídeo: ')))
###### Extraindo áudio ######   
video = yt.streams.filter(only_audio=True).first()
###### Salvando no diretório ######
print('Qual destino? (/var/www/python-world/mp3player/download)')
destination = str(input(">> "))
###### Saída ######
saida = video.download(output_path=destination)
###### Salvando... ######
base, ext = os.path.splitext(saida)
novo = base + '.mp3'
os.rename(saida, novo)
###### Sucesso ######
print(yt.title + ' Sucesso! Baixado...')