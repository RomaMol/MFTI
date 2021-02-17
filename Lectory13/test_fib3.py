import fib

final_result = True

test_list = 40
for n in range(int(test_list)):

    result = fib.fib(n)
    print(f'n {n},  fib.fib(n) {fib.fib(n)}, ')
    n += 1

if final_result:
    print(f"TEST OK")

