
from ascend import songs, titles, models


def main():
    print("================================")
    print("       ASCEND EDIT GENERATOR")
    print("================================")

    print("\nGYM ASCENSION EDIT")

    print("\nTITLE:")
    print(titles.make_title("gym", "win"))

    print("\nSONG:")
    print(songs.pick_song("gym"))

    print("\nMODEL:")
    print(models.pick_model("runway"))

    print("\n--- SONG CATALOG ---")
    for category in ["gym", "study", "edit", "chill", "BPCORE"]:
        print(category, ":", songs.pick_song(category))

    print("\n--- TITLE OUTCOMES ---")
    for outcome in ["win", "loss", "grind"]:
        print(outcome, ":", titles.make_title("gym", outcome))

    print("\n--- MODEL CATALOG ---")
    for category in ["runway", "editorial", "classic",
                     "angel", "high-fashion"]:
        print(category, ":", models.pick_model(category))

    print("\n--- INVALID INPUT EXAMPLES ---")
    print("Invalid song:", songs.pick_song("unknown"))
    print("Invalid title:", titles.make_title("", "win"))


if __name__ == "__main__":
    main()
