#   https://www.youtube.com/watch?v=-ZY0KHGOQoY
#   ООП Python 3 #11: функторы и менеджеры контекста

# ------менеджер контекста ----------------

try:
    with open("myfile.txt")as fp:
        for t in fp:
            print(t)
except Exception as e:
    print(e)


# with <менеджер контекста> as <переменная>:
#  список конструкции(переменные, функции) питона


class DefVect:
    def __init__(self, v):
        print(f'DefVect v = {v}')
        self.__v = v

    def __enter__(self):
        self.__temp = self.__v[:]  # создаем копию вектора v
        print(f'DefVect self.__temp = {self.__temp}')
        return self.__temp

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Проверка на исключения"""
        if exc_type is None:  # если  None то  return False = передаем исключение
            self.__v[:] = self.__temp
        return False  # если  True  то исключение не передается


v1 = [1, 2, 3]
v2 = [1, 2, ]
print(f' v1 = {v1}\n v2 = {v2}\n v1+v2')
try:
    with DefVect(v1) as dv:
        for i in range(len(dv)):
            if v2[i] is None:
                dv[i] += v2[i]
            dv[i] += 0
            print(f"dv[i]  = {dv[i]}")
except Exception as e:
    print(e)

print(f'v1  = {v1}')
