import time

def check_time(func):
    def wrap_func(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"함수 {func.__name__}가 {(end - start) * 1000}ms 걸렸습니다.")
        return result
    return wrap_func