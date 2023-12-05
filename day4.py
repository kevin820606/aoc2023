import utils

quiz = utils.read_quiz(4)
scores = []
for line in quiz:
    Card, card_numbers = line.split(":")
    card_n = int(Card.replace("Card ", ""))
    winning_card_str, own_card_str = card_numbers.split("|")
    winning_card = set(winning_card_str.strip().split(" "))
    own_card = set(own_card_str.strip().split(" "))
    inters = winning_card.intersection(own_card)
    if "" in inters:
        inters.remove("")
    if len(inters) > 0:
        scores.append(2 ** (len(inters) - 1))
print(sum(scores))


winning_table: dict[int, int] = {}

for line in quiz:
    Card, card_numbers = line.split(":")
    card_n = int(Card.replace("Card ", ""))
    winning_card_str, own_card_str = card_numbers.split("|")
    winning_card = set(winning_card_str.strip().split(" "))
    own_card = set(own_card_str.strip().split(" "))
    inters = winning_card.intersection(own_card)
    if "" in inters:
        inters.remove("")
    winning_table[card_n] = winning_table.get(card_n, 0) + 1
    if (win_game := len(inters)) > 0:
        for i in range(1, win_game + 1):
            winning_table[card_n + i] = (
                winning_table.get(card_n + i, 0) + winning_table[card_n]
            )
        print(card_n, winning_table)
print(winning_table)
print(sum(winning_table.values()))
