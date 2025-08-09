from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    def __init__(self, total: float, discount: DiscountStrategy):
        self.__total = total
        self.__discount = discount

    @property
    def total(self):
        return self.__total

    @property
    def total_with_discount(self):
        return self.__discount.calculate(self.total)


class DiscountStrategy(ABC):
    @abstractmethod
    def calculate(self, value: float) -> float: ...


class TwentyPercent(DiscountStrategy):
    def calculate(self, value: float):
        return value - (value * 0.2)


class FiftyPercent(DiscountStrategy):
    def calculate(self, value: float):
        return value - (value * 0.3)


class NoDiscount(DiscountStrategy):
    def calculate(self, value: float):
        return value


class CustomDiscount(DiscountStrategy):
    def __init__(self, discount):
        self.discount = discount / 100

    def calculate(self, value: float):
        return value - (value * self.discount)


if __name__ == "__main__":
    twent_porcent = TwentyPercent()
    fifty_porcent = FiftyPercent()
    no_discount = NoDiscount()
    five_discount = CustomDiscount(5)

    order = Order(1000, discount=twent_porcent)
    print(order.total, order.total_with_discount)

    print()
    order = Order(1000, discount=fifty_porcent)
    print(order.total, order.total_with_discount)

    print()
    order = Order(1000, no_discount)
    print(order.total, order.total_with_discount)

    print()
    order = Order(1000, five_discount)
    print(order.total, order.total_with_discount)
