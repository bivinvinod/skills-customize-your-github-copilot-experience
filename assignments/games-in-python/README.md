
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Build a classic Hangman game using Python strings, loops, conditional logic, and user input.

## 📝 Tasks

### 🛠️ Game Setup and Word Selection

#### Description
Create a list of hidden words and randomly choose one word at the start of the game.

#### Requirements
Completed program should:

- Define a list of possible words for the game.
- Use `random.choice()` to select the hidden word.
- Start the game with the chosen word hidden from the player.

### 🛠️ Player Guessing and Progress Display

#### Description
Allow the player to guess letters and show the current word progress in a `_ _ _` format.

#### Requirements
Completed program should:

- Accept a single letter guess from the player.
- Reveal correctly guessed letters in the word.
- Display remaining letters as underscores separated by spaces.
- Show the current progress after each guess.

### 🛠️ Guess Tracking and Game End

#### Description
Track incorrect guesses, limit attempts, and end the game with a win or loss message.

#### Requirements
Completed program should:

- Keep a count of incorrect guesses.
- Limit the number of wrong attempts.
- End the game when the player guesses the whole word or runs out of attempts.
- Display a clear win message when the word is solved.
- Display a clear loss message when attempts are exhausted.
