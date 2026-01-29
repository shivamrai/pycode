"""Song Selector - Select songs based on criteria."""


# song selector
def song_identifier(songs_list):
    """song_identifier function."""
    count = 0
    for i, song_i in enumerate(songs_list):
        for j, song_j in enumerate(songs_list):
            if (song_i + song_j % 60) == 0:  # and i!=j):
                count += 1
    return count


if __name__ == "__main__":
    songs = [60, 60, 60]
    print(song_identifier(songs))
