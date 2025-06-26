# Kivy Sprite Sheet Animation Example

This project demonstrates how to use sprite sheet animation in [Kivy](https://kivy.org/), featuring an animated character walking across a city-themed background.

## Quick Start

### Requirements

- Python **3.13** or later  
  Make sure Python is installed and added to your system’s PATH.

### Setup Instructions

#### Windows

1. Clone this repository  
2. Run `init.bat` to create the virtual environment and install dependencies

#### Linux / macOS

1. Clone this repository  
2. Run `init.sh` to set up the environment

## 📁 Project Structure

```text
.
├── main.py                # Main application file with AnimatedCharacter class
├── cityscene.atlas        # Texture atlas definition (used by Kivy)
├── cityscene.png          # Generated sprite sheet image
├── sprites/               # Source images used for the sprite sheet
│   └── cityscene.tps      # TexturePacker project file
├── init.bat               # Windows setup script
└── init.sh                # macOS/Linux setup script
```

