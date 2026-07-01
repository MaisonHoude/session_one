# === Stage 9: Добавь импорт начальных данных из JSON-строки ===
# Project: MeetingVault
import json, sys, os

def load_initial_data(json_string: str) -> dict:
    """Загружает начальные данные из JSON-строки в структуру проекта."""
    try:
        raw = json.loads(json_string)
        if not isinstance(raw, list):
            raise ValueError("JSON должен содержать массив встреч")
        
        meetings = []
        for item in raw:
            meeting_id = item.get('id') or len(meetings) + 1
            
            # Парсинг участников (формат: "Имя <role>")
            participants_raw = item.get('participants', [])
            participants = [
                {
                    'name': p['name'],
                    'role': p.get('role', 'attendee'),
                    'email': p.get('email')
                } for p in participants_raw if isinstance(p, dict)
            ]
            
            # Парсинг повестки (формат: "Тема -> Решение")
            agenda_items = []
            raw_agenda = item.get('agenda', [])
            for entry in raw_agenda:
                if isinstance(entry, str):
                    parts = entry.split('->')
                    if len(parts) == 2:
                        topic, decision = [s.strip() for s in parts]
                        agenda_items.append({'topic': topic, 'decision': decision})
                
            # Парсинг действий (формат: "Действие -> Ответственный -> Дедлайн")
            actions_raw = item.get('actions', [])
            actions = []
            for entry in actions_raw:
                if isinstance(entry, str):
                    parts = [s.strip() for s in entry.split('->')]
                    if len(parts) >= 3:
                        action_desc = ' '.join(parts[:-2])
                        assignee = parts[-2]
                        deadline = parts[-1]
                        actions.append({
                            'description': action_desc,
                            'assignee': assignee,
                            'deadline': deadline
                        })

            meetings.append({
                'id': meeting_id,
                'title': item.get('title', f'Встреча #{meeting_id}'),
                'date': item.get('date'),
                'participants': participants,
                'agenda_items': agenda_items,
                'actions': actions
            })

        return {'meetings': meetings}
    except json.JSONDecodeError as e:
        print(f"Ошибка парсинга JSON: {e}", file=sys.stderr)
        sys.exit(1)
