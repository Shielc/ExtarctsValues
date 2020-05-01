import re
import pyperclip


#Psate the text
bigString = pyperclip.paste()

 
#We go over the text and exstract the Telephon &Phone &emails numbers and adress
#to saprated lists (by type)

#TODO make the regex more acurate
#to not extract emails with @@, emails with another words bedor and after (אביב־יפוShirel123@12gmail.com)
#to continue the dibag

##compile the regexs
telPhonReg =r"0\d-\d{7}|0\d\d{7}|0\d\d-\d{7}|0\d\d\d{7}|0\d\d-\d{3}-\d{4}|0\d-\d{3}-\d{4}"
telPhonReg_comp=re.compile(telPhonReg)

phonReg =r"0\d{2}-\d{7}|0\d{2}\d{7}"
phonReg_comp=re.compile(phonReg)

emailReg = r"\S+@\w+\.\w+"
emailReg_comp=re.compile(emailReg)


##exstract the requierd values 
bigList = telPhonReg_comp.findall(bigString)
bigList = bigList + phonReg_comp.findall(bigString)
bigList = bigList + emailReg_comp.findall(bigString)
print(bigList)

#Compy nicly to clicboard
bigNewString = "\n".join(bigList)
pyperclip.copy(bigNewString)
















