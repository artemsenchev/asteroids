# Asteroids Game: Object-Oriented Programming Practice

This repository contains an implementation of a classic **Asteroids-style game**, built using Python and Pygame. The project was developed to practice object-oriented programming (OOP) principles and multi-file Python project organization.

---

## Prerequisites

To run this project, ensure you have the following:
- **Python 3.10+** installed
- Access to a Unix-like shell (e.g., zsh or bash)
- A virtual environment configured with the following dependency:
  
```bash
pygame==2.6.1
```

### Setting Up the Environment

To set up the virtual environment and install dependencies, use the following commands:
```bash
$ python -m venv venv
$ source venv/bin/activate
$ pip install pygame==2.6.1
```

---

## Learning Objectives

The primary objectives of this project are:
1. To gain experience working with multi-file Python projects.
2. To explore practical applications of object-oriented programming concepts.
3. To develop a functional game while focusing on clean, modular code design.

---

## Features Implemented

The game includes the following features:
- **Player Movement**: Controlled via WASD or arrow keys.
- **Asteroid Collisions**: The player can collide with asteroids, leading to the game-ending condition.
- **Shooting Mechanic**: Players can shoot projectiles at asteroids, with rate limiting implemented.
- **Asteroid Destruction**: Asteroids are destroyed upon collision with a projectile.
- **Asteroid Splitting**:
  - Large asteroids split into two medium-sized asteroids.
  - Medium-sized asteroids split into two small ones.
  - Small asteroids disappear when destroyed.

---

## Possible Extensions

While the current implementation is functional, there are several opportunities for future enhancements:
- **Scoring System**: Add a scoring mechanism to track player performance.
- **Lives and Respawning**: Implement multiple lives and respawn functionality.
- **Explosion Effects**: Add visual effects for asteroid destruction.
- **Acceleration**: Introduce acceleration mechanics for smoother player movement.
- **Screen Wraparound**: Make objects wrap around the screen edges rather than disappearing.
- **Background Enhancements**: Add a background image or dynamic visuals.
- **Weapon Variety**: Implement different types of weapons with unique behaviors.
- **Improved Collision Models**: Replace circular hitboxes with more precise shapes (e.g., triangular for the ship).
- **Power-Ups**: Introduce power-ups such as shields, speed boosts, or bombs.

---

## Technical Overview

The game loop runs at a fixed frame rate of 60 FPS to ensure smooth gameplay. Player movement is handled via sprites, with the ship represented as a triangle rendered within a circular hitbox for simplicity. Collision detection is implemented to handle interactions between the player, projectiles, and asteroids.

---

## Conclusion

This project demonstrates how object-oriented programming principles can be applied effectively in game development using Python and Pygame. It serves as both an educational tool and a foundation for further exploration into more advanced game mechanics and features. 
