#coding: UTF-8

class Song(object):
    lyrics_list = []

    def __init__(self, lyrics_list):
        Song.lyrics_list = lyrics_list

    def sing_me_a_song(self):
        for line in self.lyrics_list:
            print line

lyrics_list = ["Happy birthday to you",
                   "I don't want to get sued",
                   "So I'll stop right there"]
happy_bday = Song(lyrics_list)
happy_bday.sing_me_a_song()

lyrics_list = ["They rally around tha family",
                        "With pockets full of shells"]
bulls_on_parade = Song(lyrics_list)
bulls_on_parade.sing_me_a_song()
