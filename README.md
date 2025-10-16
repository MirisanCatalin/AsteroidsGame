# AsteroidsGame 🚀

An authentic, Python-based clone of the classic 1979 arcade game, Asteroids. Navigate your spaceship, destroy incoming asteroids, and survive for the high score!

[![Python](https://img.shields.io/badge/Language-Python-blue.svg)](https://www.python.org/)
[![Game Engine](https://img.shields.io/badge/Engine-Pygame-blue.svg)](https://www.pygame.org/news)
[![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)]()
[![License](https://img.shields.io/badge/License-Unspecified-lightgrey.svg)](#license)

***

## ✨ Features

This game implements core mechanics from the original arcade classic, managed through an Object-Oriented approach:

* **Classic Gameplay:** Control a spaceship with thrust and rotation.
* **Dynamic Asteroids:** Asteroids break into smaller pieces when shot, making the game progressively more challenging.
* **Weapons System:** Standard laser shots and a limited-use **Bomb** mechanic.
* **Power-Ups:** Collect **New Life** drops that randomly spawn.
* **High Score Tracking:** Saves and displays the persistent high score.
* **Visual Effects:** Includes ship thrust effects and asteroid **explosions**.

***

## 🚀 Getting Started

These instructions will get you a copy of the project running on your local machine for development and play.

### Prerequisites

You need **Python 3.x** and the **Pygame** library installed.

```bash
# Install the Pygame library
pip install pygame
```

Installation and Setup

    Clone the repository:
    Bash

git clone [https://github.com/MirisanCatalin/AsteroidsGame.git](https://github.com/MirisanCatalin/AsteroidsGame.git)
cd AsteroidsGame

Run the game:
Bash

    python main.py

Controls

Key	Action
Arrow Up / W	Apply thrust / accelerate forward
Arrow Left / A	Rotate spaceship counter-clockwise
Arrow Right / D	Rotate spaceship clockwise
Spacebar	Fire laser shot
B	Deploy Bomb (limited use)

## 🎓 What I Learned

Developing an Asteroids clone was a significant step in my programming journey, providing hands-on experience with fundamental game development concepts:

# 1. Game Loop Implementation

I mastered the fundamental structure of all video games: the Game Loop (Input → Update State → Render). This ensures smooth, consistent frame rates and responsive gameplay.

# 2. Object-Oriented Programming (OOP)

The project is built entirely using OOP, which was essential for managing complexity:

    Classes and Inheritance: Created separate, self-contained classes for every entity (e.g., Player, Asteroid, Laser, Explosion).

    Entity Management: Developed systems within main.py and asteroidfield.py to efficiently create, update, and destroy game objects.

# 3. 2D Physics and Vector Math

I applied principles of vector mathematics to create realistic motion:

    Thrust and Acceleration: Implemented logic for the player ship to accelerate and decelerate based on thrust in the direction of rotation.

    Rotation: Calculated rotation and applied it to the ship's direction of movement and its visual sprite.

    Wrapping: Implemented screen wrapping (torus physics) so objects disappear on one side of the screen and reappear on the opposite side.

# 4. Collision Detection

I implemented the logic necessary to detect when two objects occupy the same space:

    Circle Collision: Used mathematical formulas to check for collisions between circular hitboxes (player, asteroids, bullets).

    Collision Response: Handled outcomes like scoring points, destroying bullets, and splitting asteroids into smaller pieces.

# 5. Game State and Persistence

I learned how to manage crucial game data:

    State Tracking: Managed player lives, current score, and game mode (playing, game over).

    Data Persistence: Used File I/O to load and save the high score permanently via highscore.txt.

## 🛠️ Built With

    Python – Core language

    Pygame – Primary library for 2D graphics, input handling, and sound

## 🤝 Acknowledgements

This project was a major milestone in my journey into game development, allowing me to translate mathematical and OOP concepts into a functional, interactive experience.
