# === Stage 34: Добавь простую систему шаблонов для быстрого создания записей ===
# Project: MeetingVault
TEMPLATE_REGISTRY = {}

def register_template(name, schema):
    """Register a meeting template with a field schema.
    schema: dict of field_name -> field_type (str, list, datetime, choice)
    """
    TEMPLATE_REGISTRY[name] = schema

def create_from_template(name, **overrides):
    """Create a new meeting record from a registered template.
    Returns a dict representing the meeting with default values filled in.
    """
    if name not in TEMPLATE_REGISTRY:
        raise ValueError(f"Unknown template: {name}")
    schema = TEMPLATE_REGISTRY[name]
    defaults = {}
    for field, ftype in schema.items():
        if ftype == 'choice':
            defaults[field] = list(schema[field])[0] if schema[field] else None
        elif ftype == 'datetime':
            defaults[field] = None
        elif ftype == 'list':
            defaults[field] = []
        else:
            defaults[field] = ""
    defaults.update(overrides)
    return defaults

# Example usage:
register_template("standup", {
    "topic": "str",
    "attendees": "list",
    "decisions": "list",
    "actions": "list",
    "notes": "str"
})

register_template("review", {
    "topic": "str",
    "attendees": "list",
    "decisions": "list",
    "actions": "list",
    "notes": "str"
})
