from PIL import Image
from random import randint
import numpy as np
import json

higher = (2**8) - 1
lower = 0
#print(higher, lower)

Image_input = Image.open("D:/Documents/Cyber Security J Component/Tushar-Photo.jpg");
kk, ht = Image_input.size
pxls = Image_input.load()
print(pxls[0,0])
contains_alpha = len(pxls[0,0]) == 4
#print(M, N)

filling = 1
a = [[filling for ttz in range(kk)] for kkm in range(ht)]

for kkm in range(ht):
    for ttz in range(kk):
        if contains_alpha:
            red, green, blue, a = pxls[ttz,kkm]
        else:
            red, green, blue = pxls[ttz,kkm]
        #lum = 255-red # Reversed luminosity
        a[kkm][ttz] = red # Map values from range 0-255 to 0-1

KR = []
KC = []

for p in range(ht):
    KR.insert(p, randint(lower, higher))

for p in range(kk):
    KC.insert(p, randint(lower, higher))

for p in range(ht):
    alpha = 0
    for rz in range(kk):
        alpha = ((alpha%2) + (a[p][rz] % 2)) % 2
    if(alpha == 0):
        for pq in range(KR[p]):
            temporary_var = a[p][kk-1]
            for mn in range(kk-1, -1, -1):
                a[p][mn] = a[p][mn-1];
            a[p][0] = temporary_var;
    else:
        for pq in range(KR[p]):
            temporary_var = a[p][0]
            for mn in range(kk-1):
                a[p][mn] = a[p][mn+1];
            a[p][kk-1] = temporary_var;

for rz in range(kk):
    beta = 0
    for p in range(ht):
        beta = ((beta%2) + (a[p][rz] % 2)) % 2
    if(beta == 0):
        for pq in range(KC[rz]):
            temporary_var = a[ht - 1][rz]
            for mn in range(ht-1, -1, -1):
                a[mn][rz] = a[mn-1][rz]
            a[0][rz] = temporary_var;
    else:
        for pq in range(KC[rz]):
            temporary_var = a[0][rz]
            for mn in range(ht-1):
                a[mn][rz] = a[mn+1][rz];
            a[ht-1][rz] = temporary_var;



for rz in range(kk):
    for p in range(ht):
        if((p%2) !=0 ):
            a[p][rz] = a[p][rz]^KC[rz]
        else:
            a[p][rz] = a[p][rz]^KC[kk-1-rz]


for p in range(ht):
    for rz in range(kk):
        if((rz%2) !=0 ):
            a[p][rz] = a[p][rz]^KR[p]
        else:
            a[p][rz] = a[p][rz]^KR[ht-1-p]

array1 = np.array(a, dtype=np.uint8)
gen_img = Image.fromarray(array1)
gen_img.save('D:/Documents/Cyber Security J Component/Tushar-encrypted.png')

with open("KR.txt", "w") as outfile:
    json.dump(KR, outfile)

with open("KC.txt", "w") as outfile:
    json.dump(KC, outfile)
