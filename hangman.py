import random

GREEN = '\033[92m'
RED = '\033[91m'
CYAN = '\033[96m'
YELLOW = '\033[93m'
RESET = '\033[0m'

words = ['apple', 'tiger', 'house', 'robot', 'chair']
word_to_guess = random.choice(words)
guessed_word = ['_'] * len(word_to_guess)
guessed_letters = []
incorrect_guesses = 0
max_incorrect = 6

def display_status():
    print(f"\n🔤 Word: {' '.join(guessed_word)}")
    print(f"🔁 Guessed Letters: {', '.join(guessed_letters) if guessed_letters else 'None'}")
    print(f"❤️ Lives Left: {RED}{'❤' * (max_incorrect - incorrect_guesses)}{RESET}\n")

print(CYAN + "\n🎮 WELCOME TO HANGMAN! 🎮" + RESET)
print("Guess the word one letter at a time.")
print(f"{YELLOW}You have {max_incorrect} lives. Good luck!{RESET}\n")

while incorrect_guesses < max_incorrect and '_' in guessed_word:
    display_status()
    guess = input("➡️  Enter a letter: ").lower()

    if not guess.isalpha() or len(guess) != 1:
        print(RED + "⚠️ Please enter a single valid letter!" + RESET)
        continue

    if guess in guessed_letters:
        print(YELLOW + "❗ You've already guessed that letter." + RESET)
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print(GREEN + f"✅ Great! '{guess}' is in the word!" + RESET)
        for idx, char in enumerate(word_to_guess):
            if char == guess:
                guessed_word[idx] = guess
    else:
        incorrect_guesses += 1
        print(RED + f"❌ Oops! '{guess}' is not in the word." + RESET)

#end
print("\n" + ("🏆" * 10))

if '_' not in guessed_word:
    print(GREEN + f"🎉 Congratulations! You guessed it right: {''.join(guessed_word)}" + RESET)
else:
    print(RED + f"💀 Game Over! The word was: {word_to_guess}" + RESET)

print("Thanks for playing Hangman! 👋")
print(("🏆" * 10) + "\n")
