# === Stage 26: Добавь набор демо-команд для быстрого ручного тестирования ===
# Project: MeetingVault
import json, sys
from MeetingVault import MeetingVault

def main():
    vault = MeetingVault()
    
    # --- Демо: создание встреч ---
    meeting1 = vault.create_meeting(
        title="Спринт-план", 
        date="2024-05-15", 
        participants=["Анна", "Борис"], 
        topics=["Цели спринта", "Ресурсы"]
    )
    
    meeting2 = vault.create_meeting(
        title="Технический ретроспектив", 
        date="2024-05-16", 
        participants=["Анна", "Борис", "Виктор"], 
        topics=["Качество кода", "Скорость"]
    )
    
    # --- Демо: добавление действий ---
    vault.add_action(meeting1, "До 20 мая", "Подготовить задачи спринта")
    vault.add_action(meeting1, "До 25 мая", "Назначить ресурсы")
    vault.add_action(meeting2, "До 26 мая", "Обновить метрики качества")
    
    # --- Демо: поиск и вывод ---
    print("=" * 40)
    print("📋 Все встречи:")
    for m in vault.list_meetings():
        actions = vault.get_actions(m.title) if vault.has_meeting(m.title) else []
        action_str = f" | Действия: {', '.join(a['description'] for a in actions)}" if actions else ""
        print(f"  • {m['title']} ({m['date']}) — Участники: {', '.join(m['participants'])}{action_str}")
    
    print("\n🔍 Поиск по ключевому слову 'Спринт':")
    for m in vault.search("Спринт"):
        actions = vault.get_actions(m.title) if vault.has_meeting(m.title) else []
        action_str = f" | Действия: {', '.join(a['description'] for a in actions)}" if actions else ""
        print(f"  • {m['title']} ({m['date']}) — Участники: {', '.join(m['participants'])}{action_str}")

if __name__ == "__main__":
    main()
