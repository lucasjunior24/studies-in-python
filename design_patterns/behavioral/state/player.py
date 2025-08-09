from __future__ import annotations
from abc import abstractmethod


class IPlayMode:
    @abstractmethod
    def press_next(self) -> None:
        pass

    @abstractmethod
    def press_prev(self) -> None:
        pass


class RadioMode(IPlayMode):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    def press_next(self) -> None:
        self.sound.playing += 1000

    def press_prev(self) -> None:
        self.sound.playing -= 1000 if self.sound.playing > 0 else 0


class MusicMode(IPlayMode):
    def __init__(self, sound: Sound) -> None:
        self.sound = sound

    def press_next(self) -> None:
        self.sound.playing += 1

    def press_prev(self) -> None:
        self.sound.playing -= 1 if self.sound.playing > 0 else 0


class Sound:
    def __init__(self) -> None:
        self.mode: RadioMode | MusicMode = RadioMode(self)
        self.playing = 0

    def change_mode(self, mode: IPlayMode) -> None:
        print(f"Mudando para: {mode.__class__.__name__}")
        self.mode = mode
        self.playing = 0

    def press_next(self) -> None:
        self.mode.press_next()
        print(self)

    def press_prev(self) -> None:
        self.mode.press_prev()
        print(self)

    def __str__(self) -> str:
        return str(self.playing)


if __name__ == "__main__":
    sound = Sound()
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()

    print()
    sound.change_mode(MusicMode(sound))
    sound.press_next()
    sound.press_next()
    sound.press_next()
    sound.press_prev()
    sound.press_next()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
    sound.press_prev()
