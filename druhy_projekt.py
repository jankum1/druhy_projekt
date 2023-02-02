"""
projekt_2.py: druhý projekt do Engeto Online Python Akademie

author: Michal Janků
email: michal.janku@cdv.cz
discord: Michal J.#5035
"""
import datetime
import random
random.seed()

separator = "-" * 73


def generate_number() -> list:
    # generate a number in the interval 1000-9999, if the condition is not met, it creates a new number
    while True:
        number = random.randint(1000, 9999)
        set_number = set(str(number))
        if len(set_number) == 4:
            return list(str(number))
        else:
            random.randint(1000, 9999)


def guess_number() -> list:  # requests a number from the user and checks its validity
    while True:
        number = input(">>> ")
        if not number.isnumeric():
            # check if it is a number
            print("The entered value is not a number!")
        elif number.isnumeric() and len(str(number)) != 4:
            # check that it has exactly four digits
            print("The entered number does not have 4 digits!")
        elif number.isnumeric() and len(set(number)) < 4:
            # check whether there are no repeating digits
            print("There are duplicates in the entered value!")
        elif number[0] == "0":
            # check that the entered number does not start with zero
            print("The entered value starts with zero!")
        else:
            return list(str(int(number)))


def bulls_counter(number_of_bulls):  # determine the correct option: bull/bulls
    if number_of_bulls == 1:
        return "bull: 1"
    else:
        return f"bulls: {number_of_bulls}"


def cows_counter(number_of_cows):  # determine the correct option: cow/cows
    if number_of_cows == 1:
        return "cow: 1"
    else:
        return f"cows: {number_of_cows}"


def game_rating(guesses):  # print the rating by the quantity of guesses
    if guesses < 7:
        print("That's amazing!")
    elif guesses < 10:
        print("That's average!")
    else:
        print("That's not so good!")


def save_result(finish, guesses, time):  # save the result to the txt file
    file_name = "score.txt"
    new_score = f"Date: {finish.strftime('%d/%m/%Y %H:%M')}; Guesses: {guesses}; Guess time: {time} \n"
    # save local game end time, the number of guesses and the guessing time
    txt_file = open(file_name, mode="a")
    txt_file.write(new_score)
    txt_file.close()


def print_game_history():  # load and print previous results from txt file
    txt_file = open("score.txt", mode="r")
    ranking = txt_file.read()
    print(ranking)


def seconds_counter(seconds):  # determine the correct option: second/seconds
    if seconds == 1:
        return "second"
    else:
        return "seconds"


def minutes_counter(minutes):  # determine the correct option: minute/minutes
    if minutes == 1:
        return "minute"
    else:
        return "minutes"


def time_counter(time1, time2):  # returns the duration of the game in minutes + seconds
    total_time = round(time2.timestamp() - time1.timestamp(), 0)
    # duration of the game in seconds
    seconds = total_time % 60
    minutes = (total_time - seconds) / 60
    return f"{int(minutes)} {minutes_counter(minutes)} and {int(seconds)} {seconds_counter(seconds)}"


print(f"""
Hi there!
{separator}
I've generated a random 4 digit number for you.
Let's play a bulls and cows game.
{separator}
Enter a number:
{separator}""")


game_running = True  # the game is running
start_time = datetime.datetime.now()  # save the start time of the game

secret_number = generate_number()  # create a secret 4-digit number
players_guess = guess_number()
attempts = int()


while game_running:
    if secret_number == players_guess:
        attempts += 1  # if guessed, add a last attempt to overall score
        game_running = False  # end of guessing
    else:
        bulls = int()
        for i in range(4):
            if players_guess[i] == secret_number[i]:
                # compare digits in specific positions
                bulls += 1
                # for each match add one bull
        cows = len(set(secret_number).intersection(set(players_guess))) - bulls
        # determine the quantity of cows
        attempts += 1
        # if not guessed, increase the quantity of attempts
        print(bulls_counter(bulls), ",", cows_counter(cows))
        # print guessed number of bull(s) and cow(s)
        print(separator)
        players_guess = guess_number()
        # invite the player for another guess
else:
    if not game_running:  # the user guessed the right number
        print(f"Correct, you've guessed the right number in {attempts} guesses!")
        print(separator)

finish_time = datetime.datetime.now()  # save the finish time of the game
game_time = time_counter(start_time, finish_time)  # duration of the game (min + sec)
save_result(finish_time, attempts, game_time)

game_rating(attempts)

print(f"""{separator}
It took you {game_time}.
{separator}
Game history:
""")

print_game_history()
