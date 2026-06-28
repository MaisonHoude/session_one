# === Stage 7: Добавь сортировку записей по дате, приоритету и названию ===
# Project: MeetingVault
def sort_meetings(meeting_list, key='date', reverse=False):
    date_key = lambda m: m.get('created_at') or m.get('updated_at') or 0
    priority_map = {'high': -1, 'medium': 0, 'low': 1}
    name_key = lambda m: m.get('title', '').lower()
    
    if key == 'date':
        return sorted(meeting_list, key=lambda x: (not reverse and date_key(x) or float('-inf'), -priority_map.get(priority_map.get(x.get('priority','medium'),0), 0)), reverse=reverse)
    elif key == 'priority':
        def priority_sort(m):
            p = m.get('priority', 'medium')
            return (not reverse and priority_map.get(p, 0) or float('-inf')) if not reverse else (-1 * priority_map.get(p, 0))
        return sorted(meeting_list, key=priority_sort, reverse=reverse)
    elif key == 'name':
        return sorted(meeting_list, key=name_key, reverse=reverse)
    return meeting_list
