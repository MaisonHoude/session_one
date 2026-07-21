# === Stage 20: Добавь восстановление записей из архива ===
# Project: MeetingVault
import json, os, sys
from pathlib import Path

ARCHIVE_DIR = Path(__file__).parent / "archive"

def load_archive():
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    files = sorted(ARCHIVE_DIR.glob("*.json")) if ARCHIVE_DIR.exists() else []
    records = {}
    for f in files:
        with open(f) as fh:
            data = json.load(fh)
            mid = data.get("_id") or os.path.splitext(f.name)[0]
            records[mid] = data
    return records

def add_record_from_archive(record):
    """Добавляет запись из архива в активную базу."""
    from database import DB
    db = DB()
    mid = record.get("_id") or os.path.splitext(os.path.basename(record.get("file", "")))[0]
    if not mid:
        raise ValueError("Record must have _id or filename to be restored")
    existing = db.find_one({"_id": mid})
    if existing:
        existing.update(record)
        db.save(existing)
        print(f"  Updated {mid}")
    else:
        db.insert(record)
        print(f"  Added {mid} from archive")

def restore_all():
    """Восстанавливает все записи из архива в основную базу."""
    records = load_archive()
    if not records:
        print("  Archive is empty.")
        return
    for mid, rec in records.items():
        add_record_from_archive(rec)

if __name__ == "__main__":
    restore_all()
