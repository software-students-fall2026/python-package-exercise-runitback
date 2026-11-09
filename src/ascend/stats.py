
import random


def make_stat_card(activity, level):
    """
    Create a fictional stat card for an everyday activity.
    Scores depend on the selected level from 1 to 10.
    """

    if not isinstance(activity, str):
        raise TypeError("Activity must be a string.")

    if activity.strip() == "":
        raise ValueError("Activity cannot be empty.")

    if type(level) is not int:
        raise TypeError("Level must be an integer.")

    if level < 1 or level > 10:
        raise ValueError("Level must be between 1 and 10.")

    activity_name = activity.strip()
    activity_lower = activity_name.lower()

    if activity_lower == "studying":
        labels = ["Focus", "Studymaxxing", "Exam Aura"]
    elif activity_lower == "gym":
        labels = ["Strength", "Gymmaxxing", "Physique Aura"]
    elif activity_lower == "gaming":
        labels = ["Reaction Time", "Gamer Aura", "Clutch Factor"]
    elif activity_lower == "cooking":
        labels = ["Chef Energy", "Flavor Aura", "Kitchenmaxxing"]
    elif activity_lower == "sleeping":
        labels = ["Rest", "Dreammaxxing", "Sleep Aura"]
    else:
        labels = ["Effort", "Maxxing", "Aura"]

    minimum_score = (level - 1) * 10 + 1
    maximum_score = level * 10

    scores = []

    for label in labels:
        score = random.randint(minimum_score, maximum_score)
        scores.append(score)

    overall_aura = sum(scores) // len(scores)

    if level <= 3:
        rank = "NPC Energy"
    elif level <= 6:
        rank = "Aura Apprentice"
    elif level <= 9:
        rank = "Certified Maxxer"
    else:
        rank = "Final Boss Aura"

    card = "================================\n"
    card += "       ASCEND STAT CARD\n"
    card += "================================\n"
    card += "Activity: " + activity_name + "\n"
    card += "Level: " + str(level) + "/10\n\n"

    for i in range(len(labels)):
        card += labels[i] + ": " + str(scores[i]) + "/100\n"

    card += "\nOverall Aura: " + str(overall_aura) + "/100\n"
    card += "Rank: " + rank + "\n"
    card += "================================"

    return card
