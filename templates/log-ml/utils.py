from datetime import datetime
import re

# ✅ 로그 파싱 함수
def parse_syslog(message):
    try:
        # <숫자>로 시작하는 syslog PRI 헤더 제거
        clean_msg = re.sub(r"^<\d+>", "", message).strip()

        # timestamp 파싱 (예: Nov 25 22:00:00)
        parts = clean_msg.split(" ", 3)
        timestamp_str = " ".join(parts[0:3])
        timestamp = datetime.strptime(timestamp_str, "%b %d %H:%M:%S")

        return {
            "timestamp": timestamp,
            "message": parts[3] if len(parts) > 3 else ""
        }

    except Exception as e:
        print(f"Syslog 파싱 실패: {e}")
        return None

# ✅ 버퍼에 로그 추가 함수
def add_to_buffer(buffer, item, max_size=100):
    if item is None:
        return
    buffer.append(item)
    if len(buffer) > max_size:
        buffer.pop(0)
