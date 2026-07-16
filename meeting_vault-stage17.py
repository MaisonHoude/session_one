# === Stage 17: Добавь группировку записей по категориям ===
# Project: MeetingVault
from collections import defaultdict


def group_by_category(records):
    """Группирует записи по категории (тема, статус, приоритет)."""
    grouped = defaultdict(list)
    for r in records:
        key = f"{r.get('category', 'other')}_{r.get('status', 'unknown')}"
        grouped[key].append(r)
    return dict(sorted(grouped.items()))


def categorize_meetings(meetings):
    """Добавляет категории к записям: тема, статус, приоритет."""
    categorized = []
    for m in meetings:
        cat = {
            "topic": m.get("agenda", {}).get("main_topic", "Обсуждение"),
            "status": m.get("resolution_status", "pending"),
            "priority": m.get("action_priority", "normal"),
        }
        categorized.append({**m, **cat})
    return categorized


def filter_by_status_and_category(meetings, status=None, category=None):
    """Фильтрует встречи по статусу и категории."""
    filtered = meetings
    if status:
        filtered = [m for m in filtered if m.get("status") == status]
    if category:
        filtered = [m for m in filtered if m.get("topic", "").startswith(category)]
    return filtered


def get_stats_by_category(meetings):
    """Статистика по категориям."""
    stats = defaultdict(lambda: {"total": 0, "resolved": 0, "pending": 0})
    for m in meetings:
        topic = m.get("topic", "other")
        status = m.get("status", "unknown")
        stats[topic]["total"] += 1
        if status == "resolved":
            stats[topic]["resolved"] += 1
        elif status == "pending":
            stats[topic]["pending"] += 1
    return dict(stats)
