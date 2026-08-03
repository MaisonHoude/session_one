# === Stage 30: Добавь поддержку нескольких пользовательских профилей внутри приложения ===
# Project: MeetingVault
class Profile:
    def __init__(self, name, role="user"):
        self.name = name
        self.role = role

    def can_manage(self, meeting):
        return self.role in ("admin", "organizer") or (
            self.role == "participant" and meeting.attendees.get(self.name) is not None
        )


class MeetingVault:
    def __init__(self):
        self.profiles = {}

    def register_profile(self, name, role="user"):
        if name in self.profiles:
            raise ValueError(f"Profile {name!r} already exists")
        self.profiles[name] = Profile(name, role)
        return self.profiles[name]

    def login(self, name):
        profile = self.profiles.get(name)
        if not profile:
            return None
        self._current_profile = profile
        return profile

    @property
    def current_profile(self):
        return getattr(self, "_current_profile", None)

    def can_manage_meeting(self, meeting):
        profile = self.current_profile
        if not profile or profile.role == "user":
            return False
        attendees = {p.name for p in meeting.attendees}
        return profile.name in attendees or profile.role == "admin"


class Meeting:
    def __init__(self, title):
        self.title = title
        self.attendees = {}

    @property
    def attendees_dict(self):
        return {p.name for p in self.attendees}
