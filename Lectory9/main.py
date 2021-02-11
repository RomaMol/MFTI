class Base:
    def __init__(self, x):
        self.x = x

    def show(self):
        print(f"BASE {self.x}")


class Derivative(Base):
    def __init__(self, name):
        super().__init__(20)  # явный вызов констркутора
        self.name = name


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
