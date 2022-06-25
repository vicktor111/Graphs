def __rgb(number):
    f = 0

    def new_func(number):
        numbers = [10, 11 , 12, 13, 14, 15]
        strings = ['a', 'b', 'c', 'd', 'e', 'f']
        string = number
        for i in range(len(numbers)):
            if number == numbers[i]:
                string = strings[i]
        
        return string

    while True:
        if number > 15:
            number -= 16
            f += 1
        else:
            break
    number = new_func(number)
    f = new_func(f)
    return f"{str(f) + str(number)}"

def hex(r=0, g=0, b=0):
    "Функція яка перетворує rgb в hex."
    if r <= 255 and g <= 255 and b <= 255:
        r = __rgb(r)
        g = __rgb(g)
        b = __rgb(b)
        return f"#{r}{g}{b}"
