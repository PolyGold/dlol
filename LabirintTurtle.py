from termcolor import colored


class LabirintTurtle:
    def __init__(self):
        self.map = []
        self.turtle = []
        self.znach = None
        self.perem = []
        self.puti = [[-1, -1, -1]]

    def load_map(self, name):
        file = open(name, "r", encoding='utf-8')
        line = file.readline()
        while line.find(" ") != -1 or line.find("*") != -1:
            self.map.append(list(line[:-1]))
            line = file.readline()
        # есть ли в карте координаты черепашки
        try:
            x = int(line)
            line = file.readline()
            y = int(line)
            self.turtle = [x, y]
            if self.check_map() is None:
                print('с картой беды')
                self.load_map(input())

        except ValueError:
            print("А координаты вносить кто будет?????")
            self.load_map(input())

    def show_map(self, turtle=None):
        if turtle is True:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    if self.turtle[0] == i and self.turtle[1] == j:
                        print('🦋', end='\t')
                    else:
                        print(colored(self.map[i][j], 'magenta'), end='\t')
                print()

        else:
            for i in range(len(self.map)):
                for j in range(len(self.map[i])):
                    print(colored(self.map[i][j], 'magenta'), end='\t')
                print()

    def check_map(self):
        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if self.map[i][j] != '*' and self.map[i][j] != ' ' and self.map[i][j] != '🦋':
                    return None

        # в карте обязательно должен быть выход
        """up = self.map[0]
        bottom = self.map[-1]
        left = [i[0] for i in self.map]
        right = [i[-1] for i in self.map]"""

        for i in range(0, len(self.map)):
            for j in range(0, len(self.map[i])):
                if i == 0 or j == 0 or i == self.map or j == self.map[0]:
                    if self.map[i][j] == ' ':
                        self.perem = [i, j]
                        print(self.perem)
                        break
            if self.perem == []:
                print('выхода нет')
                return None

        # нет областей из которых выход черепахи невозможен.

        # черепашка не может находится на стенке

        if self.map[int(self.turtle[0])][int(self.turtle[1])] != "*":
            pass
        else:
            print("Черепаха на месте стены")
            return None

        return 1

    '''def exit_show_step(self):
        while self.turtle[i,j] != self.perem[i,j]:

        break'''


a = LabirintTurtle()
a.load_map('1')
a.show_map(turtle=True)
