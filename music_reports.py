import os
from display import search_album

os.system("clear")
'''
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
'''

def meniu():
    while True:
        print(  """\t\t MENIU
        
        1. View all imported albums
        2. Find all albums by genre
        3. Find all albums from given time range
        4. Find shortest/longest album
        5. Find all albums created by given artist
        6. Find album by album name
        7. Full Report
        8. Exit/Quit

        \t\t SPECIAL

        9. View similar music by genres
       10. Add new album
       11. Edit album
       12. Export album to external file""")

        user_input = input("\nWhat would you like to do? ")
        if user_input =="1": 
            search_album() 
        elif user_input =="2":
            print("\n Ceva Deleted") 
        elif user_input =="3":
            print("\n Ceva Record Found") 
        elif user_input =="8":
            print("\n Goodbye")
            break 
        elif user_input !="":
            print("\n Not Valid Choice Try again") 


meniu()