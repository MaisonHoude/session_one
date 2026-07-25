# === Stage 23: Добавь форматированный вывод таблицей в консоль ===
# Project: MeetingVault
def print_meeting_table(meetings):
    """Compact console-table printer for MeetingVault."""
    if not meetings:
        print("  Нет записей в архиве.\n")
        return
    headers = ("ID", "Дата", "Тема", "Участники", "Статус", "Действия")
    widths = [len(h) for h in headers]
    rows = list(zip(headers, *zip(*meetings)))
    fmt = "  {:<" + str(widths[0]) + "} | {:<" + str(widths[1]) + "} | {:<" + str(widths[2]) + "} | {:<" + str(widths[3]) + "} | {:<" + str(widths[4]) + "} | {:<}" + str(widths[5]) + "}"
    print(fmt.format(*rows[0]))
    print("  -" * (sum(widths) + 11))
    for r in rows[1:]:
        print(fmt.format(*r))

if __name__ == "__main__":
    meetings = [
        {"id": "M-001", "date": "2024-03-05", "topic": "Запуск проекта", "members": ["Анна", "Борис"], "status": "Закончена", "actions": "Договорились о дедлайне"},
        {"id": "M-002", "date": "2024-03-12", "topic": "Финансы Q1", "members": ["Виктор"], "status": "Продолжается", "actions": "Отправить отчёт до 25 марта"},
    ]
    print_meeting_table(meetings)
