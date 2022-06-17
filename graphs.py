import random
import module as mod
from tkinter import Tk, Canvas


WITH_LINES = "with lines"

def create_num_float(num):
    a = 0
    b = 0
    for _ in range(num):
        if b >= 9:
            a += 1
            b = 0
        else:
            b += 1
        yield f" {a}.{b} "

def create_scale(num_scales, numbers, max_1=10):
    # Математечний спосіб запису числа
    def convert_nums(number):
        return 10 ** - (len(str(int(number))) - 1)
    max_num = max(numbers)
    result = 0
    scale = []
    new_numbers = []
    # Коли число більше за максимальне.
    if max_num > max_1:
        science_num = convert_nums(max_num)
        for i in range(len(numbers)):
            result = numbers[i] * science_num
            new_numbers.append(result)
    # Запис в список чисил для шкали.
    for i in range(1, num_scales):
        num = i * (10 ** (len(str(int(max_num))) - 1))
        scale.append(num)
    if len(new_numbers) == 0:
        return [scale, numbers]
    else:
        return [scale, new_numbers]


class Attribute:
    def __init__(self, name, value, color):
        self.name = name
        self.value = value
        self.color = color

    def set_value(self, new_value):
        if type(new_value) == type(int()):
            self.value.append(new_value)
        elif type(new_value) == type(list()) or type(tuple()):
            for i in range(len(new_value)):
                self.value.append(new_value[i])

    def __repr__(self):
        return f'[name: {self.name}.\nvalue: {self.value}.\ncolor: {self.color}.]'


class Graph:

    def __init__(self, master, width, height, num_x, num_y,
                 *attributes: list[Attribute],
                 type_graph="normal",
                 more_nums=False):
        self._x = 10
        self._y = 20
        self.master = master
        self.type_graph = type_graph
        self.more_nums = more_nums
        self._height = height
        self._width = width
        self._attributes = attributes
        self.num_y = num_y
        self.num_x = num_x
        self._canvas = Canvas(master, bg="#ffffff",
                              width=width, height=height + 30)
        self._create_graph()

    def _paint_scale(self, lengths: list[int, int],
                    locations: list[list, list]):
        canvas = self._canvas
        self._range_1 = lengths[1] / self.num_y
        # Накреслення шкали на вісі ординат.
        for i in range(1, self.num_y):
            y = locations[1] - (self._range_1 * i)
            if y > 10:
                canvas.create_line(locations[0], y,
                                   locations[0] - 5, y)
                canvas.create_line(locations[0], y,
                                   locations[0] + 5, y)
                if self.type_graph == "with lines":
                    canvas.create_line(
                        locations[0], y, self._width, y,
                        fill=f"black")
                canvas.create_text(
                    locations[0] - 10, y, text=f"{self.special_list[0][i - 1]}")
            else:
                break
        # Накреслення шкали на вісі абсис.
        special_num = create_num_float(self.num_x)
        for i in range(1, self.num_x):
            if self.more_nums == False:
                x = locations[0] + (self._range_1 * i)
            else:
                range_1 = 13
                x = locations[0] + (range_1 * i)
            # Накреслення самих ліній.
            if x < lengths[0]:
                canvas.create_line(x, locations[1], x,
                                   locations[1] - 5)
                canvas.create_line(x, locations[1], x,
                                   locations[1] + 5)
                if self.more_nums == True:
                    canvas.create_text(x, locations[1] + 10, text=f"{next(special_num)}",
                                       font=('Helvetica 5 bold'))
                else:
                    canvas.create_text(x, locations[1] + 10, text=f"{i}")
            else:
                break

    def _create_rectangle(self):
        y0 = self._height + 10
        x0 = 10
        range_1 = self._width / (len(self._attributes) + 1)
        for i in range(len(self._attributes)):
            x = x0 + (range_1 * i)
            self._canvas.create_rectangle(x, y0, x + 30, y0 + 5,
                                          fill=self._attributes[i].color)
            self._canvas.create_text(
                x + 60, y0, text=self._attributes[i].name)

    def _create_marks(self):
        """Розміщення об'єктів на графіку."""
        # Знаходження значень для побудування шкали.
        x0 = 20
        y0 = self._height - 20
        length_line_y = self._height - 30
        length_line_x = self._width - 30
        self._paint_scale(
            [length_line_x, length_line_y],
            [x0, y0])
        self._create_rectangle()
        # Візуалізація даних.
        for attribute in self._attributes:
            y_coordinate = self.special_list[1]
            if self.more_nums == False:
                for i in range(len(y_coordinate) - 1):
                    if x0 + (self._range_1 * i) < length_line_x:
                        # Накреслення ліній.
                        self._canvas.create_line(
                            x0 + (self._range_1 * i),
                            y0 - (self._range_1 * y_coordinate[i]),
                            x0 + (self._range_1 * (i + 1)),
                            y0 - (self._range_1 * y_coordinate[i + 1]),
                            fill=attribute.color)
                    else:
                        break
            else:
                # Початкові кординати точок.
                range_2 = 13
                x = x0
                # Розміщення точок на кординатній площині.
                for i in range(len(y_coordinate)):
                    x += 1 * range_2
                    y = y0 - (self._range_1 * y_coordinate[i])
                    if x < length_line_x:
                        self._canvas.create_oval(
                            x - 2,
                            y - 2,
                            x + 2,
                            y + 2,
                            fill=attribute.color)
                    else:
                        break

    def _create_graph(self):
        self.special_list = create_scale(self.num_y, self._attributes[0].value)
        # Довжини кордиатних прямих.
        height = self._height - 20
        width = self._width - 10
        canvas = self._canvas
        # Накреслення кордиатної прямої y.
        canvas.create_line(20, 10, 20, height, fill="black")
        canvas.create_line(20, 10, 25, 15)
        canvas.create_line(20, 10, 15, 15)
        # Накреслення кордиатної прямої x.
        canvas.create_line(20, height, width, height, fill="black")
        canvas.create_line(width, height, width - 6, height - 6)
        canvas.create_line(width, height, width - 6, height + 6)
        # Початок кординат.
        canvas.create_oval(19, height + 1, 22, height - 2,
                           fill="black")
        self._create_marks()

    def place(self, x, y):
        self._canvas.place(x=x, y=y)

    def pack(self):
        self._canvas.place(x=10, y=20)

    def update(self, *new_attribute, x=10, y=20):
        self._canvas.destroy()
        self._canvas = Canvas(self.master, bg="#ffffff",
                              width=self._width, height=self._height + 30)
        self._attributes = new_attribute
        self._create_graph()
        self.place(x, y)

    def __repr__(self):
        text = ''
        for attribute in self._attributes:
            title = attribute.name
            text += f"{title}, "
        return f"""    atributes: {text[0:len(text) - 2]}.
    height: {self._height}.
    width: {self._width}.
    num_x: {self.num_y}.
    num_y: {self.num_x}."""


class Graph_Сomparable(Graph):

    def __init__(self, master, width, height, num_y,
                 attribute: Attribute):
        super().__init__(master, width, height, 0, num_y, attribute)

    def _create_marks(self):
        # Початкові кординати точок.
        attribute = self._attributes[0]
        x0 = 20
        y0 = self._height - 20
        length_line_x = self._width - 30
        self._paint_scale_y([x0, y0])
        # Накреслення поріваняльних прямокутників.
        y_coordinate = self.special_list[1]
        x0 = 40
        for i in range(len(y_coordinate)):
            if x0 + (self._range_1 * i) < length_line_x:
                # Накреслиння квадратів.
                x = x0 + (80 * i)
                self._canvas.create_rectangle(
                    x,
                    y0,
                    x + 40,
                    y0 - (self._range_1 * y_coordinate[i]),
                    fill=attribute.color[i])
                self._canvas.create_text(x + 20, y0 + 10,
                                         text=attribute.name[i])
            else:
                break

    def update(self, new_attribute, x=10, y=20):

        self._canvas.destroy()
        self._attributes = new_attribute
        self._create_graph()
        self.place(x, y)

    def _paint_scale_y(self, locations):
        # Значення для накреслення шкали.
        canvas = self._canvas
        length_line_y = self._height - 30
        self._range_1 = length_line_y / self.num_y
        # Накреслення шкали на вісі ординат.
        for i in range(1, self.num_y):
            y = locations[1] - (self._range_1 * i)
            if y > 10:
                canvas.create_line(locations[0], y,
                                   locations[0] - 5, y)
                canvas.create_line(locations[0], y,
                                   locations[0] + 5, y)
                canvas.create_text(
                    locations[0] - 10, y, text=f"{self.special_list[0][i - 1]}")
            else:
                break


class Graph_Oval:

    def __init__(self, window, width, height, x=10, y=40, color="#ffffff"):
        self.window = window
        self.width = width
        self.height = height
        self.color = color
        self.canvas = Canvas(window, width=width, height=height + 30, bg=color)
        self.canvas.place(x=x, y=y)

    def create_part_ovals(self, scale=40, extents=[25, 25, 25, 25]):
        # Основні зміні для строрення круга.
        CONST = 129600
        start = 0
        x0 = self.width / 2
        y0 = self.height / 2
        self.__attributes = []
        scale *= 2
        # Створення і оформлення секторів (частин круга).
        for i in range(len(extents)):
            color = mod.hex(random.randint(0, 255),
                            random.randint(0, 255),
                            random.randint(0, 255))
            # Конвертація відцотка в градуси.
            deg = (CONST * extents[i]) / 36000
            self.canvas.create_arc(x0 - scale, y0 - scale, x0 + scale, y0 + scale, start=start,
                                   extent=deg, fill=color)
            self.__attributes.append(Attribute(i + 1, extents[i], color))
            start += deg
            if len(extents) - 1 == i and sum(extents) != 100:
                deg = (CONST * (100 - sum(extents))) / 36000
                self.canvas.create_arc(x0 - scale, y0 - scale, x0 + scale, y0 + scale, start=start,
                                       extent=deg, fill="gray")
        self.__create_rectangle()

    def get_info(self):
        return self.__attributes

    def __create_rectangle(self):
        y0 = self.height + 10
        x0 = 10
        range_1 = self.width / (len(self.__attributes) + 1)
        # Розміщення і креслення прямокутників.
        for i in range(len(self.__attributes)):
            x = x0 + (range_1 * i)
            self.canvas.create_rectangle(x, y0 + 3, x + 20, y0 - 3,
                                         fill=self.__attributes[i].color)
            self.canvas.create_text(
                x + 30, y0, text=self.__attributes[i].name)
