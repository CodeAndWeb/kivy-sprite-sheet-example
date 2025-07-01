import kivy
kivy.require('2.1.0')

from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.floatlayout import FloatLayout
from kivy.core.window import Window
from kivy.atlas import Atlas
from kivy.clock import Clock
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
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        # Load animation frames
        self.frames = frames_for_animation("assets-optimized/cityscene", "capguy_walk_")
        self.frame_count = len(self.frames)
        self.frame_duration = 1.0 / FRAME_RATE

        # Setup widget properties
        self.size_hint = (None, None)
        self.source = self.frames[0]
        
        # Bind to texture to set size when available
        self.bind(texture=self._on_texture)  # type: ignore[attr-defined]
        
        # Initialize position
        self.x = -self.width  # Start off-screen left
        self.y = DEFAULT_Y_POSITION
        
        # Animation step tracking
        self.step = 0
        screen_distance = Window.width + (2 * self.width)
        self.total_steps = int(screen_distance / PIXELS_PER_FRAME)
        
        # Schedule timer-based updates
        Clock.schedule_interval(self._update, self.frame_duration)

    def _update(self, dt):
        """Update sprite frame and position on each clock tick."""
        self.step += 1
        
        # Update sprite frame
        frame_idx = self.step % self.frame_count
        self.source = self.frames[frame_idx]
        
        # Update position
        self.x = -self.width + (self.step * PIXELS_PER_FRAME)
        
        # Loop back when reaching the end
        if self.step >= self.total_steps:
            self.step = 0
            self.x = -self.width

    def _on_texture(self, instance, texture):
        """Set widget size once texture is loaded."""
        self.size = texture.size

class CitySceneApp(App):
    def build(self) -> FloatLayout:
        root = FloatLayout()
        
        # Add background image
        background = Image(
            source='atlas://assets-optimized/cityscene/background',
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
