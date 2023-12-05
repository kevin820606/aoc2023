def read_quiz(day: int, is_example: bool = False):
    example_file = "_example" if is_example else ""
    file_path = f"data/day{day}{example_file}.txt"
    with open(file_path, mode="r") as readfile:
        return readfile.readlines()
