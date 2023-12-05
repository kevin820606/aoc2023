
def read_quiz(day: int):
    with open(f"data/day{day}.txt", mode= 'r') as readfile:
        return readfile.readlines()
