# === Stage 31: Добавь переключение активного пользовательского профиля ===
# Project: MeetingVault
class Profile:
    def __init__(self, name, role, color):
        self.name = name
        self.role = role
        self.color = color

    def __repr__(self):
        return f"Profile({self.name}, {self.role})"


class MeetingVault:
    _profiles = []
    _current_profile = None

    def __init__(self):
        MeetingVault._profiles = [
            Profile("Иван Иванов", "Председатель", "#4CAF50"),
            Profile("Мария Петрова", "Секретарь", "#2196F3"),
            Profile("Алексей Сидоров", "Член", "#FF9800"),
        ]
        MeetingVault._current_profile = MeetingVault._profiles[0]

    @classmethod
    def list_profiles(cls):
        return cls._profiles

    @classmethod
    def switch_profile(cls, name):
        if not MeetingVault._current_profile:
            MeetingVault._current_profile = MeetingVault._profiles[0]
        for p in cls._profiles:
            if p.name == name:
                MeetingVault._current_profile = p
                print(f"\nПрофиль переключен: {p.name} ({p.role}, {p.color})")
                return True
        print(f"Профиль '{name}' не найден. Доступные: {[p.name for p in cls._profiles]}")
        return False

    @classmethod
    def get_current_profile(cls):
        return MeetingVault._current_profile
