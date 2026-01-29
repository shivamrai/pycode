# song selector
def songIdentifier(songs):
    count = 0
    for i in range(0, len(songs)):
        for j in range(0, len(songs)):
            if (songs[i] + songs[j] % 60) == 0:  # and i!=j):
                count += 1
    return count


if __name__ == "__main__":
    songs = [60, 60, 60]
    print(songIdentifier(songs))
