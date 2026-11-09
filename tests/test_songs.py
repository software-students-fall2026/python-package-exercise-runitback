
from ascend import songs


def test_pick_song_gym():
    result = songs.pick_song("gym")
    assert result == ("METAMORPHOSIS", "INTERWORLD")


def test_pick_song_study():
    result = songs.pick_song("study")
    assert result == ("Memory Reboot", "VØJ, Narvent")


def test_pick_song_invalid_category():
    result = songs.pick_song("unknown")
    assert result is None


def test_pick_song_invalid_type():
    result = songs.pick_song(123)
    assert result is None

def test_pick_song_edit():
    result = songs.pick_song("edit")
    assert result == ("Murder In My Mind", "Kordhell")


def test_pick_song_chill():
    result = songs.pick_song("chill")
    assert result == ("After Dark", "Mr.Kitty")


def test_pick_song_bpcore():
    result = songs.pick_song("BPCORE")
    assert result == ("Love Potions", "BJ Lips")


def test_pick_song_invalid_list():
    result = songs.pick_song([])
    assert result is None
