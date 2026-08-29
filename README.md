# 👾 Alien Invasion Game

A 2D Arcade Space Shooter built using **Python** and **Pygame**. Control your ship, dodge descending alien fleets, and shoot them down through multiple difficulty stages!

---

## 🌟 Features

- **🛸 Multi-Row Alien Fleet**: Battles multiple rows of descending alien invaders.
- **⚡ 3 Difficulty Stages**:
  - **Stage 1 (Easy)**: Relaxed alien speed.
  - **Stage 2 (Medium)**: Faster alien speed.
  - **Stage 3 (Hard)**: Rapid alien speed challenge!
- **📊 Real-time HUD**: Displays your current **Score** (top-center) and **Stage** (top-left).
- **💥 Collision & Game Over**: Full collision detection between bullets, aliens, and the player ship body.
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
