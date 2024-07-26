import random
import prompt


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = 10
    return [start + step * i for i in range(length)]


def play_progression_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    CORRECT_ANSWERS = 0
    while CORRECT_ANSWERS < 3:
        progression = generate_progression()
        length = len(progression)
        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = ".."
        print("Question: " + " ".join(map(str, progression)))
        user_answer = prompt.string("Your answer: ")

        if int(user_answer) == correct_answer:
            print("Correct!")
            CORRECT_ANSWERS += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
