from script1 import data
from Pin_low import Pin_Low

"""
    Ten skrypt posłuży nam, aby przeiterować przez dane, znaleźć pasuje do wzorca świece 
    
"""


def is_the_formation_successful(nr_candle: list):

    """
    Pokazuje czy formacja zadziałała prawidłowo
    :param nr_candle:
    :param close:
    :return: success_counter
    """
    success_counter = 0
    for nr in nr_candle:
        count = 0
        for num in range(4):
            if nr + num + 1 >= 250:
                break
            candle_close = data.iloc[nr + num + 1].Close["AAPL"]
            if candle_close <= data.iloc[nr].Close["AAPL"]:
                continue
            count += 1
            if count == 4:
                success_counter += 1

    return success_counter


def counter():
    """
    zlicza ilość wystąpień formacji w danych oraz na której pozycji jest formacja i jej cene zamkniecia
    :return: counter, tab- tablica z indeksami formacji
    """
    counter = 0
    length = len(data)
    tab = []
    tab_close = []
    for i in range(length):
        close = data.iloc[i].Close["AAPL"]
        open = data.iloc[i].Open["AAPL"]
        high = data.iloc[i].High["AAPL"]
        low = data.iloc[i].Low["AAPL"]
        candle = Pin_Low(close, open, high, low)
        flag = candle.conditions()
        if flag:
            counter += 1
            tab.append(i)
            tab_close.append(close)
    return counter, tab


results = counter()
print(results)

success_counter = is_the_formation_successful(results[1])
print(success_counter)

probability_of_success = (success_counter / results[0]) * 100
print(probability_of_success, "%")
