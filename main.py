import os
import eyed3
import shutil

ipod_drive = "E:"

iploc = ipod_drive+"/iPod_Control/Music"
files = os.listdir(iploc)

try:
    os.mkdir("songs")
except:
    idk=""

def remove_symbol(text):
    stopwords = ['\\','/',':','*','?','"','<','>','|']
    for i in range(len(stopwords)):
        text = text.replace(stopwords[i],"")
    if(text[-1] == " "):
        text = text[:-1]
    return text


def formating(title,artist,file):
    ntitle = remove_symbol(title)
    nartist = remove_symbol(artist)

    formats = file.split(".")
    nfile = nartist + " - " + ntitle + "." + formats[1]
    return nfile

for i in range(len(files)):
    if("._" not in files[i]):
        songs = os.listdir(iploc+"/"+files[i])
        print(files[i])
        for a in range(len(songs)):
            audio = eyed3.load("{}/{}/{}".format(iploc,files[i],songs[a]))
            try:
                print("|--"+audio.tag.title)
                shutil.copy("{}/{}/{}".format(iploc,files[i],songs[a]), "./songs/"+formating(audio.tag.title,audio.tag.artist,songs[a]))
            except:
                print("|--"+songs[a])
                shutil.copy("{}/{}/{}".format(iploc,files[i],songs[a]), "./songs/"+songs[a])


