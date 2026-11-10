
import json

from ascend import songs, titles, models, translator, stats


def build_edit_blueprint(activity, outcome, song_category,
                         model_category, caption, level):
    """Generate the content needed for an Ascend edit."""

    if not isinstance(level, int) or not 1 <= level <= 10:
        raise ValueError("Level must be between 1 and 10.")

    title = titles.make_title(activity, outcome)
    song = songs.pick_song(song_category)
    model = models.pick_model(model_category)
    translated_caption = translator.translate_sentence(caption)
    stat_card = stats.make_stat_card(activity, level)

    if title is None or song is None or translated_caption is None:
        raise ValueError("One or more edit inputs are invalid.")

    blueprint = {
        "activity": activity,
        "outcome": outcome,
        "title": title,
        "song": {
            "title": song[0],
            "artist": song[1]
        },
        "model": model,
        "caption": translated_caption,
        "stat_card": stat_card
    }

    return blueprint


def main():
    print("================================")
    print("       ASCEND EDIT BUILDER")
    print("================================")
    print("Create your own BP-style edit!\n")

    activity = input("Enter an activity (e.g. gym): ").strip()

    print("\nOutcomes: win, loss, grind")
    outcome = input("Choose an outcome: ").strip()

    print("\nSong categories: gym, study, edit, chill, BPCORE")
    song_category = input("Choose a song category: ").strip()

    print("\nModel categories: runway, editorial, classic, angel, high-fashion")
    model_category = input("Choose a model category: ").strip()

    caption = input("\nWrite your original caption: ").strip()

    try:
        level = int(input("Choose an aura level (1-10): ").strip())

        blueprint = build_edit_blueprint(
            activity, outcome, song_category,
            model_category, caption, level
        )

    except (ValueError, TypeError) as error:
        print("\nCould not generate edit:", error)
        return

    print("\n================================")
    print("        YOUR EDIT BLUEPRINT")
    print("================================")

    print("\nTITLE:", blueprint["title"])
    print("SONG:", blueprint["song"]["title"],
          "-", blueprint["song"]["artist"])
    print("MODEL:", blueprint["model"])
    print("CAPTION:", blueprint["caption"])
    print("\n" + blueprint["stat_card"])

    with open("edit_blueprint.json", "w", encoding="utf-8") as file:
        json.dump(blueprint, file, indent=4, ensure_ascii=False)

    print("\nBlueprint saved to edit_blueprint.json")
    print("Ready for video generation!")


if __name__ == "__main__":
    main()
