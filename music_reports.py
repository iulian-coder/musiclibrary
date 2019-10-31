from display import *
import os



def meniu():
    while True:
        print("""\t\t MENIU
        
        1. View all imported albums
        2. Find all albums by genre
        3. Find all albums from given time range (Under Construction)
        4. Find shortest/longest album (Under Construction)
        5. Find all albums created by given artist
        6. Find album by album name
        7. Full Report
        8. Exit/Quit

        \t\t SPECIAL

        9. View similar music by genres (Under Construction)
       10. Add new album (Under Construction)
       11. Edit album (Under Construction)
       12. Export album to external file - Under Construction """)

        user_input = input("\nWhat would you like to do? ")
        if user_input == "1":
            display_albums()
            input("Press enter to continue...")
            os.system("clear")
        elif user_input == "2":
            search_genre()
            input("Press enter to continue...")
            os.system("clear")
        elif user_input == "3":
            print("\n Under Construction")
        elif user_input =="4":
            print("\n Under Construction")
        elif user_input =="5":
            print("\n Ceva Record Found")
        elif user_input =="6":
            print("\n Ceva Record Found")
        elif user_input =="7":
            print("\n Ceva Record Found")    
        elif user_input =="8":
            print("\n Goodbye")
            break 
        elif user_input !="":
            print("\n Not Valid Choice Try again")            


meniu()