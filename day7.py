import utils

quiz: list[str] = utils.read_quiz(day=7, is_example=True)


card_ord: dict = {
    "A": 14,
    "K": 13,
    "Q": 12,
    "J": 11,
    "T": 10,
    "9": 9,
    "8": 8,
    "7": 7,
    "6": 6,
    "5": 5,
    "4": 4,
    "3": 3,
    "2": 2,
}


def get_types(cards: str) -> float:
    pair = False
    largest = 0
    for c in card_ord.keys():
        count = cards.count(c)
        if count > 3:
            return count
        if count > largest:
            largest = count
        if count == 2:
            if pair:
                return 2.5
            pair = True
    if pair:
        if largest == 3:
            return 3.5
        return 2
    return largest


CardContent = tuple[list[int], float, int]

pairs: list[CardContent] = [
    (
        [card_ord[card] for card in line.split()[0]],
        get_types(line.split()[0]),
        int(line.split()[1]),
    )
    for line in quiz
]


def is_bigger(first_card: CardContent, second_card: CardContent) -> bool:
    if first_card[1] != second_card[1]:
        return first_card[1] > second_card[1]
    for i in range(5):
        if first_card[i] != second_card[i]:
            return first_card[i] != second_card[i]
    return False


sorted(pairs)
