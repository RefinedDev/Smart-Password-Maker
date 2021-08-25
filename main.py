from tkinter import *
from tkinter.constants import BOTH
from tkinter.font import BOLD

import numpy as np
import uuid
import pyperclip
import random
from versionCheck import check

class SPM:
    def __init__(self):
        self.CURRENT_VERSION  = '0.1'
        check(self.CURRENT_VERSION)

        self.UI = Tk()
        self.BGcolor = 'dim gray'

        self.app_Icon = PhotoImage(file='Assets/SPM_Icon.png')
        self.titleIcon = PhotoImage(file = 'Assets/SPM_Title.png')

        self.UI.iconphoto(False, self.app_Icon)
        self.UI.title('Smart Password Maker')

        self.create_Scene()

    @staticmethod
    def copyPassword(text,button):
        pyperclip.copy(str(text))
        button.config(text ='Copied')

    def set_Password_Type(self,theType,buttonObject,Frame):
        self.currentType = theType

        for i in Frame.winfo_children():
            i.config(bg=self.BGcolor)

        buttonObject.config(bg='red')

        for i in self.constraints.winfo_children():
            if isinstance(i,Button) or isinstance(i,Entry):
                if self.currentType == 'Token':
                    i.config(state=DISABLED)
                else:
                    i.config(state=NORMAL)

    def set_Constraint_Type(self,theType,buttonObject):
        self.currentConstraint = theType

        for i in self.constraints.winfo_children():
            i.config(bg=self.BGcolor)

        buttonObject.config(bg='red')
    
    def generatePassword(self,bgFrame):
        alphabets = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

        RESULT = ''
        if self.currentType == 'Token':
            RESULT = uuid.uuid4().hex
            self.passwordLable.config(text=RESULT,fg='springgreen2')
        else:
           while True:
                for _ in range(np.clip(int(self.passLength.get()),5,20)):
                    if self.currentConstraint == 'LettersOnly':
                        chosenLetter = random.choice(alphabets)
                        RESULT = RESULT + chosenLetter
                    elif self.currentConstraint == 'NumbersOnly':
                        chosenNumber = str(random.randint(0,9))
                        RESULT = RESULT + chosenNumber
                    else:
                        chosenLetter = random.choice(alphabets)
                        chosenNumber = str(random.randint(0,9))
                        comp = random.randint(0,1)
                        if comp == 1:
                            RESULT = RESULT + chosenLetter
                        else:
                            RESULT = RESULT + chosenNumber

                self.passwordLable.config(text=RESULT) 
                if not(RESULT in self.usedPasswords):
                    self.usedPasswords = np.append(self.usedPasswords,RESULT)
                    self.passwordLable.config(fg='springgreen2')
                    break

        
        if not (hasattr(self,'copyButton')):
            self.copyButton = Button(bgFrame,text='Copy',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,command=lambda : self.copyPassword(RESULT,self.copyButton))
            self.copyButton.pack(side='top',pady=5)
        else:
            self.copyButton.config(text='Copy')

    def create_Scene(self):
        self.usedPasswords = np.array([],dtype='str')
        self.currentType = 'Normal'
        self.currentConstraint = 'Both'

        # TOP
        bgFrame = Frame(self.UI,bg=self.BGcolor)
        bgFrame.pack(fill=BOTH,expand=True)

        Label(bgFrame,image=self.titleIcon,bg=self.BGcolor).pack(side='top')
    
        self.passwordLable = Label(bgFrame,text='Choose some options to filter or just click Create!',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD))
        self.passwordLable.pack(side='top')
        
        # PASSWORD TYPES
        typesFrame = Frame(bgFrame,bg=self.BGcolor)
        typesFrame.pack(side='top',pady=20)

        Label(typesFrame,text='Password Type',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD)).pack(side='top')
        
        token = Button(typesFrame,text='Token',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,width=12,command=lambda : self.set_Password_Type('Token',token,typesFrame))
        token.pack(side='left',padx=10)

        normal = Button(typesFrame,text='Normal',bg='red',fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,width=12,command=lambda : self.set_Password_Type('Normal',normal,typesFrame))
        normal.pack(side='left')

        # Constraints TYPES
        self.constraints = Frame(bgFrame,bg=self.BGcolor)
        self.constraints.pack(side='top',pady=20)

        Label(self.constraints,text='Constraints',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD)).pack(side='top')
        
        self.passLength = Entry(self.constraints,bg=self.BGcolor,fg='white',font=("Arial",20,BOLD),width=3,disabledforeground='black',disabledbackground='black')
        self.passLength.insert(0,'5')
        self.passLength.pack(side='top',pady=10)
        
        nO = Button(self.constraints,text='Numbers Only',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,width=12,command=lambda: self.set_Constraint_Type('NumbersOnly',nO),disabledforeground='black')
        nO.pack(side='left')

        lO = Button(self.constraints,text='Letters Only',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,width=12,command=lambda: self.set_Constraint_Type('LettersOnly',lO),disabledforeground='black')
        lO.pack(side='left',padx=10)

        b = Button(self.constraints,text='Both',bg='red',fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,width=12,command=lambda: self.set_Constraint_Type('Both',b),disabledforeground='black')
        b.pack(side='left')

        # CREATE BUTTON
        createButton = Button(bgFrame,text='Create',bg=self.BGcolor,fg='white',font=("Arial",20,BOLD),relief=GROOVE,borderwidth=5,command=lambda : self.generatePassword(bgFrame))
        createButton.pack(side='top',pady=20)
        
if __name__ == '__main__':
    app = SPM()
    app.UI.mainloop()