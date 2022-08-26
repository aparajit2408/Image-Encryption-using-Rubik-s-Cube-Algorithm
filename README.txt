To run the project, you require Python 3.8, and a reputed IDE for Python, such as PyCharm.

The Python libraries to be installed are PIL (for image processing), random 
(for random number generation), numpy (for shuffling and user defined functions),
and json. Make sure the versions are up to date.

To run the project, change the path given in lines 10 and 91 for the encrypt file, and 
lines 6 and 74 for the decrypt file to the file path saved on the local directory.

In order to run the project with a custom input, add the desired picture to the project folder,
and reference it the image.open command by entering the correct file path of the photo.

To encrypt an image, reference the image in line 10 of the encrypt code, and choose the desired
output name for the picture along with the path in line 91.
To view the encrypted picture, simply open the new png file generated in the location given by
the user. To decrypt the image, reference the encrypted image in line 6 of the decrypt code,
select the desired path and file name of the decrypted file and run the decrypt code.
To view the decrypted picture, simply open the new png file generated in the location given by the user.

To view the keys generated KC and KR, open the txt files KC.txt and KR.txt.