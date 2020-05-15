import re
import pyperclip


#Psate the text
bigString = pyperclip.paste()

#We go over the text and exstract the Telephon &Phone &emails numbers and adress
#to saprated lists (by type)

##compile the regexs
telPhoneReg = r"(0\d|0\d\d)[-\ ]{0,1}(\d{3})[-\ ]{0,1}(\d{4})"
telPhonReg_comp=re.compile(telPhoneReg)

emailReg = r"\S+@\w+\.\w+"
emailReg_comp=re.compile(emailReg)

##exstract the requierd values 
bigList = telPhonReg_comp.findall(bigString)

allPhoneNum = []
for	groups	in	bigList:
    phonNum='-'.join([groups[0],groups[1],groups[2]])
    allPhoneNum.append(phonNum)
  
allPhoneNum = allPhoneNum + emailReg_comp.findall(bigString)
print(allPhoneNum)

#Compy nicly to clicboard
bigNewString = "\n".join(allPhoneNum)
pyperclip.copy(bigNewString)
















