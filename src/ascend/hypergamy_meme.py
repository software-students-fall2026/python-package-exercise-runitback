import random

_HYPERGAMY_MESSAGES = ("there's no hope.", "its so jover.", "hypergamy comes for us all.")


def make_hypergamy_meme_ascii(color=False):
    width, height = 82, 33
    canvas = [[" "] * width for _ in range(height)]
    colored_cells = {}

    women_y = (2, 7, 12, 17, 22, 27)
    men_y = women_y
    woman_x, man_x = 9, 74
    start_x, target_x, target_y = woman_x + 4, 68, 3

    # Draw complete rising lines from each woman to the top man.
    for woman_y_pos in women_y:
        start_y = woman_y_pos + 1
        previous_y = start_y

        for x in range(start_x, target_x):
            progress = (x - start_x) / (target_x - start_x)
            y = round(start_y + (target_y - start_y) * progress)
            stroke = "-" if y == previous_y else "/"
            canvas[y][x] = stroke
            previous_y = y

        canvas[target_y][target_x] = ">"

    def draw_figure(x, y, figure, group):
        for row_offset, row in enumerate(figure):
            for column_offset, char in enumerate(row):
                canvas[y + row_offset][x + column_offset] = char
                if char != " ":
                    colored_cells[(x + column_offset, y + row_offset)] = group

    woman = (" O ", "/|\\", "/_\\", "| |")
    man = (" O ", "/|\\", "| |", "/ \\")

    for y in women_y:
        draw_figure(woman_x, y, woman, "women")

    for y in men_y:
        draw_figure(man_x, y, man, "men")

    ansi = {"women": "\033[95m", "men": "\033[96m"}
    reset = "\033[0m"
    output = []

    for y, row in enumerate(canvas):
        last = len(row)
        while last and row[last - 1] == " ":
            last -= 1

        rendered = []
        active_color = None

        for x, char in enumerate(row[:last]):
            next_color = ansi.get(colored_cells.get((x, y))) if color else None

            if next_color != active_color:
                if active_color:
                    rendered.append(reset)
                if next_color:
                    rendered.append(next_color)
                active_color = next_color

            rendered.append(char)

        if active_color:
            rendered.append(reset)

        output.append("".join(rendered))

    output.append(random.choice(_HYPERGAMY_MESSAGES))
    return "\n".join(output)
