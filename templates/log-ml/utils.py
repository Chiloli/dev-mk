import re
from datetime import datetime

def parse_syslog(message: str):
    try:
        clean = re.sub(r"^<\d+>", "", message).strip()
        parts = clean.split(" ", 3)
        timestamp = datetime.strptime(" ".join(parts[0:3]), "%b %d %H:%M:%S")
        return {"timestamp": timestamp, "message": parts[3] if len(parts) > 3 else ""}
    except Exception as e:
        print(f"[❌] 파싱 실패: {e}")
        return None

def append_to_buffer(buffer: list, item: dict, max_size=100):
    if item:
        buffer.append(item)
        if len(buffer) > max_size:
            buffer.pop(0)
