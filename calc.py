def splitting(comb):
    elems = []
    ind0 = 0
    for index in range(len(comb)):
        if comb[index] in "+-*/%":
            if comb[index] == '-':
                if index == 0 or (index > 0 and comb[index-1] not in "0123456789."):
                    j = index + 1
                    while j < len(comb) and comb[j] in "0123456789.-":
                        j += 1
                    elems.append(comb[index:j])
                    ind0 = j
                    continue #пропускаем итерацию
            elems.append(comb[ind0:index])
            elems.append(comb[index])
            ind0 = index + 1
    elems.append(comb[ind0:]) #добавляем последний элемент
    elems = [x for x in elems if x]
    return elems

def calculate_expression(elements):
    def apply_operator(operators, values):
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

    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '%': 2}
    operators = []
    values = []
    i = 0

    while i < len(elements):
        token = elements[i]
        if token in precedence:
            while (operators and precedence[operators[-1]] >= precedence[token]):
                apply_operator(operators, values)
            operators.append(token)
        else:
            values.append(float(token))
        i += 1

    while operators:
        apply_operator(operators, values)

    return values[0]

def calculator(expression):
    elements = splitting(expression)
    try:
        result = calculate_expression(elements)
    except ValueError as e:
        return str(e)
    return round(result, 3)

# Пример использования
expression = "-5.5+-7.3/-5*66666"
result = calculator(expression)
print(f"Результат: {result}")
