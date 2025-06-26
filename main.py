import kivy
kivy.require('2.1.0')
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import NumericProperty
from kivy.core.window import Window
from kivy.atlas import Atlas
from kivy.animation import Animation
from typing import List

# Animation constants
FRAME_RATE = 6.0  # frames per second
PIXELS_PER_FRAME = 24  # How many pixels to move per frame change
DEFAULT_Y_POSITION = 240

def frames_for_animation(atlas_path: str, prefix: str) -> List[str]:
    """Return a list of frame sources from a Kivy atlas for animation."""
    atlas = Atlas(atlas_path + ".atlas")
    frame_keys = sorted([k for k in atlas.textures.keys() if k.startswith(prefix)])
    return [f"atlas://{atlas_path}/{k}" for k in frame_keys]

class AnimatedCharacter(Image):
    
    frame_index = NumericProperty(0)
    
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Load animation frames
        self.frames = frames_for_animation("cityscene", "capguy_walk_")
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
        
        # Start the animation
        self.start_animation()
    
    def start_animation(self) -> None:
        """Start the frame animation which drives both sprite frames and movement."""
        self.frame_index = 0
        
        # Calculate total frames needed to cross the screen
        screen_distance = Window.width + (2 * self.width)  # From off-screen left to off-screen right
        total_frames_needed = int(screen_distance / PIXELS_PER_FRAME)
        
        # Create animation that cycles through frames for the duration needed
        animation_duration = total_frames_needed * self.frame_duration
        
        self.animation = Animation(
            frame_index=total_frames_needed,
            duration=animation_duration,
            transition='linear'
        )
        self.animation.bind(on_complete=self.on_animation_complete)
        self.animation.start(self)
    
    def on_animation_complete(self, animation: Animation, character: 'AnimatedCharacter') -> None:
        """Restart animation when it completes."""
        # Reset position to start
        self.x = -self.width
        self.start_animation()
    
    def on_frame_index(self, instance: 'AnimatedCharacter', value: float) -> None:
        """Update both sprite frame and position when frame_index changes."""
        # Update sprite frame (cycle through available frames)
        frame_idx = int(value) % self.frame_count
        self.source = self.frames[frame_idx]
        
        # Update position - move character based on frame progression
        frame_step = int(value)
        new_x = -self.width + (frame_step * PIXELS_PER_FRAME)
        self.x = new_x

class CitySceneApp(App):
    def build(self) -> FloatLayout:
        root = FloatLayout()
        
        # Add background image
        background = Image(
            source='atlas://cityscene/background',
            fit_mode="fill",
            size_hint=(1, 1),
            pos_hint={'x': 0, 'y': 0}
        )
        root.add_widget(background)
        
        # Add animated character
        character = AnimatedCharacter()
        root.add_widget(character)
        
        return root

if __name__ == '__main__':
    CitySceneApp().run()