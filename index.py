from random import randint
def guess():
    guessed = False
    rnd = randint(1, 100)
    while not guessed:
        insert = input("Guess the number:")
        try:
            num = int(insert)
            if num == rnd:
                print("You win!")
                guessed = True
            elif num > rnd:
                print("To big!")
            elif num < rnd:
                print("To small!")
        except ValueError:
            print("It's not a number!")
            continue
if __name__ == '__main__':
    guess()