import pygame
import tkinter
from tkinter.filedialog import askdirectory
import os


root = tkinter.Tk()
root.geometry("450x400")
root.title("MP3 Player")
root.resizable(0, 0)
root.config(bg="black")
root.iconbitmap("music_icon.ico")


def get_songs():
    """Clear the listbox, then get the music directory and display all files in the folder to the listbox."""

    song_listbox.delete(0, tkinter.END)

    music_dir = askdirectory(title="Please select a music folder")
    os.chdir(music_dir)
    song_list = os.listdir(music_dir)

    for i in range(len(song_list)):
        song_listbox.insert(i, song_list[i])


# Initialise pygame
pygame.init()
pygame.mixer.init()


def play_song():
    pygame.mixer.music.load(song_listbox.get(tkinter.ACTIVE))
    current_song.set(song_listbox.get(tkinter.ACTIVE))
    pygame.mixer.music.play()


def stop_song():
    pygame.mixer.music.stop()


def pause_song():
    pygame.mixer.music.pause()


def unpause_song():
    pygame.mixer.music.unpause()


title_frame = tkinter.Frame(root)
title_frame.pack(padx=5, pady=5)
song_listbox_frame = tkinter.Frame(root, bg="black")
song_listbox_frame.pack(padx=5, pady=5)
options_frame = tkinter.Frame(root, bg="black")
options_frame.pack(padx=5, pady=5)

current_song = tkinter.StringVar()

title = tkinter.Label(title_frame, text="MP3 Player", font=("Rubrik", 25), bg="black", fg="gold")
title.pack()

song_listbox = tkinter.Listbox(song_listbox_frame, font=("Rubrik", 10), bg="black", fg="gold", selectmode=tkinter.SINGLE, width=50)
song_listbox.pack()

get_songs_button = tkinter.Button(song_listbox_frame, text="Get Songs", font=("Rubrik", 13), bg="black", fg="gold", command=get_songs)
get_songs_button.pack(padx=2, pady=5)

play_button = tkinter.Button(options_frame, text="Play", bg="black", fg="gold", command=play_song, width=7)
play_button.grid(row=0, column=0, padx=2, pady=2)

stop_button = tkinter.Button(options_frame, text="Stop", bg="black", fg="gold", command=stop_song, width=7)
stop_button.grid(row=0, column=1, padx=2, pady=2)

pause_button = tkinter.Button(options_frame, text="Pause", bg="black", fg="gold", command=pause_song, width=7)
pause_button.grid(row=0, column=2, padx=2, pady=2)

unpause_button = tkinter.Button(options_frame, text="Unpause", bg="black", fg="gold", command=unpause_song, width=7)
unpause_button.grid(row=0, column=3, padx=2, pady=2)

current_playing_label = tkinter.Label(root, text="Select a Song!", font=("Rubrik", 10), textvariable=current_song, bg="black", fg="gold")
current_playing_label.pack(padx=10, pady=10)


root.mainloop()
