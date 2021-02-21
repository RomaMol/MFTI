import fib
final_result = True

result = fib.fib(0) == 0
final_result &= result

result = fib.fib(1) == 1
final_result &= result

result = fib.fib(2) == 2
final_result &= result

result = fib.fib(5) == 10
final_result &= result

if final_result:
    print(f"TEST OK")
else:
    print(f"TEST FALSE")