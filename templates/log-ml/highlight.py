def print_alert(msg: str):
    print("\n" + "⚠️" * 10 + " 이상 징후 감지 " + "⚠️" * 10)
    print(f"\033[91m{msg}\033[0m")
    print("⚠️" * 30 + "\n")
