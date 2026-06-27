# === Stage 6: Добавь фильтрацию записей по статусу, категории или тегам ===
# Project: MeetingVault
def filter_meetings(meetings, status=None, category=None, tags=None):
    if not meetings: return []
    filtered = [m for m in meetings]
    if status is not None and m.get('status') != status: filtered.remove(m)
    if category is not None and m.get('category') != category: filtered.remove(m)
    if tags is not None:
        meeting_tags = set(t.lower() for t in m.get('tags', []))
        search_tags = [t.lower() for t in tags]
        if not any(tag in meeting_tags for tag in search_tags): filtered.remove(m)
    return filtered

def get_meeting_statuses(meetings):
    statuses = set()
    for m in meetings: statuses.add(m.get('status', 'unknown'))
    return sorted(statuses, key=lambda s: {'planned': 0, 'in_progress': 1, 'completed': 2, 'cancelled': 3}.get(s.lower(), 99))

def get_meeting_categories(meetings):
    categories = set()
    for m in meetings: categories.add(m.get('category', 'general'))
    return sorted(categories)
