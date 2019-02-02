#-------------------------------------------------------------------------------
# Name:        PasswordClassGen
# Purpose:  Class Based Password Generator
#
# Author:      Layonthehorn
#
# Created:     12/30/2017
# Copyright:   None
# Licence:     None
#-------------------------------------------------------------------------------

import random, string

'''

make a password

1: call PassChecker
    newpassword = PassChecker()
2: run finalcheck with length of password
    newpassword.finalcheck(4)
3: save into new variable with 
    finalpassword = newpassword.password

'''


class RandomValue:

    def __init__(self):
        self.password = ''

    def generatepassworddigit(self): # defining a function
         return str(random.randrange(0,10)) # returns a random number of 0 to 9

    def generatepasswordUppercase(self): # defining a function
        return random.choice("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

    def generatepasswordLowercase(self): # defining a function

        return random.choice("abcdefghijklmnopqrstuvwxyz")

    def generateSpecialCharactors(self): # defining a function

        return random.choice("!@#$%?^&*")


class PassChecker(RandomValue):

    def passwordcheckersp(self,pword):
        special= string.punctuation
        specialchecker = -1
        for i in special:
            if pword.count(i)>0:
                specialchecker = 1

        return specialchecker

    def passwordcheckercap(self,pword):
        # 'QWERTYUIOPLKJHGFDSAZXCVBNM'
        cap = string.ascii_uppercase
        capchecker = -1
        for i in cap:
            if pword.count(i)>0:
                capchecker = 1

        return capchecker

    def passwordcheckerlow(self,pword):
        # 'qwertyuioplkjhgfdsazxcvbnm'
        low = string.ascii_lowercase
        lowchecker = -1
        for i in low:
            if pword.count(i)>0:
                lowchecker = 1

        return lowchecker

    def passwordcheckernum(self,pword):
        # '1234567890'
        num = string.digits
        numchecker = -1
        for i in num:
            if pword.count(i)>0:
                numchecker = 1

        return numchecker

    def generatePassword(self, request):  # defining a function
        password = ""  # defining a blank string
        passwordchar = 0  # setting the number of charactor in the string to zero to control the loop

        # repeats the indented text while the password is less than requested number of characters long
        while(passwordchar < request):

            menu = [self.generatepassworddigit(),self.generatepasswordLowercase(),self.generatepasswordUppercase(),self.generateSpecialCharactors()]
            password = password + menu[random.randrange(0,4)]
            passwordchar = passwordchar + 1

        return password
# final check creates the password and checks it for all 4 types of characters
#
#

    def finalcheck(self,request):
        superp = ''
        low = 0
        sp = 0
        cap = 0
        num = 0
        #run = 0
        while low < 1 or num < 1 or cap < 1 or sp < 1:
            superp = self.generatePassword(request)
            #run = run + 1
            low = self.passwordcheckerlow(superp)
            num = self.passwordcheckernum(superp)
            cap = self.passwordcheckercap(superp)
            sp = self.passwordcheckersp(superp)

        self.password = superp







