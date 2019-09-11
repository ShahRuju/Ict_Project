from tkinter import *
import pygame
from tkinter.filedialog import askopenfilename
from PIL import ImageTk, Image
import os

root = Tk()
root.title("Music Player")
#root.geometry('700x400')
pygame.init()
root.configure(background='grey')
#canv = Canvas(root, width=800, height=800, bg='white')
#canv.grid(row=2, column=3)

#img = ImageTk.PhotoImage(Image.open("C:/Users/siddhi/AppData/Local/Programs/Python/Python37/mp1.jpg"))
#canv.create_image(10, 10, anchor=NW, image = img)

global filename
global file
global song_list
global song

def open_file():
    filename = askopenfilename(defaultextension = ".mp3", filetypes=[("MP3", ".mp3")])
    file = os.path.split(filename)[-1]
    for i in [file]:
        song_list.insert(END,i)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()
    
def play():                                  
    pygame.mixer.music.play()
    
def stop():                                     
    pygame.mixer.music.stop()  
              
def pause():                                   
    pygame.mixer.music.pause()
       
def unpause():                                   
    pygame.mixer.music.unpause()
        
def rewind():                                    
    pygame.mixer.music.rewind()
    
def next_song():
    """filename = askopenfilename(defaultextension = ".mp3", filetypes=[("MP3", ".mp3")])
    file = os.path.split(filename)[-1]
    for i in [file]:
        song_list.insert(END,i)
        pygame.mixer.music.load(file)
        pygame.mixer.music.play()"""
    #w = evt.widget
    #song = int(w.curselection()[0])
    n = song_list.get(song)
    pygame.mixer.music.load(n+1)
    pygame.mixer.music.play()

def get_song(evt):
    w = evt.widget
    song = int(w.curselection()[0])
    get = song_list.get(song)
    pygame.mixer.music.load(get)
    pygame.mixer.music.play()
       
def vol(event):                                
    v = Scale.get(volume_slider)
    pygame.mixer.music.set_volume(v)
    
def Exit():
    exit()


    
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
menubar.add_cascade(label='File', menu = filemenu)
filemenu.add_command(label='Open', command = open_file)
filemenu.add_separator()
filemenu.add_command(label='Exit', command = Exit)
root.config(menu=menubar)

openfile = Button(root, width = 20, height = 2, text = 'Open file',font=("Helvetica bold",10),bd=5, command = open_file)
song_list = Listbox(root, width=50, height=10)
song_list.pack(side=TOP)
song_list.insert(END,"PlayList")
song_list.insert(END,"------------------------------------------------------------")
yscroll = Scrollbar(command=song_list.yview, orient=VERTICAL)
yscroll.place(x=325, y=30)
song_list.configure(yscrollcommand=yscroll.set)
rewind_img = ImageTk.PhotoImage(Image.open('C:/Users/siddhi/AppData/Local/Programs/Python/Python37/rewind.jpg'))
rewind_button = Button(root, height=40, width=40, image=rewind_img, command = rewind)
pause_img = ImageTk.PhotoImage(Image.open('C:/Users/siddhi/AppData/Local/Programs/Python/Python37/pause.jpg'))
pause_button = Button(root, height=40, width=40, image=pause_img, command = pause)
play_img = ImageTk.PhotoImage(Image.open('C:/Users/siddhi/AppData/Local/Programs/Python/Python37/play.jpg'))
play_button = Button(root, height=40, width=40, image=play_img, command = play)
unpause_img = ImageTk.PhotoImage(Image.open('C:/Users/siddhi/AppData/Local/Programs/Python/Python37/unpause.jpg'))
unpause_button = Button(root, height=40, width=40, image=unpause_img, command = unpause)
stop_img = ImageTk.PhotoImage(Image.open('C:/Users/siddhi/AppData/Local/Programs/Python/Python37/stop.jpg'))
stop_button = Button(root, height=40, width=40, image=stop_img, command = stop)
next_img = ImageTk.PhotoImage(Image.open('C:/Users/siddhi/AppData/Local/Programs/Python/Python37/next.jpg'))
next_button = Button(root, height=40, width=40, image=next_img, command = next_song)
song_list.bind('<<ListboxSelect>>',get_song)
volume_slider = Scale(root, width = 3, from_=0, to=1, resolution=.1, label='Volume', orient = 'horizontal', fg = 'black', command = vol)

openfile.pack(pady=20)
#song_list.pack(pady=20)
rewind_button.pack(side = LEFT)
pause_button.pack(side = LEFT)
play_button.pack(side = LEFT)
unpause_button.pack(side = LEFT)
stop_button.pack(side = LEFT)
next_button.pack(side = LEFT)
volume_slider.pack(side = LEFT)

root.mainloop()
