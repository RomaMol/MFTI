import fib

final_result = True
test_list = [(0, 0), (1, 1), (2, 1), (5, 5), ]

for n, answer in test_list:
    result = fib.fib(n)
    correct = (result == answer)

    if not correct:
        print(f'fib.fib(n) {fib.fib(n)}, answer {answer}')
        print(f"TEST FALSE")
    final_result &= correct

if final_result:
    print(f"TEST OK")
else:
    print(f"final_result &= correct TEST FALSE")
