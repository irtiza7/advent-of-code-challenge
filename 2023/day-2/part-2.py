def calculate_sum_of_powers(games):
    powers_sum = 0
    for game in games:
        game_info = game.split(": ")
        game_sets = game_info[1].split("; ")

        minimum_colors_required = {"red": 0, "blue": 0, "green": 0}

        for game_set in game_sets:
            colors_freqs_info = game_set.split(", ")

            for color_freq_info in colors_freqs_info:
                color_freq_and_color = color_freq_info.split(" ")

                if minimum_colors_required[color_freq_and_color[1]] < int(
                    color_freq_and_color[0]
                ):
                    minimum_colors_required[color_freq_and_color[1]] = int(
                        color_freq_and_color[0]
                    )

        power = 1
        for minimum_color_counts in minimum_colors_required.values():
            power *= minimum_color_counts

        powers_sum += power

    return powers_sum


with open("./input.txt", "r") as file:
    games = file.read().splitlines()
    sum_of_powers = calculate_sum_of_powers(games)
    print(sum_of_powers)
