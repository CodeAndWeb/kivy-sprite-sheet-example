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

- `src/main.py` - Main application with AnimatedCharacter class
- `assets-optimized/` - Processed game assets
  - `cityscene.atlas` - Sprite sheet texture atlas
  - `cityscene.png` - Packed sprite sheet image
- `assets-raw/` - Source sprite images organized by character/animation
  - `cityscene.tps` - TexturePacker project file
  - `cityscene/` - Raw sprite images
