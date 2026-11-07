
from ascend import songs


def main():
    print("Welcome to Ascend!")
    print("------------------")

    print("\nSong Selection Examples:")

    categories = ["gym", "study", "edit", "chill", "BPCORE"]

    for category in categories:
        result = songs.pick_song(category)
        print(category, ":", result)


if __name__ == "__main__":
    main()
