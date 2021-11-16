import random


minusculo = 'abcdefghijklmnopqrstuvwxyz'
maiusculo = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'
simbolos = '[]{}#()*;._-'

all = minusculo + maiusculo + numeros + simbolos
length = 22

password = ''.join (random.sample(all,length))
print ('\033[1;32;40mSua senha gerada é: %s\033[m' % password)
