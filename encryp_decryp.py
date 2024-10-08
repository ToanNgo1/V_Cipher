#!/usr/bin/env python3
# # -*- coding: utf-8 -*-
"""user input text encryption using Vignere Cipher """
__author__="Toan Ngo"
#prototype
#later this will become a files 
import string
letter=string.ascii_lowercase
#------------------------------------------------------------------------------------------------------------------------------------
def encry(message,key,mode):
    global letter
    message_container=[]
    keyindex=0                  #this will continute looping till the message reach it end 
    mode=mode
    if(mode=="decry"):
        try:
            rever="".join(chr(int(i,2))for i in message.split(" "))
            print(message)
            message=rever
        except ValueError:
            print("this message was never envrypt by this program exited binery converter")
    #loop for each character in the message 
    for element in message:
        #getting the first letter index in the root check
        try:
            num=letter.index(element.lower())
            #print(num,element)

            #getting the index in the main root letter with the combine of key index
            if(mode=="encry"): 
                num+=letter.index(key[keyindex])                                #the equation are f(C)=(C(original) +C(key)) mod 26
            elif(mode=="decry"):
                num-=letter.index(key[keyindex])                                #the equation are f(C)=(C(original) - C(key)) mod 26
            #mod the number with the lengh of the letter root
            num%=len(letter)
            #print(f"check {letter[num]}")

            #original type check
            if element.isupper():
                message_container.append(letter[num].upper())
            elif element.islower():
                message_container.append(letter[num])
            keyindex+=1

            #restart the loop key
            if keyindex==len(key):
                keyindex=0
            #else:
            #    print("this is check")
            #    message_container.append(element)
        except ValueError:              #if value not in the list of letter.
            message_container.append(element)

    print(f"this is your message after the progam:{"".join(message_container)}")       #one more change to the message 
    out_packet="".join(message_container)
    binery=" ".join(format(ord(i),"b")for i in out_packet)
    print(f"and this is binery of that: {binery}")
#--------------------------------------------------------------------------------------------------------
if __name__=="__main__":
    user_message=input("please enter your user message here: ")
    while True:
        try:
            user_select=input("please enter your your selected mode: encryption(encry) or decryption(decry):")
            if(user_select in ["encry","decry"]):
                break
            elif(user_select or user_message =="exit"):
                break
            else:
                print("that is not a valid input to be accepted, please only entering encry(encryption) or decry(decryption)")
                continue
        except Exception:
            print("something has when wrong")
    if(user_select=="encry"):
        user_key=input("please enter something to create a key for encryption(anything is fine as long it as its a letter)(for example: cat): ")
        encry(user_message,user_key,user_select)
        print(f"please keep this key for your encryption or decryption: {user_key}")
    elif(user_select=="decry"):
        user_key=input("please enter the key that was created by the process of your encryption: ")
        encry(user_message,user_key,user_select)
        print(f"please keep this key for your encryption or decryption: {user_key}")
    else:
        print("exit the program ")
