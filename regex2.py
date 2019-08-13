#! python3
import re, pyperclip
#create a regex for phone numbers
phoneRegex = re.compile(r''' 
#52 41 45 45 Ext. 2127
#(998) 8 81 01 00 Ext. 63904
#(81) 81 58 15 00 Ext. 1503
#83 54 83 48
( 
((\(\d\d\d\)) | (\(\d\d\)))? #area code (optional)
(\s) #Primer separador
(\d\s\d\d\s\d\d\s\d\d | \d\d\s\d\d\s\d\d\s\d\d) #Formato de numeros
((ext(\.)?\s |x) (\d{2,5}))?) #extension
'''
,re.VERBOSE)
#todo: create a regex for email addresses
emailRegex = re.compile(r''' 
[a-zA-Z0-9.+]+ #expresion que evalua si tiene letras o numeros
@ #expresion que evalua el @
[a-zA-Z0-9.+]+ 
'''
,re.VERBOSE)

text = pyperclip.paste()


extractedPhone = phoneRegex.findall(text)
extractedemail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(allPhoneNumbers)
print(extractedemail)

#todo: get the text off the clipboard
#todo: Extract the email / phone from this text
#todo: copy the extracted email / phone to the clipboard


