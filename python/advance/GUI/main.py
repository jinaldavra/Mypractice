import tkinter as tk
import os
import pygame
import time

screen = tk.Tk()

pygame.mixer.init()

screen.title("Musics")

screen.geometry("400x300")

screen.iconbitmap("Images\musical-note.ico")

musics = os.listdir("Musics")

# Create a scrollbar:

scrollbar = tk.Scrollbar(screen)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Create a listbox:

listbox = tk.Listbox(screen, yscrollcommand=scrollbar.set,width=50,height=15)
for music in musics:
    music_file_path = r'E:\PYTHON\advance\GUI\Musics' + "\\" + music
    listbox.insert(tk.END,music)
    pygame.mixer.music.load(music_file_path)
listbox.pack(side=tk.LEFT, fill=tk.Y)

# Function to play the mp3 file :

def play_music():
    pygame.mixer.music.play()

# Function to stop the mp3 file :

def stop_music():
    pygame.mixer.music.stop()

# Create a play button :

play_button = tk.Button(screen, text="Play",command=play_music)
play_button.pack(pady=10)

stop_button = tk.Button(screen, text="Stop",command=stop_music)
stop_button.pack(pady=10)



scrollbar.config(command=listbox.yview)

screen.mainloop()