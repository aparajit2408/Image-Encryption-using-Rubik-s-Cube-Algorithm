from PIL import Image
from random import randint
import numpy as np
import json

input_img = Image.open("D:/Documents/Cyber Security J Component/Tushar-encrypted.png");
w, ht = input_img.size
pxls = input_img.load()

f = 1
array = [[f for tt in range(w)] for mm in range(ht)]

for mm in range(ht):
    for tt in range(w):
        #lum = 255 - pxls[tt,mm] # Reversed luminosity
        array[mm][tt] = pxls[tt,mm] # Map values from range 0-255 to 0-1

with open("KR.txt", "r") as infile:
    KR = json.load(infile)

with open("KC.txt", "r") as infile:
    KC = json.load(infile)

for pq in range(ht):
    for st in range(w):
        if((st%2) != 0):
            array[pq][st] = array[pq][st] ^ KR[pq]
        else:
            array[pq][st] = array[pq][st] ^ KR[ht - 1 - pq]

for st in range(w):
    for pq in range(ht):
        if((pq%2) != 0):
            array[pq][st] = array[pq][st] ^ KC[st];
        else:
            array[pq][st] = array[pq][st] ^ KC[w - 1 - st]

for st in range(w):
    bt = 0
    for pq in range(ht):
        bt = ((bt % 2) + (array[pq][st] % 2)) % 2
    if(bt == 0):
        for ttz in range(KC[st]):
            temporary_var = array[0][st]
            for l in range(ht - 1):
                array[l][st] = array[l+1][st]
            array[ht - 1][st] = temporary_var
    else:
        for ttz in range(KC[st]):
            temporary_var = array[ht - 1][st]
            for l in range(ht-1, -1, -1):
                array[l][st] = array[l-1][st]
            array[0][st] = temporary_var

for pq in range(ht):
    alfa = 0
    for st in range(w):
        alfa = ((alfa % 2) + (array[pq][st] % 2)) % 2
    if(alfa == 0):
        for ttz in range(KR[pq]):
            temporary_var = array[pq][0]
            for l in range(w - 1):
                array[pq][l] = array[pq][l+1]
            array[pq][w - 1] = temporary_var
    else:
        for ttz in range(KR[pq]):
            temporary_var = array[pq][w - 1]
            for l in range(w-1, -1, -1):
                array[pq][l] = array[pq][l-1]
            array[pq][0] = temporary_var   

arr = np.array(array, dtype=np.uint8)
gen_img = Image.fromarray(arr)
gen_img.save('D:/Documents/Cyber Security J Component/Tushar-decrypt.png')

               
