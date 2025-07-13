import time

def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

print("⏱ Đang đo hiệu năng đơn luồng bằng tính fibonacci(35)...")
start = time.time()
fibonacci(35)  # Số càng lớn thì càng nặng CPU
end = time.time()

print(f"Thời gian chạy: {round(end - start, 3)} giây")
