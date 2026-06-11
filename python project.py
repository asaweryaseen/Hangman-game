import random

# 30 words with hints (Food + Fashion + Movies + Avengers)
words_with_hints = [
    ("burger", "🍔 A famous fast food item."),
    ("pizza", "🍕 Round, cheesy and delicious."),
    ("biryani", "🍚 Famous spicy rice dish."),
    ("pasta", "🍝 Italian noodles with sauce."),
    ("sandwich", "🥪 Bread filled with yummy things."),
    ("fries", "🍟 Potato snack, served with burgers."),
    ("samosa", "🥟 Triangle shaped snack."),
    ("taco", "🌮 Mexican folded food."),
    ("chocolate", "🍫 Sweet treat loved by all."),
    ("noodles", "🍜 Long thin strands to slurp."),

    ("jeans", "👖 Everyday casual pants."),
    ("jacket", "🧥 Warm outerwear for winters."),
    ("hoodie", "🧢 Sweatshirt with a hood."),
    ("sneakers", "👟 Cool and comfy shoes."),
    ("sunglasses", "🕶️ Stylish eye protection."),
    ("bracelet", "📿 Stylish hand jewelry."),
    ("scarf", "🧣 Stylish wrap around neck."),
    ("handbag", "👜 Carried to keep things."),
    ("backpack", "🎒 Worn on back, for school."),
    ("heels", "👠 Fancy footwear for women."),

    ("avatar", "🎬 Sci-fi movie about blue aliens."),
    ("inception", "🌀 Dream inside a dream movie."),
    ("joker", "🃏 Story of Batman’s villain."),
    ("titanic", "🚢 Love story on a sinking ship."),
    ("gladiator", "⚔️ Roman warrior movie."),
    
    # Avengers addition starts here
    ("ironman", "🛡️ Genius billionaire superhero in red armor."),
    ("thor", "⚡ God of Thunder with a hammer."),
    ("hulk", "💚 Big green smashing hero."),
    ("blackwidow", "🕷️ Skilled female spy and fighter."),
    ("thanos", "💀 Mad Titan who snapped fingers.")
]

# Randomly pick a word and hint
chosen_word, hint = random.choice(words_with_hints)

# Hide the word with underscores
word_display = ["_" for _ in chosen_word]

# Maximum wrong guesses allowed
guesses_left = 6

# List to store guessed letters
guessed_letters = []

print("🎉 Welcome to Hangman Game - Fashion, Food, Movies & Avengers Edition! 🎉")
print(f"🔍 Hint: {hint}")

# Game loop
while guesses_left > 0 and "_" in word_display:
    print("\nWord: ", " ".join(word_display))
    print(f"Guesses left: {guesses_left}")
    
    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("⚠️ Please enter only one valid letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
    elif guess in chosen_word:
        print("✅ Correct guess!")
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                word_display[i] = guess
    else:
        print("❌ Wrong guess!")
        guesses_left -= 1

    guessed_letters.append(guess)

# Check if player won or lost
if "_" not in word_display:
    print("\n🎉 Congratulations! You guessed the word:", chosen_word)
else:
    print("\n💀 Game Over! The word was:", chosen_word)