# CATCH.PY
#### Video Demo:  https://youtu.be/-blMNPSoEiY

CATCH.PY is an retro fruit-catcher game developed using pygame. The objective is to catch apples using a basket while avoiding bombs. The game features power-ups and an increasing challenge as the player progresses.

## Features
- **Basket Movement:** Control the basket to catch falling apples while dodging bombs.
- **Falling Objects:**
  - **Apples:** Red apples increase your score.
  - **Golden Apples:** Restore full health (lives).
  - **Bombs & Diagonal Bombs:** Instantly end the game.
  - **Magnet:** Attracts apples to your basket for 6 seconds.
- **Game Over Condition:** The game ends when you run out of hearts or hit a bomb.
- **Difficulty:** Bombs fall faster as your score increases.
- **Pause Feature:** Pause the game anytime by pressing the **Spacebar**.
- **Background Music:** Enjoy immersive gameplay with continuous 8-bit themed background music.


## Requirements
```bash
pip install pygame
```

### How to Play?
Execute the following command in your terminal:
```bash
python project.py
```


## Keyboard Controls
- Left Arrow --> Move the basket left
- Right Arrow --> Move the basket right
- Spacebar  --> Pause/Resume game


## Rules
- **Catch the apples** to score points.
- **Avoid bombs** to stay in the game.
- **Golden apples** replenish all lives if you have less than 3 hearts.
- **Magnets** attract apples to your basket.
- **Game Over:**
  - Running out of hearts.
  - Catching a bomb.

---

## Powerups
| Object | Effect |
|--------|--------|
| Apple | +1 point |
| Golden Apple | Restores all hearts (if below 3) |
| Bomb | Ends the game instantly |
| Diagonal Bomb | Moves sideways and falls faster |
| Magnet | Attracts apples to your basket for 6 seconds |


## Screens
### In-Game Screen
- **Score Display** - Shows the current score at the top left.
- **Lives Display** - Hearts represent remaining lives at the top right.

### Pause Screen
- Displays a pause icon when the game is paused.
- Press **Spacebar** to resume.

### Game Over Screen
- Shows final score.
- Option to restart the game by pressing **Spacebar**.
- Shows my authorship data

## Restart
- Press **Spacebar** on the **Game Over Screen** to restart the game.


## Scoring & Difficulty Progression
- Every **20 points**, bomb falling speed increases slightly.
- The game progressively becomes more challenging as your score rises.


## Code Structure
```
CATCH.PY
│-- project.py      # main game file
|-- test_project.py # pytest file
│-- images.py       # Handles image loading
│-- images/         # Directory containing game assets
│-- music.mp3       # Background music file
```


## Authorship
Developed by **Taskin Saadman**
- GitHub: [taskin-saadman](https://github.com/taskin-saadman)
