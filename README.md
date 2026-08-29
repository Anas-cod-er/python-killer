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
  - [Settings Module](#settings-module)
  - [Ship Module](#ship-module)
  - [Bullet Module](#bullet-module)
  - [Alien Module](#alien-module)
  - [Scoreboard Module](#scoreboard-module)
  - [Game Functions Module](#game-functions-module)
  - [Main Game Module](#main-game-module)

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
| ← / → | Move ship left / right |
| ↑ / ↓ | Move ship up / down |
| SPACE | Fire bullet |
| 1 | Easy difficulty |
| 2 | Medium difficulty |
| 3 | Hard difficulty |
| Q | Quit game |

---

## 🎚️ Difficulty Levels

| Level | Name | Alien Speed | Description |
|-------|------|-------------|-------------|
| 1 | Easy | 0.5 | Slowest aliens, perfect for beginners |
| 2 | Medium | 1.0 | Moderate speed, balanced challenge |
| 3 | Hard | 1.8 | Fastest aliens, extreme difficulty |

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

**Class: `Settings`**

| Method | Purpose |
|--------|---------|
| `__init__()` | Initialize game settings (screen size, speeds, bullet/alien properties) |
| `set_stage(stage_num)` | Change difficulty level and update alien speed (1=Easy, 2=Medium, 3=Hard) |

**Key Attributes:**
- `screen_width`, `screen_height`: Display dimensions (1200×800)
- `ship_speed_factor`: Player movement speed (1.5)
- `bullet_speed_factor`: Projectile speed (1.0)
- `alien_speed_factor`: Enemy speed based on current stage
- `bullet_allowed`: Max bullets on screen (3)

---

### Ship Module (`ship.py`)

Player-controlled spaceship with 4-directional movement.

**Class: `Ship`**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen)` | Load ship image, set initial position (bottom center) |
| `update()` | Update position based on movement flags, keep within screen bounds |
| `blitme()` | Draw ship sprite to screen |

**Movement Flags:**
- `moving_left`, `moving_right`, `moving_up`, `moving_down` — Set by keyboard input

---

### Bullet Module (`bullet.py`)

Projectiles fired by the ship, moving upward.

**Class: `Bullet(Sprite)`**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen, ship)` | Create bullet at ship position with upward velocity |
| `update()` | Move bullet up by `speed_factor` |
| `draw_bullet()` | Render bullet rectangle to screen |

**Properties:** Speed (1.0), Color (black), Max on screen (3)

---

### Alien Module (`alien.py`)

Enemy aliens that descend from top of screen.

**Class: `Alien(Sprite)`**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen)` | Load alien image (90×90), set initial position |
| `update()` | Move alien down by `alien_speed_factor` |
| `blitme()` | Draw alien sprite to screen |

**Movement:** Aliens move downward; when reaching bottom, they wrap back to top

---

### Scoreboard Module (`scoreboard.py`)

Displays score and current difficulty level in top corners.

**Class: `Scoreboard`**

| Method | Purpose |
|--------|---------|
| `__init__(ai_settings, screen)` | Initialize fonts and render initial score/stage |
| `prep_score()` | Render score text with shadow, position at top center |
| `prep_stage()` | Render stage text with shadow, position at top left |
| `show_score()` | Draw both score and stage to screen |

**Display:** White text with black shadow for visibility

---

### Game Functions Module (`game_fuction.py`)

Core game logic, event handling, and collision detection.

**Event Handlers:**

| Function | Purpose |
|----------|---------|
| `check_keydown_events(event, ship, ...)` | Handle key presses (arrows, space, 1-3, Q) |
| `check_keyup_events(event, ship)` | Handle key releases (clear movement flags) |
| `check_events(ship, ai_settings, ...)` | Main event dispatcher |

**Fleet Management:**

| Function | Purpose |
|----------|---------|
| `create_fleet(ai_settings, screen, ship, aliens)` | Generate grid of aliens filling screen |
| `create_alien(ai_settings, screen, aliens, alien_number, row_number)` | Spawn single alien at position |
| `get_number_aliens_x(ai_settings, alien_width)` | Calculate aliens per row |
| `get_number_rows(ai_settings, ship_height, alien_height)` | Calculate number of rows |
| `check_aliens_bottom(ai_settings, screen, aliens)` | Wrap aliens from bottom to top |

**Game Updates:**

| Function | Purpose |
|----------|---------|
| `update_aliens(ai_settings, screen, ship, aliens)` | Move aliens, check ship collision, end game if hit |
| `update_bullets(ai_settings, screen, ship, aliens, bullets, sb)` | Move bullets, detect alien hits, update score |
| `update_screen(ai_setting, screen, ship, aliens, bullets, sb)` | Render all objects (background, ships, aliens, bullets, score) |

**Game Over:**

| Function | Purpose |
|----------|---------|
| `show_game_over(screen)` | Display "GAME OVER" message and exit after 2 seconds |

---

### Main Game Module (`alien_invasion.py`)

Entry point and main game loop.

**Function: `run_game()`**

Initializes Pygame, creates all game objects, and runs the main loop:
1. Initialize Pygame
2. Create settings, screen, and scoreboard
3. Create player ship and sprite groups
4. Generate initial alien fleet
5. **Main Loop:**
   - Check events (player input)
   - Update ship position
   - Update bullets and collisions
   - Update aliens and check ship collision
   - Render screen

---

## 🐛 Troubleshooting

**Game won't start?**
- Ensure all image files (ship.png, py.png, bg-image.png) are in the same directory as the Python files
- Verify Pygame is installed: `pip install pygame`

**Images not showing?**
- Check that image file names match exactly (case-sensitive on some systems)
- Ensure images are in PNG format and not corrupted

**Game is too slow/fast?**
- Adjust `ship_speed_factor`, `bullet_speed_factor`, and `alien_speed_factor` in `settings.py`

---

## 🎓 Learning Outcomes

This project demonstrates:
- Object-oriented programming with classes
- Pygame library usage for graphics and game loops
- Collision detection algorithms
- Event-driven programming
- Sprite management with sprite groups
- Game state management

---

## 📝 License

This project is provided as-is for educational purposes.

---

## 🤝 Contributing

Feel free to enhance the game with:
- Power-ups and special weapons
- Sound effects and music
- Multiple lives system
- Persistent high scores
- Animated sprites
- Boss levels

---

**Enjoy the game! 🚀**
- **🎮 Dynamic Controls**: Switch stages manually at any time using numeric keys (`1`, `2`, `3`).

---

## 🎮 Controls

| Action | Key |
| :--- | :--- |
| **Move Left / Right** | `←` / `→` Arrow Keys |
| **Move Up / Down** | `↑` / `↓` Arrow Keys |
| **Fire Bullet** | `Spacebar` |
| **Easy Stage** | `1` |
| **Medium Stage** | `2` |
| **Hard Stage** | `3` |
| **Quit Game** | `Q` |

---

## 🛠️ Installation & Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/YOUR_USERNAME/Alien-Invasion.git
   cd Alien-Invasion
   ```

2. **Install Pygame**:
   ```bash
   pip install pygame
   ```

3. **Run the Game**:
   ```bash
   python alien_invasion.py
   ```

---

## 📁 Project Structure

```
Game/
├── alien_invasion.py  # Main game loop and entry point
├── alien.py           # Alien sprite definition & movement
├── ship.py            # Player ship sprite & controls
├── bullet.py          # Bullet sprite logic
├── game_fuction.py    # Game event handlers & update functions
├── scoreboard.py      # HUD Score & Stage renderer
├── settings.py        # Configurable game settings & stage speeds
└── assets/            # Game images (bg-image.png, ship.png, py.png)
```
#   p y t h o n - k i l l e r 
 
 