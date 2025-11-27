import socketserver

from utils import parse_syslog, add_to_buffer
from model import detect_anomaly

log_buffer = []

RED = "\033[91m"
RESET = "\033[0m"
ALERT = "이상 징후 감지!"


class SyslogUDPHandler(socketserver.BaseRequestHandler):
    def handle(self):
        data = self.request[0].strip()
        socket = self.request[1]
        try:
            message = data.decode("utf-8", errors="replace")  # ★ 오류 방지용
            print(f"받은 로그: {message}")

            parsed = parse_syslog(message)
            add_to_buffer(log_buffer, parsed, max_size=100)

            if detect_anomaly(log_buffer):
                print(f"{RED}{ALERT} 로그 내용: {message}{RESET}")


        except Exception as e:
            print(f"로그 처리 중 오류: {e}")

if __name__ == "__main__":
    HOST, PORT = "0.0.0.0", 1514
    server = socketserver.UDPServer((HOST, PORT), SyslogUDPHandler)
    print(f"Syslog 수신 서버 시작 (포트 {PORT})")
    server.serve_forever()
