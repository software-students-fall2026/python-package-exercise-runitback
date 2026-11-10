
from ascend import stats


class Tests:
    def test_studying(self):
        card = stats.make_stat_card("studying", 7)

        assert isinstance(card, str)
        assert "ASCEND STAT CARD" in card
        assert "Activity: studying" in card
        assert "Level: 7/10" in card
        assert "Focus:" in card
        assert "Studymaxxing:" in card
        assert "Exam Aura:" in card
        assert "Certified Maxxer" in card

    def test_gym(self):
        card = stats.make_stat_card("gym", 3)

        assert "Activity: gym" in card
        assert "Strength:" in card
        assert "Gymmaxxing:" in card
        assert "Physique Aura:" in card
        assert "NPC Energy" in card

    def test_other_activities(self):
        activities = [
            ("gaming", "Clutch Factor"),
            ("cooking", "Kitchenmaxxing"),
            ("sleeping", "Dreammaxxing"),
            ("walking", "Effort"),
        ]

        for activity, label in activities:
            card = stats.make_stat_card(activity, 5)

            assert "Activity: " + activity in card
            assert label + ":" in card
            assert "Aura Apprentice" in card

    def test_score_ranges(self):
        for level in range(1, 11):
            for i in range(100):
                card = stats.make_stat_card("studying", level)
                lines = card.split("\n")

                minimum_score = (level - 1) * 10 + 1
                maximum_score = level * 10

                scores = []

                for line in lines:
                    if line.startswith("Focus:") or line.startswith("Studymaxxing:") or line.startswith("Exam Aura:"):
                        score = int(line.split(": ")[1].split("/")[0])
                        scores.append(score)

                        assert minimum_score <= score
                        assert score <= maximum_score

                assert len(scores) == 3

                overall_line = ""
                for line in lines:
                    if line.startswith("Overall Aura:"):
                        overall_line = line

                overall_score = int(overall_line.split(": ")[1].split("/")[0])
                assert overall_score == sum(scores) // len(scores)

    def test_rank_levels(self):
        ranks = [
            (1, "NPC Energy"),
            (3, "NPC Energy"),
            (4, "Aura Apprentice"),
            (6, "Aura Apprentice"),
            (7, "Certified Maxxer"),
            (9, "Certified Maxxer"),
            (10, "Final Boss Aura"),
        ]

        for level, rank in ranks:
            card = stats.make_stat_card("studying", level)
            assert "Rank: " + rank in card

    def test_invalid_activity(self):
        invalid_activities = ["", "   ", 123, None]

        for activity in invalid_activities:
            try:
                stats.make_stat_card(activity, 5)
                assert False, "Expected an error for invalid activity"
            except (TypeError, ValueError):
                pass

    def test_invalid_level(self):
        invalid_levels = [0, 11, -1, "five", 3.5, None, True]

        for level in invalid_levels:
            try:
                stats.make_stat_card("studying", level)
                assert False, "Expected an error for invalid level"
            except (TypeError, ValueError):
                pass

    def test_boundary_levels(self):
        card_one = stats.make_stat_card("studying", 1)
        card_ten = stats.make_stat_card("studying", 10)

        assert "Level: 1/10" in card_one
        assert "Rank: NPC Energy" in card_one
        assert "Level: 10/10" in card_ten
        assert "Rank: Final Boss Aura" in card_ten

    def test_activity_whitespace_and_case(self):
        card = stats.make_stat_card("  STUDYING  ", 7)

        assert "Activity: STUDYING" in card
        assert "Focus:" in card
        assert "Studymaxxing:" in card
        assert "Exam Aura:" in card
    
    def test_ascii_graph_has_figures_and_arrows(self):
        graph = stats.make_hypergamy_meme_ascii()

        assert graph.count("O") == 12
        assert "/" in graph
        assert "-" in graph
        assert ">" in graph


    def test_ascii_graph_uses_color_only_when_requested(self):
        plain_graph = stats.make_hypergamy_meme_ascii()
        color_graph = stats.make_hypergamy_meme_ascii(color=True)

        assert "\033[" not in plain_graph
        assert "\033[95m" in color_graph
        assert "\033[96m" in color_graph
