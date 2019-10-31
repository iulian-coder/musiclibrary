
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


def display_albums():
    print("\n\tAll Albums\n")
    x = import_music()
    albums = [item[1] for item in x]
    for i, data in enumerate(albums):
        print(i+1, data)


def search_artist():
    user_input = input("Write artist ")
    lista = import_music()
    for x in lista:
        if x[0].lower() == user_input.lower():
            print('\nArtist: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))


def search_album():
    user_input = input('Write album ')
    lista = import_music()
    for x in lista:
        if x[1].lower() == user_input.lower():
            print('\nArtist: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))


def search_genre():
    user_input = input('Write genre ')
    list = import_music()
    for x in list:
        if x[3].lower() == user_input.lower():
            print('\nArtist: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration: {}\n'.format(x[0], x[1], x[2], x[3], x[4]))
