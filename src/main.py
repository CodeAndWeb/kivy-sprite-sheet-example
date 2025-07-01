"""Kivy application that animates a character across a city scene background."""

import kivy
kivy.require("2.3.0")

from kivy.atlas import Atlas
from kivy.app import App
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.image import Image


def frames_for_animation(atlas_path: str, prefix: str) -> list[str]:
    """Return frame source URIs from a Kivy atlas."""
    atlas = Atlas(f"{atlas_path}.atlas")
    keys = sorted(k for k in atlas.textures if k.startswith(prefix))
    return [f"atlas://{atlas_path}/{key}" for key in keys]


# Animation constants
FRAME_RATE = 6.0  # Frames per second
PIXELS_PER_FRAME = 24.0  # Pixels per frame movement


class AnimatedCharacter(Image):
    """Image widget that cycles through frames to animate a character."""

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.frames = frames_for_animation(
            "assets-optimized/cityscene", "capguy_walk_"
        )
        # start position, initial frame
        self.x = -self.width
        self.y = 240
        self.frame_index = 0
        self.size_hint = (None, None)
        self.source = self.frames[self.frame_index]
        self.bind(texture=self._on_texture)  
        # schedule updates
        Clock.schedule_interval(self._update, 1.0 / FRAME_RATE)

    def _update(self, dt: float) -> None:
        """Advance frame and position each tick."""
        self.frame_index = (self.frame_index + 1) % len(self.frames)
        self.source = self.frames[self.frame_index]
        self.x += PIXELS_PER_FRAME
        if self.x >= Window.width + 2 * self.width:
            self.x = -self.width

    def _on_texture(self, instance, texture) -> None:
        """Set image size when texture loads."""
        self.size = texture.size


class CitySceneApp(App):
    """Kivy application to display the animated city scene."""

    def build(self):
        layout = FloatLayout()
        background = Image(
            source="atlas://assets-optimized/cityscene/background",
            fit_mode="fill",
        )
        layout.add_widget(background)
        layout.add_widget(AnimatedCharacter())
        return layout

if __name__ == "__main__":
    CitySceneApp().run()
