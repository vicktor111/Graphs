from tkinter import Tk, Canvas


WITH_LINES = "with lines"


class Graph:

    def __init__(self, master, width, height, num_x, num_y,
                 *atributes: list[dict[str, list[int]]],
                 type_graph="normal",
                 more_nums=False):
        self._x = 10
        self._y = 20
        self.master = master
        self.type_graph = type_graph
        self.more_nums = more_nums
        self._height = height
        self._width = width
        self._atributes = atributes
        self.num_y = num_y
        self.num_x = num_x
        self._canvas = Canvas(master, bg="#ffffff",
                              width=width, height=height + 30)
        self.create_graph()

    def write_lines(self, lengths: list[int, int],
                    locations: list[list, list]):
        canvas = self._canvas
        self._range_1 = lengths[1] / self.num_y
        # Накреслення шкали на вісі абсис.
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
                canvas.create_text(locations[0] - 10, y, text=f"{i}")
            else:
                break
        # Накреслення шкали на вісі ординат.
        for i in range(1, self.num_x):
            if self.more_nums == False:
                x = locations[0] + (self._range_1 * i)
            else:
                range_1 = 10
                x = locations[0] + (range_1 * i)
            # Накреслення самих ліній.
            if x < lengths[0]:
                canvas.create_line(x, locations[1], x,
                                   locations[1] - 5)
                canvas.create_line(x, locations[1], x,
                                   locations[1] + 5)
                if self.more_nums == True:
                    canvas.create_text(x, locations[1] + 10, text=f"{i}",
                                       font=('Helvetica 5 bold'))
                else:
                    canvas.create_text(x, locations[1] + 10, text=f"{i}")
            else:
                break

    def create_rectangle(self):
        y0 = self._height + 10
        x0 = 10
        range_1 = self._width / (len(self._atributes) + 1)
        for i in range(len(self._atributes)):
            x = x0 + (range_1 * i)
            self._canvas.create_rectangle(x, y0, x + 30, y0 + 5,
                                          fill=self._atributes[i]["color"])
            self._canvas.create_text(
                x + 60, y0, text=self._atributes[i]["name"])

    def create_marks(self):
        """Розміщення об'єктів на графіку."""
        # Знаходження значень для побудування шкали.
        x0 = 20
        y0 = self._height - 20
        length_line_y = self._height - 30
        length_line_x = self._width - 30

        self.write_lines(
            [length_line_x, length_line_y],
            [x0, y0])
        self.create_rectangle()
        # Візуалізація даних.
        for atribute in self._atributes:
            y_coordinate = atribute["value"]
            if self.more_nums == False:
                for i in range(len(y_coordinate) - 1):
                    if x0 + (self._range_1 * i) < length_line_x:
                        # Накреслиння ліній.
                        self._canvas.create_line(
                            x0 + (self._range_1 * i),
                            y0 - (self._range_1 * y_coordinate[i]),
                            x0 + (self._range_1 * (i + 1)),
                            y0 - (self._range_1 * y_coordinate[i + 1]),
                            fill=atribute["color"])
                    else:
                        break
            else:
                # Початкові кординати точок.
                range_2 = 10
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
                            fill=atribute["color"])
                    else:
                        break

    def create_graph(self):
        # Довжини кордиатних прямих.
        height = self._height - 20
        width = self._width - 10
        canvas = self._canvas
        # Накреслиння кордиатної прямої y.
        canvas.create_line(20, 10, 20, height, fill="black")
        canvas.create_line(20, 10, 25, 15)
        canvas.create_line(20, 10, 15, 15)
        # Накреслиння кордиатної прямої x.
        canvas.create_line(20, height, width, height, fill="black")
        canvas.create_line(width, height, width - 6, height - 6)
        canvas.create_line(width, height, width - 6, height + 6)
        # Початок кординат.
        canvas.create_oval(19, height + 1, 22, height - 2,
                           fill="black")
        self.create_marks()

    def place(self, x, y):
        self._canvas.place(x=x, y=y)

    def pack(self):
        self._canvas.place(x=10, y=20)

    def __repr__(self):
        text = ''
        for atribute in self._atributes:
            title = atribute["name"]
            text += f"{title}, "
        return f"""    atributes: {text[0:len(text) - 2]}.
    height: {self._height}.
    width: {self._width}.
    num_x: {self.num_y}.
    num_y: {self.num_x}."""


if __name__ == '__main__':
    import math
    window = Tk()
    window.geometry("900x900")
    atribute_1 = {"name": "numbers",
                  "value": [(math.sqrt(i)) for i in range(1, 90)],
                  "color": "#3aaa34"}
    window.geometry("200x200")
    graph = Graph(window, 1000, 500, 100, 30,
                  atribute_1, more_nums=True)
    graph.pack()
    window.mainloop()
