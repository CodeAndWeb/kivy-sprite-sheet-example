# Kivy Sprite Sheet Animation Example

A demonstration of sprite sheet animation in Kivy featuring an animated character walking across a city background.

## Features

- **Sprite Sheet Animation**: Uses Kivy Atlas for efficient texture management
- **Smooth Movement**: Character walks continuously across the screen
- **Frame-based Animation**: 8-frame walk cycle at 6 fps
- **Automatic Looping**: Character reappears when reaching screen edge

## Quick Start

### Setting up the environment
```bash
# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install Kivy
pip install kivy==2.3.1

# Run the application
python main.py
```

## Project Structure

- `main.py` - Main application with AnimatedCharacter class
- `cityscene.atlas` - Sprite sheet texture atlas
- `cityscene.png` - Packed sprite sheet image
- `sprites/` - Source sprite images organized by character/animation
    - `cityscene.tps` - TexturePacker project file

## Animation System

The animation uses a single `Animation` object that drives both:
- Sprite frame cycling (8 walk frames)
- Character movement (24 pixels per frame)

Key constants in `main.py`:
- `FRAME_RATE`: 6 fps animation speed
- `PIXELS_PER_FRAME`: 24px movement per frame
- `DEFAULT_Y_POSITION`: 240px vertical position

## Requirements

- Python 3.13
- Kivy 2.3.1 (included in virtual environment)

## Customization

- **Animation Speed**: Modify `FRAME_RATE` in main.py:13
- **Movement Speed**: Modify `PIXELS_PER_FRAME` in main.py:14
- **Character Height**: Modify `DEFAULT_Y_POSITION` in main.py:15