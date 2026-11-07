
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
