PROBLEM_1_INPUT_PATH = "src/01/input.txt"

def read(path: str) -> list[str]:
    file = open(path, 'r')
    lines = file.readlines()
    for i in range(len(lines)):
        lines[i] = lines[i].strip('\n')
    
    print(f"📋 Loaded {len(lines)} lines from {path}")
    return lines

def is_char_a_number(char: str) -> bool:
    return char in "0123456789"

def first_problem(lines: list[str]):
    total = 0
    for line in lines:
        first_number = 0
        last_number = 0

        for char in line:
            if is_char_a_number(char):
                if first_number == 0:
                    first_number = int(char)
                else:
                    last_number = int(char)
        
        if last_number == 0:
            last_number = first_number

        current_line_total = (first_number * 10) + last_number
        #print(f" - Line total: {current_line_total}")
        total += current_line_total

    return total

def test_problem(obtained, expected: int):
    assert obtained == expected, (
        f"🔴 Test failed. Expected {expected}. Got {obtained}"
    )
    print("🟢 Test passed")

def test_firstProblem():
    lines = [
        "1abc2",
        "pqr3stu8vwx",
        "a1b2c3d4e5f",
        "treb7uchet"
    ]
    test_problem(first_problem(lines), 142)

def second_problem(lines: list[str]):
    number_words = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }
    first_letters_of_number_words = "".join(set(key[0] for key in list(number_words.keys())))
    #print(f" - First letters of number words: {first_letters_of_number_words}")

    total = 0
    for line in lines:
        first_number = 0
        last_number = 0

        # first, need to convert all number-words to numbers
        cleaned_line = ""
        i = 0
        while i < len(line):
            char = line[i]
            if char in first_letters_of_number_words:
                # check the next characters to see if it's a number-word
                # if it is, replace it with the number
                # if it isn't, just add the character
                three_chars = line[i:i+3]
                four_chars = line[i:i+4]
                five_chars = line[i:i+5]
                if three_chars in number_words:
                    cleaned_line += number_words[three_chars]
                    i += 2
                elif four_chars in number_words:
                    cleaned_line += number_words[four_chars]
                    i += 3
                elif five_chars in number_words:
                    cleaned_line += number_words[five_chars]
                    i += 4
                else:
                    cleaned_line += char
                    i += 1
            else:
                cleaned_line += char
                i += 1


        #print(f" - Line: {cleaned_line}")

        for char in cleaned_line:
            if is_char_a_number(char):
                if first_number == 0:
                    first_number = int(char)
                else:
                    last_number = int(char)
        
        if last_number == 0:
            last_number = first_number

        current_line_total = (first_number * 10) + last_number
        #print(f" - Line total: {current_line_total}")
        total += current_line_total
    
    return total

def test_secondProblem():
    lines = [
        "two1nine",
        "eightwothree",
        "abcone2threexyz",
        "xtwone3four",
        "4nineeightseven2",
        "zoneight234",
        "7pqrstsixteen"
    ]
    test_problem(second_problem(lines), 281)

if __name__ == "__main__":
    lines = read(PROBLEM_1_INPUT_PATH)
    test_firstProblem()
    test_secondProblem()
    
    print("First problem:", first_problem(lines))
    print("Second problem:", second_problem(lines))