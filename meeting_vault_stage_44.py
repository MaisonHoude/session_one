# === Stage 44: Добавь функцию резервного копирования файла данных ===
# Project: MeetingVault
import shutil
from datetime import datetime

def backup_data_file(filename):
    """Создает резервную копию файла данных с меткой даты."""
    if not filename:
        return
    backup_dir = "backups"
    os.makedirs(backup_dir, exist_ok=True)
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_path = os.path.join(backup_dir, f"backup_{filename}_{timestamp}.dat")
    shutil.copy2(filename, backup_path)
    print(f"Backup created: {backup_path}")
