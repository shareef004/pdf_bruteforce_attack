import PyPDF2 as pd
__banner__ = """
       +=======================================+
       |..........PDF  Cracker v 0.0.1.........|
       +---------------------------------------+
       |#Author: Devoloper.embuy <Shareef Ansari>             
       |#Contact: https://php-co.blogspot.com  |              
       |#Date: Thu jun 4 1:15:49 2020          |
       |#This tool is made zip pwd crack       |
       |#Changing the description of this tool |
       |Won't made you the coder ^_^ !!!       |
       |#Respect Coders ^_^                    |
       |#I take no responsibilities for the    |
       |  use of this program !                |
       +=======================================+
       |..........PDF Cracker v 0.0.1..........|
       +---------------------------------------+
"""

filename = input('Path of pdf file: ')
passlist = input('path of passlist file:') 
file = open(filename, 'rb')
pdfReader = pd.PdfFileReader(file)

tried = 0

if not pdfReader.isEncrypted:
    print('Your PDF file does not Contain a Password you can Easily open')

     
else:
    wordListFile = open(passlist, 'r')
    body = wordListFile.read().lower()
    words = body.split('\n')

    for i in range(len(words)):
        word = words[i]
        print('Trying {}'.format(word))
        result = pdfReader.decrypt(word)
        if result == 1:
            print(__banner__ +'\n[-]#####Password Cracked Successfully P#####\n[-]The password is: ' + word)
            break

        elif result == 0:
            tried += 1
            print('Passwords failed: ' + str(tried))
            continue
            


