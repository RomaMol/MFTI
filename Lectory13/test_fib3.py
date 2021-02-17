import fib

final_result = True

test_list = 30
for n in range(20, int(test_list) + 1, 2):  # началоб конец шаг
    result = fib.fib(n)
    print(f'n {n},  fib.fib(n) {fib.fib(n)}, ')
    n += 1

if final_result:
    print(f"TEST OK")
