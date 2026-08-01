# === Stage 28: Добавь подсчёт ключевых метрик проекта ===
# Project: MeetingVault
def print_metrics(meetings):
    total = len(meetings)
    if total == 0:
        print("Метрики: нет данных")
        return
    with_actions = sum(1 for m in meetings if hasattr(m, 'actions') and m.actions)
    avg_participants = sum(len(m.get('participants', [])) for m in meetings) / total
    unique_topics = len(set(t.upper() for m in meetings for t in (m.get('agenda', []) or [])))
    print(f"Всего встреч: {total}")
    print(f"С действиями: {with_actions} ({100*with_actions/total:.1f}%)")
    print(f"Сред. участников: {avg_participants:.1f}")
    print(f"Уникальных тем повестки: {unique_topics}")

print_metrics(meetings)
