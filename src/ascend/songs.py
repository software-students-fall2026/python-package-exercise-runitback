
def pick_song(category):
    songs = {
        "gym": ("METAMORPHOSIS", "INTERWORLD"),
        "study": ("Memory Reboot", "VØJ, Narvent"),
        "edit": ("Murder In My Mind", "Kordhell"),
        "chill": ("After Dark", "Mr.Kitty"),
        "BPCORE": ("Love Potions", "BJ Lips")
    }

    if not isinstance(category, str):
        return None

    if category not in songs:
        return None

    return songs[category]
