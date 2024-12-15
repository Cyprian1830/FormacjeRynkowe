
"""
    Tutaj będziemy analizować, czy  formacja Młotek zachodzi
"""


class Pin_Low:
    def __init__(self, close, open, high, low):
        self.close = close
        self.open = open
        self.high = high
        self.low = low

    def conditions(self):
        try:
            if not all(isinstance(value, (int, float)) for value in [self.open, self.low, self.high, self.close]):
                raise ValueError("Wszystkie wartości (open, low, high, close) muszą być liczbami.")
        except(ValueError):
            print("Wszystkie wartości (open, low, high, close) muszą być liczbami.")
        condiction_1_1 = self.open - self.low
        condiction_1_2 = 0.6*(self.high - self.low)

        condiction_2 = self.close - self.open

        condiction_3_1 = self.high - self.close
        condiction_3_2 = 0.2*(self.high - self.low)

        return ((condiction_1_1 >= condiction_1_2) and
                (condiction_2 > 0) and
                (condiction_3_1 <= condiction_3_2))
