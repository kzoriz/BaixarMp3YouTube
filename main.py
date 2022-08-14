from pytube import YouTube
from moviepy import editor as mp
import re
import os

try:
    #Digite o link do video e o local que deseja salvar o mp3
    link = input("Digite o link do video que deseja salvar: \n")
    path = input("Digite o nome do Diretorio ou tecle Enter: \n")
    if path == '':
        path = "Musicas"
    yt = YouTube(link)
    #Começa o Download
    print("Baixando...")
    ys = yt.streams.filter(only_audio=True).first().download(path)
    print("Download Completo!")

    # Converter mp4 para mp3
    for file in os.listdir(path):
        if re.search('mp4', file):
            mp4_path = os.path.join(path, file)
            mp3_path = os.path.join(path, os.path.splitext(file)[0]+'.mp3')
            new_file = mp.AudioFileClip(mp4_path)
            new_file.write_audiofile(mp3_path)
            os.remove(mp4_path)
    print("Sucesso!")
except Exception:
    print("Algo deu errado!")
    print("-------------------------------")
    print("Verifique o link do video\n"
          "Verifique o nome do diretorio")
    print("-------------------------------")