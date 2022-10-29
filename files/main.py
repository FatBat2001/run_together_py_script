from gettext import find
from http.client import FOUND
from operator import length_hint
import tkinter as tk
from tkinter import Canvas, filedialog, Text
import os
from tkinter.font import ITALIC
from unittest import skip

#initializes the screen and the list with previous selected apps 
def initializer():    
    #first we initialize the Apps list with all saved apps from before 
    #initializing the output on the frame     
    with open("save.txt", "r") as f:
        content = f.read().split('\n')
    for app in content:
        #checking if the app path isn't empty 
        if app != '':    
            label = tk.Label(frame, text=app, bg="red", fg = "white", font=ITALIC)
            label.pack()
        f.close()
    return content



#helper function to find if an path has been entered before 
def find_in_list(List, key):
    for item in List:
        if item == key:
            return False
    return True


#file dialogue function that directs me to the exe file I want 
def addApp():
    app_path = filedialog.askopenfilename(initialdir='/', title='Select File',
    filetypes=(("excutables", "*.exe"), ("all files", "*.*"))
    )
    if find_in_list(Apps, app_path) == True:
        if app_path != '':
            Apps.append(app_path)
            label = tk.Label(frame, text=app_path, bg="red", fg = "white", font=ITALIC)
            label.pack()

#passed to the button to run the saved apps 
def runApps():
    for i in range(1, len(Apps)):
        os.startfile(Apps[i])




# initializing the GUI
root = tk.Tk()

#making a canvas to make the window bigger 
Canvas = tk.Canvas(root, height=600, width=600, bg = "#263D42")
Canvas.pack()

#adding a frame to put the apps on 
frame = tk.Frame(root, bg="white") 
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

#initializing the List with previous selected apps 
Apps = initializer()



#file daialogue button
openFile = tk.Button(root, text="Select Apps", padx=10, pady=5, fg="white", bg="#263D42", command=addApp)
openFile.pack()

#running the apps button 
runApps = tk.Button(root, text="Run Apps", padx=15, pady=5, fg="white", bg="#263D42", command=runApps)
runApps.pack()


#this runs the GUI Until we press exit 
root.mainloop()
#GUI stops here 




#saving the filenames 
with open('save.txt', 'w') as f:
    lines = ""
    
    for i in range(0, len(Apps)):
        if i != (len(Apps) - 1):
            lines = lines + Apps[i] + '\n'
        else:
             lines = lines + Apps[i]
    f.write(lines)
    f.close()

#program ends
