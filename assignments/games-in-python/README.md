
# 📘 Assignment: Hangman Game Challenge

## 🎯 Objective

Practice Python fundamentals by building a classic Hangman game using strings, loops, conditionals, user input, and random selection.

## 📝 Tasks

### 🛠️ Build the Core Hangman Game

#### Description
Create a game where a player guesses letters to reveal a hidden word before running out of attempts.

#### Requirements
Completed program should:

- Randomly choose a word from a predefined list.
- Display the hidden word using underscores, such as _ _ _ _ _.
- Accept one letter at a time from the user.
- Reveal correctly guessed letters in the correct positions.
- Keep track of incorrect guesses and remaining attempts.
- End the game when the player wins or runs out of chances.
- Print a clear win or lose message at the end.

### 🛠️ Improve the Player Experience

#### Description
Add feedback and game flow so the player can easily understand what is happening while they play.

#### Requirements
Completed program should:

- Show the guessed letters so the player can track their progress.
- Tell the player when a letter is already guessed or not in the word.
- Update the display after each guess.
- Use simple, readable output messages for each round.
- Include a short example of gameplay in the program comments or console output.

Example gameplay:

```python
Word: _ _ _ _ _
Guess a letter: a
Good guess! The letter 'a' is in the word.
Word: _ a _ _ _
```
