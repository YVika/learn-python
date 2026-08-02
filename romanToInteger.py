def romanToInteger(roman: str) -> int:
    result = 0
    roman_map = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    for i in range(len(roman)):
        curr_val = roman_map[roman[i]]

        if i + 1 < len(roman) and curr_val < roman_map[roman[i + 1]]:
            result -= curr_val
        else:
            result += curr_val

    return result


print(romanToInteger("XXXIIV"))
