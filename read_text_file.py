class Song(object):
    def __init__(self, artist, track):
        self.artist = artist
        self.track = track


class ReadText:
    def read_txt(self, file):
        count = 0
        strings = []
        with open(file, "r") as fp:
            for line in fp:
                line = line.strip()
                # line = line.decode('utf-8','ignore').encode("utf-8")
                if "-" in line: # only append valid input
                    strings.append(line)
            # while True:
            #     # count += 1
            #     # line = fp.readline()
            #     # if not line:
            #     #     break
            #     # line = line.strip()
            #     # line = line.decode('utf-8', 'ignore').encode("utf-8")
            #     # strings.append(line)
        print(strings)
        return strings

    def find_artist_track(self, arr):
        songs = []
        for line in arr:
            temp = line.split("-")
            track = str.strip(temp[1])
            artist = str.strip(temp[0])
            if artist and track:
                songs.append(Song(artist, track))
        return songs

