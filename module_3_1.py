calls = 0


def count_calls():
    global calls
    calls += 1
    return calls


def string_info(string):
    a = []
    up = string.upper()
    a.append(up)
    lo = string.lower()
    a.append(lo)
    count_calls()
    return len(string), *a


def is_contains(string, list_to_search):
    count_calls()
    _string_ = string.upper()
    _list_to_search_ = []
    for i in list_to_search:
        _list_to_search_.append(i.upper())
    return _string_ in _list_to_search_


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN']))  # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic']))  # No matches
print(calls)
