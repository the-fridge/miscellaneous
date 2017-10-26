# this programm takes a source file of which you have to provide the path to
# it finds all the words in the file strips the file of them and puts them back in
# but in a completly random order
# braces stay in their places also everything which isn't a word
# it returns the result in a .txt file, that has otherwise the same name as the source file
# used on a pythonsode-file the result can be quite funny


# to make it work i had to take the backrefs folder out of the original directory and into the same directory as this .py file
# probably unnecessary but I don't know how to improve on it right now ( 27.10.2017 )
from backrefs import bre
#https://github.com/facelessuser/sublime-backrefs
import codecs
from random import random
import os


def findWords( text ) :
    words = [ ]
    indices = [ ]

    iterator = bre.finditer( "\p{L}+", text )

    for index in iterator :
        indices.append( index.span( ) )

    for word in indices :
        words.append( text[ word[ 0 ] : word[ 1 ] ] )

    return words, indices


def mixer( wList, iList, text) :
    parts = len( wList )
    vorlage = text
    text = ""
    l = len( iList )

    while parts > 0 :
        ran = int( random( ) * parts )

        if l == parts :
            text = wList[ ran ] + vorlage[ iList[ parts - 1 ][ 1 ] : ]
        else :
            text = wList[ ran ] + vorlage[ iList[ parts - 1 ][ 1 ] : iList[ parts ][ 0 ] ] + text
            
        del wList[ ran ]
        parts -= 1

    text = vorlage[ : iList[ parts ][ 0 ] ] + text
    
    return text


def main( ):
    path = input( "Dateipfad: " )
    
    if os.path.isfile( path ) == True :
        print( path, " existiert." )
        
        file = codecs.open( path, "r", "utf-8" )
        text = file.read( )
        file.close( )

        fileName, fileExtension = os.path.splitext( path )
        
        fileName = path[ : -( len( fileExtension ) ) ] + " mix.txt"
        file = open( fileName, "w" )
        
        words = findWords( text )[ 0 ]
        indices = findWords( text )[ 1 ]
        
        file.write( mixer( words, indices, text) )
        file.close( )

        print( "Erfolgreich abgeschlossen" )
        
    else :
        print( path, " existiert nicht." )
        
    print( )
    input( "Drücke Enter zum Verlassen" )


main( )
