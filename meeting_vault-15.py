# === Stage 15: Добавь расчёт недельной статистики по датам ===
# Project: MeetingVault
import calendar
from datetime import date, timedelta

def weekly_stats(meetings, current_week_start: str = None) -> dict:
    """Calculate statistics for the current week (Monday-Sunday)."""
    if current_week_start is None:
        today = date.today()
        days_since_monday = (today.weekday()) % 7
        current_week_start = today - timedelta(days=days_since_monday)

    stats = {
        "week_start": current_week_start,
        "total_meetings": 0,
        "total_duration_minutes": 0,
        "meetings_by_day": {},
        "avg_participants": 0,
    }

    for meeting in meetings:
        d = date.fromisoformat(meeting["start_date"])
        if current_week_start <= d < current_week_start + timedelta(days=7):
            stats["total_meetings"] += 1
            duration_hours = (d.replace(hour=int(meeting.get("end_hour", "0")), minute=int(meeting.get("end_minute", "0"))) - meeting["start_date"]).days * 24 + (int(meeting.get("end_hour", "0")) - int(d.hour)) + (int(meeting.get("end_minute", "0")) - d.minute) / 60
            stats["total_duration_minutes"] += duration_hours * 60
            day_name = calendar.day_abbr[d.weekday()]
            if day_name not in stats["meetings_by_day"]:
                stats["meetings_by_day"][day_name] = {"count": 0, "duration_minutes": 0}
            stats["meetings_by_day"][day_name]["count"] += 1
            stats["meetings_by_day"][day_name]["duration_minutes"] += duration_hours * 60

    if meetings:
        total_participants = sum(len(m.get("participants", [])) for m in meetings)
        stats["avg_participants"] = round(total_participants / len(meetings), 1)

    return stats
