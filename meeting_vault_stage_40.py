# === Stage 40: Добавь CLI-параметры через argparse для основных операций ===
# Project: MeetingVault
import argparse

def parse_args():
    parser = argparse.ArgumentParser(description="MeetingVault CLI")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("list", help="List all meetings")
    sub.add_parser("add", help="Add a new meeting")
    sub.add_parser("show", help="Show meeting details")
    sub.add_parser("remove", help="Remove a meeting")

    return parser.parse_args()
