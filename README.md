# Alien Invasion Game 👾

A fun, interactive space shooter game built with Python and Pygame. Defend your ship from an invading fleet of aliens across three difficulty levels!

---

## 📋 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [How to Play](#how-to-play)
- [Game Controls](#game-controls)
- [Difficulty Levels](#difficulty-levels)
- [Project Structure](#project-structure)
- [Code Documentation](#code-documentation)

---

## 🎮 Overview

Alien Invasion is a classic space shooter where you control a ship at the bottom of the screen and defend against waves of descending aliens. The goal is to survive as long as possible while increasing your score by shooting down aliens.

---

## ✨ Features

- **Three Difficulty Levels**: Easy, Medium, and Hard with adjustable alien speeds
- **Score Tracking**: Real-time score display
- **Dynamic Gameplay**: Aliens spawn in formations and move downward
- **Bullet Limiting**: Maximum of 3 bullets on screen at once
- **Smooth Movement**: 4-directional ship movement (up, down, left, right)
- **Beautiful Graphics**: Custom background image with sprite-based graphics
- **Collision Detection**: Accurate collision detection for bullets hitting aliens and aliens hitting the ship

---

## 🛠️ Installation

### Prerequisites

- Python 3.6 or higher
- Pygame library
- Game assets (ship.png, py.png, bg-image.png)

### Setup Steps

1. **Clone or download the project files**

2. **Install Pygame**
   ```bash
   pip install pygame
   ```

3. **Add game assets** to the project directory:
   - `ship.png` - Ship sprite (player character)
   - `py.png` - Alien sprite
   - `bg-image.png` - Background image (1200x800 recommended)

4. **Run the game**
   ```bash
   python alien_invasion.py
   ```

---

## 🎯 How to Play

1. Start the game by running `alien_invasion.py`
2. Use the arrow keys to move your ship around the screen
3. Press SPACE to shoot bullets at aliens
4. Destroy all aliens to progress through waves
5. Avoid colliding with aliens or the game ends
6. Change difficulty levels using number keys (1, 2, or 3)
7. Press Q to quit the game at any time

---

## ⌨️ Game Controls

| Key | Action |
|-----|--------|
| ← → | Move ship left / right |
| ↑ ↓ | Move ship up / down |
| SPACE | Fire bullet |
| 1 | Easy difficulty |
| 2 | Medium difficulty |
| 3 | Hard difficulty |
| Q | Quit game |

---

## 🎚️ Difficulty Levels

| Level | Name | Speed | Challenge |
|-------|------|-------|-----------|
| 1 | Easy | 0.5 | Perfect for beginners |
| 2 | Medium | 1.0 | Balanced challenge |
| 3 | Hard | 1.8 | Extreme difficulty |

---

## 📁 Project Structure

```
Game/
├── alien_invasion.py       # Main game entry point
├── settings.py             # Game configuration and settings
├── ship.py                 # Player ship class
├── bullet.py               # Bullet projectile class
├── alien.py                # Alien enemy class
├── scoreboard.py           # Score and stage display
├── game_fuction.py         # Core game functions
├── README.md               # This file
├── ship.png                # Ship sprite image
├── py.png                  # Alien sprite image
└── bg-image.png            # Background image
```

---

## 📚 Code Documentation

### Settings Module (`settings.py`)

Configuration class for all game settings.

**Class: Settings**

| Method | Purpose |
|--------|---------|
| `__init__()` | Initialize game settings (screen size, speeds, bullet/alien properties) |
| `set_stage(stage_num)` | Change difficulty level (1=Easy, 2=Medium, 3=Hard) |

**Key Attributes:**
- `screen_width`, `screen_height`: Display dimensions (1200×800)
- `ship_speed_factor`: Player movement speed (1.5 px/frame)
- `bullet_speed_factor`: Projectile speed (1.0 px/frame)
- `alien_speed_factor`: Enemy speed based on current stage
- `bullet_allowed`: Max bullets on screen (3)

---

### Ship Module (`ship.py`)

Player-controlled spaceship with 4-directional movement.

**Class: Ship**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen)` | Load ship image, set initial position |
| `update()` | Update position based on movement flags |
| `blitme()` | Draw ship sprite to screen |

**Movement Flags:**
- `moving_left` / `moving_right` / `moving_up` / `moving_down`

---

### Bullet Module (`bullet.py`)

Projectiles fired by the ship, moving upward.

**Class: Bullet(Sprite)**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen, ship)` | Create bullet at ship position |
| `update()` | Move bullet up |
| `draw_bullet()` | Render bullet to screen |

---

### Alien Module (`alien.py`)

Enemy aliens that descend from top of screen.

**Class: Alien(Sprite)**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen)` | Load alien image (90×90) |
| `update()` | Move alien down |
| `blitme()` | Draw alien sprite to screen |

---

### Scoreboard Module (`scoreboard.py`)

Displays score and difficulty level.

**Class: Scoreboard**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen)` | Initialize fonts and displays |
| `prep_score()` | Render score with shadow |
| `prep_stage()` | Render stage with shadow |
| `show_score()` | Draw score and stage to screen |

---

### Game Functions Module (`game_fuction.py`)

Core game logic, event handling, and collision detection.

**Event Handlers:**
- `check_keydown_events()` - Handle key presses (arrows, space, 1-3, Q)
- `check_keyup_events()` - Handle key releases
- `check_events()` - Main event dispatcher

**Fleet Management:**
- `create_fleet()` - Generate grid of aliens
- `create_alien()` - Spawn single alien
- `get_number_aliens_x()` - Calculate aliens per row
- `get_number_rows()` - Calculate number of rows
- `check_aliens_bottom()` - Wrap aliens from bottom to top

**Game Updates:**
- `update_aliens()` - Move aliens, check ship collision
- `update_bullets()` - Move bullets, detect alien hits, update score
- `update_screen()` - Render all objects to screen
- `show_game_over()` - Display game over message and exit

---

### Main Game Module (`alien_invasion.py`)

Entry point and main game loop.

**Function: run_game()**

Initializes Pygame, creates all game objects, and runs the main loop:

1. Initialize Pygame
2. Create settings, screen, and scoreboard
3. Create player ship and sprite groups
4. Generate initial alien fleet
5. Main Loop:
   - Check events (player input)
   - Update ship position
   - Update bullets and collisions
   - Update aliens
   - Render screen

---

## 🐛 Troubleshooting

**Game won't start?**
- Ensure all image files are in the same directory as Python files
- Verify Pygame is installed: `pip install pygame`

**Images not showing?**
- Check file names match exactly (case-sensitive)
- Ensure images are in PNG format

**Game too slow/fast?**
- Adjust `ship_speed_factor`, `bullet_speed_factor`, or `alien_speed_factor` in `settings.py`

---

## 🎓 Learning Outcomes

This project demonstrates:
- Object-oriented programming with classes
- Pygame library usage for graphics and game loops
- Collision detection algorithms
- Event-driven programming
- Sprite management with groups
- Game state management

---

## 📝 License

Educational project

---

## 🤝 Contributing

Enhance the game with:
- Power-ups and special weapons
- Sound effects and music
- Multiple lives system
- Persistent high scores
- Animated sprites
- Boss levels

---

**Enjoy the game! 🚀**
