# Ascend

## Build and test status

[![Build and Test](https://github.com/software-students-fall2026/python-package-exercise-runitback/actions/workflows/package-tests.yml/badge.svg)](https://github.com/software-students-fall2026/python-package-exercise-runitback/actions/workflows/package-tests.yml)

## Description

Ascend is a lighthearted Python package inspired by looksmaxxing slang, internet memes, and viral edit culture.

Created by Team Run-It-Back, Ascend transforms ordinary topics and everyday activities into exaggerated, meme-inspired content. Whether you're studying for an exam, going to the gym, or gaming with friends, Ascend helps you turn an ordinary activity into something worthy of a dramatic internet edit.

The package provides six main features.

- **Title generation:** Create dramatic, meme-inspired titles from everyday topics.
- **Song selection:** Get song and artist suggestions for your edits.
- **Sentence translation:** Rewrite ordinary sentences using looksmaxxing and internet slang.
- **Model selection:** Receive fashion model suggestions from a catalog.
- **Stat cards:** Generate fictional ratings, funny ranks, and activity-specific statistics.
- **ASCII graph.** The graph shows a text drawing with a random caption.

Ascend is intended for entertainment and creative inspiration. All stat card scores are fictional and do not represent real assessments of someone's appearance, abilities, or worth.

## Team members

Ascend is developed by **Team Run-It-Back**.

| Team member | Responsibility | GitHub |
|---|---|---|
| Brian | Title generation, package setup, publishing | [Brian](https://github.com/BrianDai22) |
| Mihir | Song selection, example program | [Mihir](https://github.com/mihirgan06) |
| Yash | Sentence translation | [Yash](https://github.com/yash-pandya9798) |
| Theo | Stat card generation | [Theo](https://github.com/theoegoldstine) |
| Linh | Model selection, README | [Linh](https://github.com/katiettran) |


## PyPI package

**Package name:** `ascend-runitback`

**Python import name:** `ascend`

> **TODO:** Add the actual PyPI package link once Brian has published the release. Verify the installation name before final submission.

## Installation

Ascend is designed to be installed using pip.

Once the package has been published on PyPI, install it with:

```bash
python -m pip install ascend-runitback
```

You can then import individual Ascend modules into your Python programs:

```python
from ascend import titles, songs, translator, models, stats, hypergamy_meme
```

## Usage

Ascend provides seven functions for generating meme-inspired content.


### Title generation

**Function:** `make_title(activity, outcome)`  
**Module:** `ascend.titles`

The `make_title()` function generates a random looksmaxxing-style edit title based on an activity and its outcome.

**Parameters:**
- `activity`: A non-empty string, such as `"gym"` or `"study"`.
- `outcome`: Must be `"win"`, `"loss"`, or `"grind"`.

Returns a randomly generated title as a string, or `None` for invalid inputs.

**Example:**

```python
from ascend import titles

print(titles.make_title("gym", "win"))
# Example output: "pov gymmaxxing brutal mog"

print(titles.make_title("study", "grind"))
# Example output: "studymaxxing update ascension pending"

print(titles.make_title("gym", "invalid"))
# Output: None
```

Results may vary because the function randomly selects phrases.


### Song selection

**Function:** `pick_song(category)`  
**Module:** `ascend.songs`

The `pick_song()` function recommends a song based on the category you choose.

**Parameters:**
- `category`: Must be `"gym"`, `"study"`, `"edit"`, `"chill"`, or `"BPCORE"`. Categories are case-sensitive.

Returns a tuple containing the song title and artist, or `None` for invalid inputs.

**Example:**

```python
from ascend import songs

print(songs.pick_song("gym"))
# Output: ('METAMORPHOSIS', 'INTERWORLD')

print(songs.pick_song("study"))
# Output: ('Memory Reboot', 'VØJ, Narvent')

print(songs.pick_song("invalid"))
# Output: None
```

### Sentence translation

**Functions:** `translate_sentence(text)` and `translate_many(texts)`  
**Module:** `ascend.translator`

The translator converts ordinary English sentences into looksmaxxing and blackpill-style slang.

#### translate_sentence()

The `translate_sentence()` function translates a single string by replacing recognized words and phrases with slang equivalents.

**Parameters:**
- `text`: A non-empty string containing the sentence to translate.

Returns the translated sentence as a string, or `None` for invalid inputs. Text without recognized phrases is returned unchanged.

**Example:**

```python
from ascend import translator

print(translator.translate_sentence("Good news!"))
# Output: Lifefuel!

print(translator.translate_sentence("I study."))
# Output: I studymaxx.

print(translator.translate_sentence(""))
# Output: None
```

#### translate_many()

The `translate_many()` function translates multiple sentences at once.

**Parameters:**
- `texts`: An iterable of strings, such as a list of sentences.

Returns a list of translated results. Invalid individual sentences produce `None` in the list. Passing a string instead of an iterable of sentences, or a non-iterable value, returns `None`.

**Example:**

```python
from ascend import translator

sentences = ["Good news!", "I study.", "Hello!"]

print(translator.translate_many(sentences))
# Output: ['Lifefuel!', 'I studymaxx.', 'Hello!']

print(translator.translate_many("Hello!"))
# Output: None
```


### Model selection

**Function:** `pick_model(category)`  
**Module:** `ascend.models`

The `pick_model()` function recommends a fashion model based on the selected category.

**Parameters:**
- `category`: A string representing one of five supported categories: `"runway"`, `"editorial"`, `"classic"`, `"angel"`, or `"high-fashion"`. Categories are case-sensitive.

Returns the name of the selected model as a string.

**Example:**

```python
from ascend import models

print(models.pick_model("runway"))
# Output: Bella Hadid

print(models.pick_model("editorial"))
# Output: Vittoria Ceretti

print(models.pick_model("high-fashion"))
# Output: Anok Yai
```

**Invalid inputs:**

The function raises a `ValueError` if the category is not a string or is not one of the supported categories.

```python
models.pick_model("invalid")  # Raises ValueError
models.pick_model(123)        # Raises ValueError
```

### Stat cards

**Function:** `make_stat_card(activity, level)`

**Module:** `ascend.stats`

Generates a fictional stat card for an everyday activity.

Each card includes three activity-specific statistics, an Overall Aura score, and a funny rank determined by the selected level.

**Parameters**

- `activity` — A nonempty string describing the activity.
- `level` — An integer from 1 to 10 determining the score range.

Each level corresponds to a ten-point score range:

| Level | Score range |
|---|---|
| 1 | 1–10 |
| 2 | 11–20 |
| 3 | 21–30 |
| 4 | 31–40 |
| 5 | 41–50 |
| 6 | 51–60 |
| 7 | 61–70 |
| 8 | 71–80 |
| 9 | 81–90 |
| 10 | 91–100 |

**Example 1: Studying**

```python
from ascend import stats

print(stats.make_stat_card("studying", 7))
```

Example output:

```text
================================
       ASCEND STAT CARD
================================
Activity: studying
Level: 7/10

Focus: 65/100
Studymaxxing: 69/100
Exam Aura: 62/100

Overall Aura: 65/100
Rank: Certified Maxxer
================================
```

**Example 2: Gym**

```python
print(stats.make_stat_card("gym", 3))
```

Example output:

```text
================================
       ASCEND STAT CARD
================================
Activity: gym
Level: 3/10

Strength: 26/100
Gymmaxxing: 23/100
Physique Aura: 29/100

Overall Aura: 26/100
Rank: NPC Energy
================================
```

Scores are randomly generated within the selected level's range, so results can differ between calls.

**Supported activity categories**

| Activity | Stat labels |
|---|---|
| Studying | Focus, Studymaxxing, Exam Aura |
| Gym | Strength, Gymmaxxing, Physique Aura |
| Gaming | Reaction Time, Gamer Aura, Clutch Factor |
| Cooking | Chef Energy, Flavor Aura, Kitchenmaxxing |
| Sleeping | Rest, Dreammaxxing, Sleep Aura |
| Other activities | Effort, Maxxing, Aura |

**Rank system**

| Level | Rank |
|---|---|
| 1–3 | NPC Energy |
| 4–6 | Aura Apprentice |
| 7–9 | Certified Maxxer |
| 10 | Final Boss Aura |

The Overall Aura is calculated as the integer average of the three generated scores.

**Invalid inputs**

The function raises:

- `TypeError` when the activity is not a string or the level is not an integer.
- `ValueError` when the activity is empty or the level is outside 1–10.

For example:

```python
stats.make_stat_card("", 5)          # ValueError
stats.make_stat_card("gaming", 11)   # ValueError
stats.make_stat_card("gym", "high")  # TypeError
```

### ASCII graph

`make_hypergamy_meme_ascii(color=False)` returns a text drawing with a random caption. Pass `color=True` to add color in the terminal.

```python
from ascend import hypergamy_meme

print(hypergamy_meme.make_hypergamy_meme_ascii())
```

## Command-line usage

Ascend can also translate text directly from the terminal using `python -m ascend`.

To translate a sentence, run:

```bash
python -m ascend "Good news!"
```

Output:

```text
Lifefuel!
```

You can also pass text through standard input:

```bash
echo "I study." | python -m ascend
```

Output:

```text
I studymaxx.
```

To view the available command-line options, run:

```bash
python -m ascend --help
```

The command accepts text as arguments or reads from standard input when no arguments are provided. It prints the translated text to the terminal.

If no valid, non-empty text is provided, the command displays an error.


## Example program

The [example program](https://github.com/software-students-fall2026/python-package-exercise-runitback/blob/main/example.py) demonstrates all seven Ascend functions.

## Development setup

Contributors should clone the shared team repository rather than creating additional forks.

**1. Clone the repository**

```bash
git clone https://github.com/software-students-fall2026/python-package-exercise-runitback.git
```

**2. Navigate into the project directory**

```bash
cd python-package-exercise-runitback
```

**3. Install Pipenv**

Install Pipenv using a supported installation method for your operating system.

**4. Install the development dependencies**

```bash
pipenv install --dev
```

This creates a virtual environment and installs the dependencies specified by the project's Pipfile.

**5. Create a feature branch**

```bash
git switch -c your-feature-branch
```

Contributors should make changes on their own feature branches and submit pull requests into the team's `main` branch.

A teammate must review the code and run the tests before changes are merged.

## Configuration

Ascend's stat card generator does not require API keys, environment variables, or external databases.

> **TODO:** Confirm whether the other four modules require additional configuration, external data, or environment variables. Document any requirements here before submission.

## Running tests

Ascend uses pytest for automated testing.

To run the full test suite from the project directory:

```bash
pipenv run python -m pytest
```

To run only the stat card tests:

```bash
pipenv run python -m pytest tests/test_stats.py
```

The stat card tests cover:

- Correct return types and formatted output.
- Activity-specific stat labels.
- Random score ranges across all ten levels.
- Overall Aura calculations.
- Rank assignments.
- Invalid activity and level inputs.
- Boundary levels and activity formatting.

The stat card implementation passed nine focused tests, and the local full test suite passed ten tests on Python 3.15.2.

GitHub Actions is configured to build and test pull requests on two recent Python versions. The final workflow results should be checked before merging.

## Building the package

Ascend uses Python's build package to generate distribution files.

From the project directory, run:

```bash
pipenv run python -m build
```

The generated distribution files are placed in the `dist/` directory.

The package is published to PyPI using Twine:

```bash
pipenv run python -m twine upload dist/*
```

Publishing is handled by the team's designated maintainer. Contributors should not upload unapproved releases.

Before publishing, the team must verify that the package builds successfully, passes its tests, and installs correctly in a fresh environment.

## Contributing

All team members contribute through their own GitHub accounts.

The contribution workflow is:

1. Update your local copy of `main`.
2. Create a personal feature branch.
3. Implement your changes and write meaningful tests.
4. Run the relevant tests.
5. Commit and push your changes.
6. Open a pull request into the shared team's `main` branch.
7. Request a teammate review and have the reviewer run the tests.
8. Resolve feedback before merging.
9. Delete the feature branch and update your local `main` after merging.

All pull requests should target the team's shared repository:

https://github.com/software-students-fall2026/python-package-exercise-runitback

## License

> **TODO:** Confirm the repository's license and link it here, if applicable.