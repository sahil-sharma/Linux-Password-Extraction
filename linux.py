#!/usr/bin/python

# Author : Sahil Sharma


import os,sys
import crypt
import codecs
import argparse

def testPass(cryptPass,user):
 
    strfile = raw_input ("Please enter the dictionary file path = ")
    dictfile = open (strfile, 'r')
    ctype = cryptPass.split("$")[1]
 
    if ctype == '6':
        print "[+] Hash found is SHA-512 ..."
        print "[+] Processing ..."
        salt = cryptPass.split("$")[2]
        insalt = "$" + ctype + "$" + salt + "$"
        for word in dictfile.readlines():
            word=word.strip('\n')
            cryptWord = crypt.crypt(word,insalt)
            if (cryptWord == cryptPass):
                
                print "[+] Found password for the user: " + user + " ====> " + word + "\n"
                return
        else:
        	print "Sorry, nothing found."
        	exit
        	
        	
def main():
	 parse = argparse.ArgumentParser(description = 'A simple brute force /etc/shadow .')
	 parse.add_argument('-f', action='store', dest='path', help='Path to shadow file, example: \'/etc/shadow\'')
	 argus=parse.parse_args()
	 if argus.path == None:
	 	parse.print_help()
	 	exit
	 else:
	 	passFile = open (argus.path,'r')
	 	for line in passFile.readlines():
	 		line = line.replace("\n","").split(":")
	 		if  not line[1] in [ 'x', '*','!' ]:
				user = line[0]
		                cryptPass = line[1]
		                testPass(cryptPass,user)

if __name__=="__main__":
	main()
