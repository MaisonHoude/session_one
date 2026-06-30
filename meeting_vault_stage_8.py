# === Stage 8: Реализуй текстовый интерфейс команд с меню действий ===
# Project: MeetingVault
import sys, os, json, time
from datetime import datetime

def show_menu():
    print("\n=== MeetingVault CLI ===")
    print("1. Создать новую встречу")
    print("2. Просмотреть список встреч")
    print("3. Редактировать встречу по ID")
    print("4. Удалить встречу по ID")
    print("5. Выход")

def create_meeting(meetings_file):
    if not os.path.exists(meetings_file):
        with open(meetings_file, 'w', encoding='utf-8') as f: json.dump([], f)
    
    title = input("Введите заголовок встречи: ")
    date_str = input("Дата (YYYY-MM-DD HH:MM): ")
    participants = input("Участники (через запятую): ").split(',')
    agenda = input("Повестка дня: ")
    decisions = input("Решения: ")
    
    meeting = {
        "id": len(meetings) + 1,
        "title": title.strip(),
        "date": date_str,
        "participants": [p.strip() for p in participants],
        "agenda": agenda.strip(),
        "decisions": decisions.strip()
    }
    
    with open(meetings_file, 'r', encoding='utf-8') as f: meetings = json.load(f)
    meetings.append(meeting)
    with open(meetings_file, 'w', encoding='utf-8') as f: json.dump(meetings, f, ensure_ascii=False, indent=2)
    print("Встреча создана успешно!")

def list_meetings(meetings_file):
    if not os.path.exists(meetings_file) or not os.path.getsize(meetings_file): return
    
    with open(meetings_file, 'r', encoding='utf-8') as f: meetings = json.load(f)
    
    print("\n=== Список встреч ===")
    for m in meetings:
        print(f"ID: {m['id']} | Дата: {m['date']} | Тема: {m['title']}")

def edit_meeting(meetings_file):
    list_meetings(meetings_file)
    try: meeting_id = int(input("Введите ID встречи для редактирования: "))
    except ValueError: return
    
    with open(meetings_file, 'r', encoding='utf-8') as f: meetings = json.load(f)
    
    for m in meetings:
        if m['id'] == meeting_id:
            print("Что обновить? 1. Заголовок 2. Дата 3. Участники 4. Повестка 5. Решения")
            choice = input()
            
            if choice == '1': new_val = input("Новый заголовок: "); m['title'] = new_val.strip()
            elif choice == '2': new_val = input("Новая дата: "); m['date'] = new_val.strip()
            elif choice == '3': new_val = input("Новые участники (через запятую): "); m['participants'] = [p.strip() for p in new_val.split(',')]
            elif choice == '4': new_val = input("Новая повестка: "); m['agenda'] = new_val.strip()
            elif choice == '5': new_val = input("Новые решения: "); m['decisions'] = new_val.strip()
            
            with open(meetings_file, 'w', encoding='utf-8') as f: json.dump(meetings, f, ensure_ascii=False, indent=2)
            print("Изменения сохранены.")
            return
    
    print("Встреча с таким ID не найдена.")

def delete_meeting(meetings_file):
    list_meetings(meetings_file)
    try: meeting_id = int(input("Введите ID встречи для удаления: "))
    except ValueError: return
    
    with open(meetings_file, 'r', encoding='utf-8') as f: meetings = json.load(f)
    
    for i, m in enumerate(meetings):
        if m['id'] == meeting_id:
            del meetings[i]
            with open(meetings_file, 'w', encoding='utf-8') as f: json.dump(meetings, f, ensure_ascii=False, indent=2)
            print("Встреча удалена.")
            return
    
    print("Встреча с таким ID не найдена.")

def main():
    meetings_file = "meetings.json"
    
    if len(sys.argv) > 1:
        cmd = sys.argv[1].lower()
        
        if cmd == 'create': create_meeting(meetings_file); return
        elif cmd == 'list': list_meetings(meetings_file); return
        elif cmd == 'edit': edit_meeting(meetings_file); return
        elif cmd == 'delete': delete_meeting(meetings_file); return
        else: print(f"Неизвестная команда: {cmd}")
    
    while True:
        show_menu()
        choice = input("Выберите действие (1-5): ")
        
        if choice == '1': create_meeting(meetings_file)
        elif choice == '2': list_meetings(meetings_file)
        elif choice == '3': edit_meeting(meetings_file)
        elif choice == '4': delete_meeting(meetings_file)
        elif choice == '5': print("Выход из программы."); break
        else: print("Некорректный выбор.")
