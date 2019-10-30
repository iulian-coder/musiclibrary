
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
    x = import_music()
    albums = [item[1] for item in x]
    for i, data in enumerate(albums):
        print(i+1, data)


