import requests
import json
from tkinter import *
import webbrowser

def __close(ui):
    ui.destroy()

def __openGithub(ui):
    webbrowser.get().open(url='https://github.com/RefinedDev/Smart-Password-Maker/releases')
    ui.destroy()

def check(desktopVersion):
    result = requests.get("https://api.github.com/repos/RefinedDev/Smart-Password-Maker/releases/latest")
    currentVersion = json.loads(result.content.decode('utf_8'))['tag_name'].split('v')

    if float(desktopVersion) < float(currentVersion[1]):
        UI = Tk()

        UI.title("New version available!")
        TOP_icon = PhotoImage(file= r"Assets\StaskLogo.png")
        UI.iconphoto(False, TOP_icon)

        titleLogo = Label(UI,text='A new version for SPM is available, would you like to install it?',font=('Arial',15))
        titleLogo.pack(side='top',expand='y')

        yes = Button(UI,text='Yes',font=('Arial',15),borderwidth=2,width=5,command=lambda : __openGithub(UI))
        yes.pack(side='top')

        no = Button(UI,text='No',font=('Arial',15),borderwidth=2,width=5,command=lambda : __close(UI))
        no.pack(side='top')

        UI.mainloop()