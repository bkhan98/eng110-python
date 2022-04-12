def scrabble_calculator(words, one_point=1, two_point=2, three_point=3, four_point=4, five_point=5, eight_point=8,
                        ten_point=10):your camera is on
    words_score = 0
    for i in words:
        if i in one_point:
            words_score += 1
        elif i in two_point:
            words_score += 2
        elif i in three_point:
            words_score += 3
        elif i in four_point:
            words_score += 4
        elif i in five_point:
            words_score += 5
        elif i in eight_point:
            words_score += 8
        elif i in ten_point:
            words_score += 10

    return words_score


class Scrabble:

    def __init__(self, words):
        self.words = words

    print(scrabble_calculator("hellopython"))


scrabble1 = Scrabble(wde)


# one_point = ["a","e","i","o","s","t","r","u","n","l"]
# two_point= ["d","g"]
# three_point=["c","m","b","p"]
# four_point=["h","v","w","y"]
# five_point=["k"]
# eight_point=["x","j"]
# ten_point=["z","q"]


def scrabble_calculator(words):
    words_score = 0
    for i in words:
        if i in one_point:
            words_score += 1
        elif i in two_point:
            words_score += 2
        elif i in three_point:
            words_score += 3
        elif i in four_point:
            words_score += 4
        elif i in five_point:
            words_score += 5
        elif i in eight_point:
            words_score += 8
        elif i in ten_point:
            words_score += 10

    return words_score


print(scrabble_calculator("hellopython"))

scrabble_calculator(input("Enter any word: \n"))
