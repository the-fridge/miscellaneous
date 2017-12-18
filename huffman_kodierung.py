# -*- coding: utf-8 -*-
"""
Created on Mon Dec 18 17:45:36 2017

@author: Jonas
"""
import math

text = input( 'Text: ' )
code = input( 'Code: ' ) # das ist ein Alphabet keine doppelten Buchstaben
letters = { }

for l in text:
    if l in letters:
        letters[ l ] += 1
    else:
        letters[ l ] = 1

tLetters = [ ]

for l in letters:
    tLetters.append( ( l, letters[ l ] ) )

# not mine
def bubble(bad_list):
    length = len(bad_list) - 1
    sorted = False

    while not sorted:
        sorted = True
        for i in range(length):
            if bad_list[i][1] > bad_list[i+1][1]:
                sorted = False
                bad_list[i], bad_list[i+1] = bad_list[i+1], bad_list[i]

bubble( tLetters )

def recTree( array, lenCode ):
    if( len( array ) > lenCode ):
        divArray = [ ]
        i = math.ceil( len( array ) / lenCode )
        c = -1
        while i > 0:
            j = [ ]
            for h in range( c + 1, lenCode + c + 1 ):
                if( h == len( array ) ):
                    break
                j.append( array[ h ] )
                c += 1
            divArray.append( j )
            i -= 1
        return recTree( divArray, lenCode )
    else:
        return array
    
tree = recTree( tLetters, len( code ) )
print( tree, '\n' )

def printTree( tree, code, depth = 0, path = '', dicTree = { } ):
    codeI = 0
    out = ''
    prePath = path
    for k in tree:
        path = prePath
        path += code[ codeI ]
        out += depth * '-' + code[ codeI ]
        if( type( k ) != tuple ):
            out += '\n'
            res = printTree( k, code, depth + 1, path, dicTree )
            out += res[ 0 ]
            dicTree.update( res[ 2 ] )
        else:
            out += ' ' + k[ 0 ] + '\n'
            dicTree[ k[ 0 ] ] = path
        codeI += 1
    return [ out, path, dicTree ]

re = printTree( tree, code )
print( re[ 0 ] )
print( re[ 2 ] )

def trans( dicTree, text ):
    out = ''
    for l in text:
        out += dicTree[ l ]
    return out

newText = trans( re[ 2 ], text )
print( newText )
    
with open( 'EntopyText.txt', 'w' ) as file:
    txt = '\n' + newText + '\n\nviel Spaß beim aufschlüsseln :)\n\n' + re[ 0 ]
    file.write( txt )
