def solve_string_value(value: str) -> int:
    maximum: int = 0
    words_processed: list = list()
    for i in range(0, len(value) + 1):
        for j in range(i + 1, len(value) + 1):
            word: str = value[i:j]
            if word in words_processed:
                continue
            val = len(word) * get_reps(value, word)
            if val > maximum:
                maximum = val
            words_processed.append(word)
    return maximum


def get_reps(value: str, word: str) -> int:
    count: int = 0
    len_: int = len(word)
    for i in range(0, (len(value) + 1) - len_):
        if value[i: i + len_] == word:
            count += 1
    return count
