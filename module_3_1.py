# Функция count_calls подсчитывающая вызовы остальных функций
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string):
    count_calls()  # Увеличиваем счетчик вызовов
    return (len(string), string.upper(), string.lower())

def is_contains(string, list_to_search):
    count_calls()  # Увеличиваем счетчик вызовов
    string_lower = string.lower()
    return any(string_lower in item.lower() for item in list_to_search)

# Данные на вход
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))    # No matches

# Проверяем количество вызовов, вызвав функцию
print(calls)
