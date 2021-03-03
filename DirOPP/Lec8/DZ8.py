class AMD:
    """Базовй класс AMD для дочернего класса CPU """

    def __init__(self):
        #print("""Базовй класс AMD для дочернего класса CPU """)
        super().__init__()


class Intel:
    """Базовй класс Intel для дочернего класса CPU """

    def __init__(self):
        #print("""Базовй класс Intel для дочернего класса CPU """)
        super().__init__()





class CPU(AMD, Intel):
    """Дочерний класс CPU
       Базовй класс CPU для дочернего класса Motherboard
    """

    def __init__(self, amd: str = None, intel: str = None):
        #print("""Дочерний класс CPU """)
        self.amd = amd
        self.intel = intel
        super().__init__()

    @staticmethod
    def test_fabric(cpu=None):

        if cpu == "i3510":
            return "Производитель Intel"
        return "Производитель AMD"

class NVidia:
    """Базовй класс NVidia для дочернего класса GPU """

    def __init__(self):
        #print("""Базовй класс NVidia для дочернего класса GPU """)
        super().__init__()


class GeForce:
    """Базовй класс GeForce для дочернего класса GPU """

    def __init__(self):
        #print("""Базовй класс GeForce для дочернего класса GPU """)
        super().__init__()


class GPU(NVidia, GeForce):
    """Дочерний класс GPU
       Базовй класс GPU для дочернего класса Motherboard
    """

    def __init__(self, nvidea: str = None, geforce: str = None):
        #print("""Дочерний класс GPU """)
        self.nvideo = nvidea
        self.geforce = geforce
        super().__init__()

    @staticmethod
    def test_fabric(gpu=None):

        if gpu == "gtx1050":
            return "Производитель GeForce"
        return "Производитель NVidia"

class Memory:
    """Базовй класс Memory для дочернего класса Motherboard """

    def __init__(self):
        super().__init__()


class Motherboard(CPU, GPU, Memory):
    """Дочерний класс Motherboard """

    def __init__(self, cpu: str = None, gpu: str = None, memory: str = None):
        self.cpu = cpu
        self.gpu = gpu
        self.memory = memory
        super().__init__()

    def show_info(self):
        #print(f' CPU = {self.cpu}\n gpu = {self.gpu}\n Memory = {self.memory}')
        print()
        print(f'{CPU.test_fabric(self.cpu)} = {self.cpu}\n'
              f'{GPU.test_fabric(self.gpu)} = {self.gpu}\n'
              f'Memory = {self.memory}')


# print(Motherboard.__mro__)
# print(CPU.__mro__)
# print(GPU.__mro__)
m1 = Motherboard("i3510", 'gtx1050', 'ddr5')
m1.show_info()
m2 = Motherboard("Ryzen3970", 'ruz1050', 'ddr5')
m2.show_info()
