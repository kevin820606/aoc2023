import utils

quiz = utils.read_quiz(7, True)
cards = "A", "K", "Q", "J", "T", 9, 8, 7, 6, 5, 4, 3, 2
pair_price = {line.split()[0]: line.split()[1] for line in quiz}
pairs = pair_price.keys()
