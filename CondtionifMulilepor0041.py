#pan cards is mandatory DL or voter is used for address proof
import os
import sys


name  = input(" please input name ")
pancard = input(" please input what is your passport ")
inDriverLicence = input(" please input what is your Score ")
votercard = input(" please input what is your Score ")

if ((pancard == "Y" or pancard == "y") and (inDriverLicence == "Y" or inDriverLicence== "y") and ( votercard =="Y" or votercard =="y")):
    print( " YOU are eligabe")
else:
    print( " you cann ot apply")