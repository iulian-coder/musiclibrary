
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
    list = import_music()
    albums = [item[1] for item in list]
    for i, data in enumerate(albums):
        print(i+1, data)


def search_artist():
    user_input = input("Write artist ")
    list = import_music()
    if any(user_input in s for s in list):
        for x in list:
            if x[0].lower() == user_input.lower():
                print('\nArtist: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))
    else:
        print(f"You don't have this {user_input} artist")


def search_album():
    user_input = input('Write album ')
    list = import_music()
    if any(user_input in s for s in list):
        for x in list:
            if x[1].lower() == user_input.lower():
                print('\nArtist: {}\nAlbum: {}\nRelease Year: {}\nGenre: {}\nDuration {}\n'.format(x[0], x[1], x[2], x[3], x[4]))
    else:
        print(f"You don't have this {user_input} album")

def search_genre():
    user_input = input('Write genre ')
    list = import_music()
    if any(user_input.lower() in s for s in list):
        for x in list:
            if x[3].lower() == user_input.lower():
                print(f'\nArtist: {x[0]}\nAlbum: {x[1]}\nRelease Year: {x[2]}\nGenre: {x[3]}\nDuration: {x[4]}\n')
    else:
        print(f"You don't have this {user_input} genre")


def getDuration(album):
    (mm, ss) = album[-1].split(':')
    return int(mm) * 60 + int(ss)


def findShortest(criteria="shortest"):
    albums = import_music()
    lst = sorted(albums, key=lambda x: getDuration(x))
    if criteria == 'longest':
        print(lst[-1])
    else:
        print(lst[0])
