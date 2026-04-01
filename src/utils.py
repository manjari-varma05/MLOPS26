import os
import json

def create_dir(path):
    """Create directory if not exists"""
    os.makedirs(path, exist_ok=True)

def save_json(data, filepath):
    """Save dictionary as JSON file"""
    with open(filepath, "w") as f:
        json.dump(data, f, indent=2)

def format_message(msg):
    """Format message for logging"""
    return f"[INFO] {msg}"


if __name__ == "__main__":
    create_dir("demo")
    save_json({"test": 123}, "demo/test.json")
    print(format_message("Utils working"))