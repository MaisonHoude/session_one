# === Stage 41: Добавь режим dry-run для операций изменения данных ===
# Project: MeetingVault
def dry_run_operation(op, payload, *, dry=False):
    if dry:
        return {
            "status": "dry-run",
            "operation": op,
            "payload": payload,
            "message": f"[DRY-RUN] {op} {payload} — изменение не применено.",
        }
    return {"status": "ok", "operation": op, "payload": payload}
