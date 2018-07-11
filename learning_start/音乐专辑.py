# def make_album(musician_name, song_name, number=""):
#     if number:
#         album = {'name': musician_name, 'song': song_name, 'number': number}
#     else:
#         album = {'name': musician_name, 'song': song_name}
#     return album
#


def make_album(musician_name, song_name, number=""):
    album = {'name': musician_name, 'song': song_name, 'number': number}
    return album


while True:
    print("(enter 'q' at any time to quit)")
    musician_name = input("请输入一个专辑的的歌手名字:")
    if musician_name == 'q':
        break
    song_name = input("请输入一首歌的名称:")
    if song_name == 'q':
        break
    album1 = make_album(musician_name, song_name)
    print(album1)
# album2 = make_album('周华健', '风雨无阻', 5)
# print(album2)
# album3 = make_album('张学仁', '赵雷')
# print(album3)


# def make_album(name, album_name, number=''):
#     if number:
#         album = {'name': name, 'album_name': album_name, 'number': number}
#     else:
#         album = {'name': name, 'album_name': album_name}
#     return album
#
#
# print(make_album('周杰伦', '听妈妈的话'))
# print(make_album('某某', '某某某', '5'))

# def make_album(name, album_name, number=''):
#     album = {'name': name, 'album_name': album_name}
#     return album
#
#
# while True:
#     print("(enter 'q' at any time to quit)")
#     name = input('请输入歌手名：')
#     if name == 'q':
#         break
#     album_name = input('请输入专辑名：')
#     if album_name == 'q':
#         break
#     print(make_album(name, album_name))

