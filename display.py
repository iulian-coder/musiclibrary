
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

# As a user I want to view all imported albums

def display_albums():
    x = import_music()
    albums = [item[1] for item in x]
    for i, data in enumerate(albums):
        print(i+1, data)


display_albums()
# As a user I want to find all albums created by given artist
print("\n**********")


    
def search_artist():
    lista = import_music()
    for x in lista:
        if x[0] == "Pink Floyd":
            print('Artisit: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))


search_artist()

# As a user I want to find album by album name

def search_album():
    lista = import_music()
    for x in lista:
        if x[1] == "Boston":
            print('Artisit: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))
        
search_album()


# As a user I want to find album by album name

def search_album():
    nume = input('SCrie albumu')
    lista = import_music()
    for x in lista:
        if x[1] == nume:
            print('Artisit: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))

       
search_album()

print(import_music())