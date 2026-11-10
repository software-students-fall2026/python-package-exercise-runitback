from ascend import hypergamy_meme


class Tests:
    def test_ascii_graph_has_figures_and_arrows(self):
        graph = hypergamy_meme.make_hypergamy_meme_ascii()

        assert graph.count("O") == 12
        assert "/" in graph
        assert "-" in graph
        assert ">" in graph

    def test_ascii_graph_uses_color_only_when_requested(self):
        plain_graph = hypergamy_meme.make_hypergamy_meme_ascii()
        color_graph = hypergamy_meme.make_hypergamy_meme_ascii(color=True)

        assert "\033[" not in plain_graph
        assert "\033[95m" in color_graph
        assert "\033[96m" in color_graph

    def test_ascii_graph_appends_randomized_message(self, monkeypatch):
        messages = ("first test message", "second test message")

        monkeypatch.setattr(hypergamy_meme, "_HYPERGAMY_MESSAGES", messages)
        monkeypatch.setattr(hypergamy_meme.random, "choice", lambda options: options[-1])

        graph = hypergamy_meme.make_hypergamy_meme_ascii()

        assert graph.endswith("second test message")
        assert graph.rfind("second test message") > graph.rfind(">")
