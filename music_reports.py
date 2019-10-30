import os
import sys

os.system("clear")

def import_music(filename="text_albums_data.txt"):
    try:
        with open(filename, "r") as f:
            album_list = []
            for line in f:
                album_list.append(line)
            album_list = [x.strip().split(',') for x in album_list]
            return album_list
    except FileNotFoundError:
        print('File not found !')

# As a user I want to find all albums created by given artist
print("Merge!")


artist = "Pink Floyd" #n = input('Search all albums by given artist')

    
def search_artist():
    lista = import_music()
    for x in lista:
        if x[0] == "Pink Floyd":
            print('Artisit: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n======================='.format(x[0], x[1], x[2], x[3], x[4]))



search_artist()

