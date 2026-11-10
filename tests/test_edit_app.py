
import json
import subprocess
import sys

import pytest

from edit_app import build_edit_blueprint
from pathlib import Path


def test_successful_blueprint():
    blueprint = build_edit_blueprint(
        "gym", "win", "gym", "runway",
        "I feel tired.", 8
    )

    assert blueprint["activity"] == "gym"
    assert blueprint["outcome"] == "win"
    assert isinstance(blueprint["title"], str)
    assert blueprint["song"] == {
        "title": "METAMORPHOSIS",
        "artist": "INTERWORLD"
    }
    assert blueprint["model"] == "Bella Hadid"
    assert "cooked" in blueprint["caption"].lower()
    assert "ASCEND STAT CARD" in blueprint["stat_card"]
    assert "Level: 8/10" in blueprint["stat_card"]


@pytest.mark.parametrize(
    "activity,outcome,song_category,model_category,caption,level",
    [
        ("gym", "win", "gym", "runway", "I feel tired.", 0),
        ("gym", "win", "gym", "runway", "I feel tired.", 11),
        ("gym", "invalid", "gym", "runway", "I feel tired.", 8),
        ("gym", "win", "unknown", "runway", "I feel tired.", 8),
        ("gym", "win", "gym", "runway", "", 8),
    ],
)
def test_invalid_blueprint_inputs(
    activity, outcome, song_category, model_category, caption, level
):
    with pytest.raises(ValueError):
        build_edit_blueprint(
            activity, outcome, song_category,
            model_category, caption, level
        )

def run_app(inputs, cwd):
    app_path = Path(__file__).resolve().parents[1] / "edit_app.py"

    return subprocess.run(
        [sys.executable, str(app_path)],
        input="\n".join(inputs) + "\n",
        text=True,
        capture_output=True,
        cwd=cwd,
        check=False,
    )



def test_cli_success_and_preserves_existing_file(tmp_path):
    # The CLI writes output to the current working directory.
    existing_file = tmp_path / "edit_blueprint.json"
    existing_file.write_text('{"keep": "original"}', encoding="utf-8")

    result = run_app(
        ["gym", "win", "gym", "runway", "I feel tired.", "8"],
        tmp_path,
    )

    assert result.returncode == 0
    assert existing_file.read_text(encoding="utf-8") == (
        '{"keep": "original"}'
    )

    new_file = tmp_path / "edit_blueprint_1.json"
    assert new_file.exists()

    blueprint = json.loads(new_file.read_text(encoding="utf-8"))
    assert blueprint["song"]["title"] == "METAMORPHOSIS"
    assert "Blueprint saved to edit_blueprint_1.json" in result.stdout


def test_cli_invalid_level_returns_nonzero(tmp_path):
    result = run_app(
        ["gym", "win", "gym", "runway", "I feel tired.", "15"],
        tmp_path,
    )

    assert result.returncode != 0
    assert "Could not generate edit" in result.stderr
    assert not (tmp_path / "edit_blueprint.json").exists()
