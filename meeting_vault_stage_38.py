# === Stage 38: Добавь расширенный набор тестов для ошибок и пограничных случаев ===
# Project: MeetingVault
def test_edge_cases():
    v = MeetingVault()
    # 1. Создание встречи без обязательных полей
    with pytest.raises(ValueError):
        v.create_meeting(title="", attendees=[], agenda=[], decisions=[], actions=[])
    # 2. Создание встречи с невалидным статусом
    with pytest.raises(ValueError):
        v.create_meeting(title="t", attendees=[], agenda=[], decisions=[], actions=[], status="invalid")
    # 3. Создание встречи без id
    with pytest.raises(ValueError):
        v.create_meeting(title="t", attendees=[], agenda=[], decisions=[], actions=[], id="")
    # 4. Добавление участника с пустым именем
    with pytest.raises(ValueError):
        v.add_attendee(meeting_id="m", name="")
    # 5. Добавление повестки с пустой темой
    with pytest.raises(ValueError):
        v.add_agenda_item(meeting_id="m", topic="")
    # 6. Добавление решения с пустым решением
    with pytest.raises(ValueError):
        v.add_decision(meeting_id="m", decision="")
    # 7. Добавление действия с пустым ответственным
    with pytest.raises(ValueError):
        v.add_action(meeting_id="m", assignee="", description="d", due_date="")
    # 8. Получение встречи по несуществующему ID
    assert v.get_meeting("nonexistent") is None
    # 9. Получение участников по несуществующему ID
    assert v.get_attendees("nonexistent") == []
    # 10. Получение повестки по несуществующему ID
    assert v.get_agenda("nonexistent") == []
    # 11. Получение решений по несуществующему ID
    assert v.get_decisions("nonexistent") == []
    # 12. Получение действий по несуществующему ID
    assert v.get_actions("nonexistent") == []
    # 13. Получение всех встреч по несуществующему статусу
    assert v.get_meetings_by_status("nonexistent") == []
    # 14. Получение всех участников по несуществующему статусу
    assert v.get_attendees_by_status("nonexistent") == []
    # 15. Получение всех повесток по несуществующему статусу
    assert v.get_agenda_by_status("nonexistent") == []
    # 16. Получение всех решений по несуществующему статусу
    assert v.get_decisions_by_status("nonexistent") == []
    # 17. Получение всех действий по несуществующему статусу
    assert v.get_actions_by_status("nonexistent") == []
    # 18. Удаление несуществующей встречи
    assert v.delete_meeting("nonexistent") == False
    # 19. Удаление несуществующего участника
    assert v.delete_attendee("nonexistent") == False
    # 20. Удаление несуществующей повестки
    assert v.delete_agenda_item("nonexistent") == False
    # 21. Удаление несуществующего решения
    assert v.delete_decision("nonexistent") == False
    # 22. Удаление несуществующего действия
    assert v.delete_action("nonexistent") == False
