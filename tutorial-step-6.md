# Step 6: Creating an animated character

Let's now create an animated character that walks from left to right. For this, we use the
`Animation()` class provided by Kivy.

### Animation helper function

This short function grabs all animation frames from an atlas and returns them
in order:

```python
def frames_for_animation(atlas_path: str, prefix: str) -> List[str]:
    """Return a list of frame sources from a Kivy atlas for animation."""
    atlas = Atlas(atlas_path + ".atlas")
    frame_keys = sorted([k for k in atlas.textures.keys() if k.startswith(prefix)])
    return [f"atlas://{atlas_path}/{k}" for k in frame_keys]
```

You can use it this way

```python
frames_for_animation("assets-optimized/cityscene", "capguy_walk_")
```

The first parameter is the atlas to use, the second the prefix of the animation.
Note that texturepacker converts the frame names by concatenating folders with `_` and
omitting the file name extension. E.g. `capguy/walk/0001.png` becomes `capguy_walk_0001`.

### The animated character class


```python

class AnimatedCharacter(Image):
    
    frame_index = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Load animation frames
        self.frames = frames_for_animation("assets-optimized/cityscene", "capguy_walk_")
        self.frame_count = len(self.frames)
        self.frame_duration = 1.0 / FRAME_RATE

        # Setup widget properties
        self.size_hint = (None, None)
        self.source = self.frames[0]
        
        # Set size based on texture
        self.size = self.texture.size
        
        # Initialize position
        self.x = -self.width  # Start off-screen left
        self.y = DEFAULT_Y_POSITION
        self.total_cycles = 0  # Track animation cycles
        
        # Start the animation
        self.start_animation()
    
    def start_animation(self) -> None:
        """Start the frame animation which drives both sprite frames and movement."""
        self.frame_index = 0
                        
        self.animation = Animation(
            frame_index=self.frame_count,
            duration=self.frame_count / FRAME_RATE,
            transition='linear'
        )
        self.animation.bind(on_complete=self.on_animation_complete)
        self.animation.start(self)
    
    def on_animation_complete(self, animation: Animation, character: 'AnimatedCharacter') -> None:
        """Restart animation when it completes."""
        self.total_cycles += 1
        self.start_animation()
    
    def on_frame_index(self, instance: 'AnimatedCharacter', value: float) -> None:
        """Update both sprite frame and position when frame_index changes."""
        # Update sprite frame (cycle through available frames)
        frame_idx = int(value) % self.frame_count
        self.source = self.frames[frame_idx]
        
        # Update position - calculate cumulative position across all cycles
        total_frames = self.total_cycles * self.frame_count + int(value)
        new_x = -self.width + total_frames * PIXELS_PER_FRAME
        
        # Reset when character goes off-screen right
        if new_x > Window.width:
            self.total_cycles = 0
            new_x = -self.width
 
        self.x = new_x
```