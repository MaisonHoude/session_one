# === Stage 25: Добавь обработку некорректных дат и понятные сообщения об ошибках ===
# Project: MeetingVault
def validate_date(date_str):
    if not date_str or not isinstance(date_str, str):
        return False
    try:
        day, month, year = map(int, date_str.split('-'))
        if year < 1000 or year > 9999 or month < 1 or month > 12 or day < 1 or day > 31:
            return False
        days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        if year % 4 == 0 and not (year % 100 == 0 and year % 400 != 0):
            days_in_month[2] = 29
        if day > days_in_month[month]:
            return False
        return True
    except ValueError:
        return False

def parse_date(date_str):
    try:
        day, month, year = map(int, date_str.split('-'))
        import datetime
        return datetime.date(year, month, day)
    except (ValueError, AttributeError):
        return None
