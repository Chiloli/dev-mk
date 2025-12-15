import socketserver
import threading
from queue import Queue
from model import detect_anomaly, update_model, save_model
from utils import parse_syslog, append_to_buffer
from highlight import print_alert

log_queue = Queue()
log_buffer = []
_server = None
_analyzer_thread = None

# ✅ 로그 수신 핸들러
class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        try:
            msg = data.decode("utf-8")
            log_queue.put(msg)
        except UnicodeDecodeError:
            print("❌ 디코딩 실패")

# ✅ 분석기 쓰레드
def analyzer():
    while True:
        raw = log_queue.get()
        parsed = parse_syslog(raw)
        if not parsed:
            continue

        append_to_buffer(log_buffer, parsed)
        msg = parsed["message"]

        is_anomaly = detect_anomaly(msg)
        label = 0 if is_anomaly else 1
        update_model(msg, label)

        if is_anomaly:
            print_alert(msg)
        else:
            print(f"✅ 정상 로그: {msg}")

# ✅ 외부에서 호출되는 함수
def start_realtime_detection(host="0.0.0.0", port=1514):
    global _server, _analyzer_thread

    print(f"📡 UDP 서버 시작: {host}:{port}")
    _server = socketserver.UDPServer((host, port), SyslogUDPHandler)
    _analyzer_thread = threading.Thread(target=analyzer, daemon=True)
    _analyzer_thread.start()

    threading.Thread(target=_server.serve_forever, daemon=True).start()

def stop_realtime_detection():
    global _server
    if _server:
        _server.shutdown()
        _server.server_close()
    save_model()
