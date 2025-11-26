import random
import tkinter as tk
from colorama import Fore, Style, init

init(autoreset=True)

HANGMANPICS = [
    """
     +---+
         |
         |
         |
        ===""",
    """
     +---+
     O   |
         |
         |
        ===""",
    """
     +---+
     O   |
     |   |
         |
        ===""",
    """
     +---+
     O   |
    /|   |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
         |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    /    |
        ===""",
    """
     +---+
     O   |
    /|\\  |
    / \\  |
        ==="""
]

def ascii_game():
    words = ["python", "developer", "hangman", "internet", "computer"]
    secret = random.choice(words)
    display = ["_"] * len(secret)
    lives = len(HANGMANPICS) - 1
    print("ASCII Hangman\n")
    while lives > 0 and "_" in display:
        print(HANGMANPICS[len(HANGMANPICS)-1-lives])
        print("Word:", " ".join(display))
        guess = input("Enter a letter: ").lower()
        if guess in secret:
            for i in range(len(secret)):
                if secret[i] == guess:
                    display[i] = guess
        else:
            lives -= 1
    if "_" not in display:
        print("You Win!")
    else:
        print(HANGMANPICS[-1])
        print("You Lost! Word:", secret)

def color_game():
    words = ["python", "coding", "hangman", "school", "internet"]
    secret = random.choice(words)
    display = ["_"] * len(secret)
    lives = 6
    print(Fore.CYAN + "Color Hangman\n")
    while lives > 0 and "_" in display:
        print(Fore.YELLOW + "Word: " + " ".join(display))
        print(Fore.MAGENTA + f"Lives: {lives}")
        guess = input(Fore.GREEN + "Enter letter: ").lower()
        if guess in secret:
            for i in range(len(secret)):
                if secret[i] == guess:
                    display[i] = guess
        else:
            lives -= 1
            print(Fore.RED + "Wrong")
    if "_" not in display:
        print(Fore.GREEN + "You Win!")
    else:
        print(Fore.RED + "You Lost! Word: " + secret)

def difficulty_game():
    words = {
        "easy": ["cat", "dog", "sun", "cup"],
        "medium": ["python", "planet", "driver", "school"],
        "hard": ["developer", "internet", "hangman", "computer"]
    }
    level = input("Choose difficulty (easy/medium/hard): ").lower()
    secret = random.choice(words[level])
    display = ["_"] * len(secret)
    lives = {"easy": 10, "medium": 7, "hard": 5}[level]
    print("Difficulty Mode:", level)
    while lives > 0 and "_" in display:
        print("Word:", " ".join(display))
        print("Lives:", lives)
        guess = input("Enter a letter: ").lower()
        if guess in secret:
            for i in range(len(secret)):
                if secret[i] == guess:
                    display[i] = guess
        else:
            lives -= 1
    if "_" not in display:
        print("You Win!")
    else:
        print("You Lost! Word:", secret)

def gui_game():
    words = ["python", "developer", "hangman", "internet"]
    secret = random.choice(words)
    display = ["_"] * len(secret)
    lives = 6

    def guess_letter():
        nonlocal lives
        letter = entry.get().lower()
        entry.delete(0, tk.END)
        if letter in secret:
            for i in range(len(secret)):
                if secret[i] == letter:
                    display[i] = letter
        else:
            lives -= 1
        word_label.config(text=" ".join(display))
        lives_label.config(text=f"Lives: {lives}")
        if "_" not in display:
            result_label.config(text="You Win!")
        elif lives == 0:
            result_label.config(text=f"You Lost! Word: {secret}")

    root = tk.Tk()
    root.title("Hangman")
    root.geometry("300x300")

    word_label = tk.Label(root, text=" ".join(display), font=("Arial", 20))
    word_label.pack(pady=10)

    lives_label = tk.Label(root, text=f"Lives: {lives}", font=("Arial", 14))
    lives_label.pack()

    entry = tk.Entry(root, font=("Arial", 14))
    entry.pack()

    button = tk.Button(root, text="Guess", command=guess_letter)
    button.pack(pady=10)

    result_label = tk.Label(root, text="", font=("Arial", 16))
    result_label.pack()

    root.mainloop()

print("1. ASCII Hangman")
print("2. Colored Hangman")
print("3. Difficulty Mode")
print("4. GUI Hangman")
choice = input("Choose option: ")

if choice == "1":
    ascii_game()
elif choice == "2":
    color_game()
elif choice == "3":
    difficulty_game()
elif choice == "4":
    gui_game()
else:
    print("Invalid choice")
