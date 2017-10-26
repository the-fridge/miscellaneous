from backrefs import bre
#https://github.com/facelessuser/sublime-backrefs/blob/master/readme.md
import codecs
from random import random
import os


def findWords(text):
    words=[]
    indices=[]

    iterator=bre.finditer("\p{L}+",text)

    for index in iterator:
        indices.append(index.span())

    for word in indices:
        words.append(text[word[0]:word[1]])

    return words, indices


def mixer(wList, iList,text):
    parts = len(wList)
    vorlage=text
    text=""
    l=len(iList)

    while parts!=0:
        ran=int(random()*parts)

        if l==parts:
            text= wList[ran]+vorlage[iList[parts-1][1]:]
        else:
            text= wList[ran]+vorlage[iList[parts-1][1]:iList[parts][0]]+text
            
        del wList[ran]
        parts-=1

    text= vorlage[:iList[parts][0]]+text
    
    return text


def main():
    path=input("Dateipfad: ")
    
    if os.path.isfile(path) == True:
        print(path, " existiert.")
        
        file=codecs.open(path,"r","utf-8")
        text=file.read()
        file.close()

        fileName, fileExtension = os.path.splitext(path)
        
        fileName=path[:-(len(fileExtension))]+" mix.txt"
        file=open(fileName,"w")
        
        words=findWords(text)[0]
        indices=findWords(text)[1]
        
        file.write(mixer(words,indices,text))
        file.close()

        print("Erfolgreich abgeschlossen")
        
    else:
        print(path, " existiert nicht.")
        
    print()
    input("Drücke Enter zum Verlassen")


main()
