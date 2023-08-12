# write a program for a validation eligibility of the student for USA unvirsity addmission
""" consider
		system should take the following input
			name 
			
"""

import os
import sys

name  = input(" please input name ")
passport = input(" please input what is your passport ")
Score = float(input(" please input what is your Score "))
gradation_state = input(" please input what is your Score ")

if (name == "" or passport == "" or Score is None or gradation_state == ""):
    print( " YOU HAVE GIVEN A NULL DETAILS")
else:
    print( "congratualition you can apply")