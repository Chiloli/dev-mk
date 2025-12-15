from realtime_detector import start_realtime_detection, stop_realtime_detection

if __name__ == "__main__":
    try:
        print("🚀 실시간 로그 이상 탐지 시스템 시작!")
        start_realtime_detection()
    except KeyboardInterrupt:
        print("🛑 시스템 종료 요청됨. 모델 저장 중...")
        stop_realtime_detection()
        print("✅ 종료 완료")
