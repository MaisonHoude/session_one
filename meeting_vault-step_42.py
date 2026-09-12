# === Stage 42: Добавь цветной вывод через ANSI-коды с возможностью отключения ===
# Project: MeetingVault
import sys

COLORS = {
    "reset": "\033[0m",
    "bold": "\033[1m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
}

class Ansi:
    _enabled = True

    @classmethod
    def toggle(cls, on):
        cls._enabled = on

    @classmethod
    def disable(cls):
        cls.toggle(False)

    @classmethod
    def enable(cls):
        cls.toggle(True)

    @classmethod
    def is_enabled(cls):
        return cls._enabled

    @classmethod
    def color(cls, color, text):
        if not cls._enabled:
            return text
        return f"{COLORS.get(color, '')}{text}{COLORS['reset']}"

    @classmethod
    def bold(cls, text):
        return cls.color("bold", text)

    @classmethod
    def title(cls, text):
        return cls.color("cyan", cls.bold(text))

    @classmethod
    def success(cls, text):
        return cls.color("green", text)

    @classmethod
    def error(cls, text):
        return cls.color("red", text)

    @classmethod
    def info(cls, text):
        return cls.color("blue", text)

    @classmethod
    def warn(cls, text):
        return cls.color("yellow", text)
