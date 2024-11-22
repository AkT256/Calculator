def splitting(comb):
    #разбивает строки на элементы списка в которых числа и операции
    elems = []
    ind0 = 0
    for index in range(len(comb)): #этот цикл проходится по строке и выделяет из неё числа и знаки
        if comb[index] in "+-*/%":
            if comb[index] == '-':
                if index == 0 or (index > 0 and comb[index-1] not in "0123456789."):
                    j = index + 1
                    while j < len(comb) and comb[j] in "0123456789.-": #этот цикл используется если у нас отрицательное число и нужно его полностью добавить в список
                        j += 1
                    elems.append(comb[index:j])
                    ind0 = j
                    continue #пропускаем итерацию
            elems.append(comb[ind0:index])
            elems.append(comb[index])
            ind0 = index + 1
    elems.append(comb[ind0:]) #добавляем последний элемент
    elems = [x for x in elems if x] #убирает пустые элементы списка
    return elems

def calculate_expression(elements):
    #инициализирует значения и операнды
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2} #приоритет операторов
    operators = [] #операторы
    values = [] #значения
    def apply_operator(operators, values):
        #Это вспомогательная функция, которая выполняет арифметическую операцию. Она извлекает из стека операторов operators последний оператор и извлекает два последних значения из стека значений values. 
        operator = operators.pop()
        right = values.pop()
        left = values.pop()
        if operator == '+':
            values.append(left + right)
        elif operator == '-':
            values.append(left - right)
        elif operator == '*':
            values.append(left * right)
        elif operator == '/':
            if right == 0:
                raise ValueError("Ошибка: Деление на ноль.")
            values.append(left / right)
        elif operator == '%':
            if right == 0:
                raise ValueError("Ошибка: Деление на ноль.")
            values.append(left % right)

    
    i = 0
    while i < len(elements): #Цикл последовательно добавляет значения и операторы в стеки values и operators.
        token = elements[i]
        if token in precedence:
            while (operators and precedence[operators[-1]] >= precedence[token]): #Если token — оператор, этот вложенный цикл обрабатывает операторы в стеке operators, которые имеют больший или равный приоритет.
                apply_operator(operators, values)
            operators.append(token)
        else:
            values.append(float(token))
        i += 1
#В общем оно проходится по операторам и в порядке у кого больший приоритет и последовательно с помощью 2 функции их считает

    while operators:
        apply_operator(operators, values)

    return values[0] #После выполнения всех операций, в стеке values останется только один элемент — результат вычисления выражения.

def calculator(expression):
    elements = splitting(expression)
    try:
        result = calculate_expression(elements)
    except ValueError as e:
        return str(e)
    return round(result, 3)


print(calculator("-5.576766+-7.3/-5*66679"))
