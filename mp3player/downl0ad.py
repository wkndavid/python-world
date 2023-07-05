import pytube from YouTube
import os
yt = YouTube(str('URL do vídeo: '))
###### Extraindo áudio ######
video = yt.streams.filter(only.audio=tTrue).first()
###### Salvando no diretório ######
print('Qual destino? (/var/www/python-world/mp3player/download)')
destination = str(input(">> "))
###### Saída ######
saida = video.download(output_path=destination)
