import utils
import typing
import math

quiz = utils.read_quiz(2)


class Bag(typing.TypedDict):
    blue: int
    red: int
    green: int


# game 1
pgame: set = set()
for line in quiz:
    game, game_bags = line.split(":")
    game_n = int(game.replace("Game ", ""))
    for exam in game_bags.split(";"):
        for ball in exam.split(","):
            tbag: Bag = Bag(blue=0, green=0, red=0)
            ball_n, ball_name = ball.strip().split(" ")
            tbag[ball_name] += int(ball_n)
            if tbag["blue"] > 14 or tbag["green"] > 13 or tbag["red"] > 12:
                pgame.add(game_n)
                break

print(sum(range(1, 101)) - sum(pgame))

# game 2
powers = []
for line in quiz:
    game, game_bags = line.split(":")
    game_n = int(game.replace("Game ", ""))
    tbag: Bag = Bag(blue=0, green=0, red=0)
    for exam in game_bags.split(";"):
        for ball in exam.split(","):
            ball_n, ball_name = ball.strip().split(" ")
            ball_n = int(ball_n)
            match ball_name:
                case "blue":
                    if ball_n > tbag["blue"]:
                        tbag["blue"] = ball_n
                case "green":
                    if ball_n > tbag["green"]:
                        tbag["green"] = ball_n
                case "red":
                    if ball_n > tbag["red"]:
                        tbag["red"] = ball_n
    powers.append(math.prod(tbag.values()))
print(sum(powers))
