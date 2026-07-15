# === Stage 16: Добавь расчёт месячной статистики по датам ===
# Project: MeetingVault
def monthly_stats(meetings):
    stats = {}
    for m in meetings:
        if not hasattr(m, 'date') or not isinstance(m.date, datetime.date): continue
        key = f"{m.date.year}-{m.date.month:02d}"
        if key not in stats:
            stats[key] = {'count': 0, 'duration_total': timedelta(0), 'attendees_set': set()}
        stats[key]['count'] += 1
        if hasattr(m, 'duration') and m.duration is not None:
            stats[key]['duration_total'] += m.duration
        for a in (m.attendees or []):
            stats[key]['attendees_set'].add(a)
    return dict(sorted(stats.items()))
