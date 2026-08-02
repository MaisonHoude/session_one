# === Stage 29: Добавь конфигурацию приложения через словарь настроек ===
# Project: MeetingVault
# MeetingVault: Архив встреч с участниками, повесткой, решениями и назначенными действиями
# Этап 29: Конфигурация приложения через словарь настроек

APP_CONFIG = {
    "app_name": "MeetingVault",
    "version": "1.0.0",
    "max_actions_per_meeting": 5,
    "default_action_priority": "normal",
    "allowed_priorities": ["low", "normal", "high"],
    "data_dir": "./meetings_data",
    "log_level": "INFO",
}


def get_config(key=None):
    if key is None:
        return APP_CONFIG.copy()
    return APP_CONFIG.get(key)


print("MeetingVault config loaded:", get_config())
