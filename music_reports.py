from display import *
import os



def main():
    while True:
        print("""\t\t ************ MENIU ************
        
        1. View all imported albums
        2. Find all albums by genre
        3. Find all albums from given time range (Under Construction)
        4. Find shortest/longest album
        5. Find all albums created by given artist
        6. Find album by album name
        7. Full Report (Under Construction)
        8. Exit/Quit

        \t************ SPECIAL ************

        9. View similar music by genres (Under Construction)
       10. Add new album (Under Construction)
       11. Edit album (Under Construction)
       12. Export album to external file - Under Construction """)

        user_input = input("\nWhat would you like to do? ")
        os.system("clear")
        if user_input == "1":
            display_albums()
            input("\nPress enter to continue...")
            os.system("clear")
        elif user_input == "2":
            search_genre()
            input("\nPress enter to continue...")
            os.system("clear")
        elif user_input == "3":
            print("\n Under Construction")
        elif user_input == "4":
            user_input2 = input("Choose shortest or longest   ")
            findShortest(user_input2)
            input("\nPress enter to continue...")
            os.system("clear")            
        elif user_input == "5":
            search_artist()
            input("\nPress enter to continue...")
            os.system("clear")
        elif user_input == "6":
            search_album()
            input("\nPress enter to continue...")
            os.system("clear")
        elif user_input == "7":
            print("\n Under Construction")    
        elif user_input == "8":
            print("\n Goodbye")
            break 
        elif user_input !="":
            print("\n *****Not Valid Choice Try again*****")            


if __name__ == "__main__":
    main()