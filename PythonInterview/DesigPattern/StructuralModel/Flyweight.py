"""
享元模式
"""
import json
from typing import Dict


class Flyweight():
    def __init__(self, shared_start: str) -> None:
        self.shared_start = shared_start

    def operation(self, unique_start: str) -> None:
        s = json.dumps(self.shared_start)
        u = json.dumps(unique_start)
        print(f"Flyweight: Displaying shared ({s}) and unique ({u}) state.", end="")


class FlyweightFactory():
    _flyweights: Dict[str, Flyweight] = {}

    def __init__(self, initial_flyweights: Dict) -> None:
        for start in initial_flyweights:
            self._flyweights[self.get_key(start)] = Flyweight(start)

    def get_key(self, start: Dict) -> str:
        return '_'.join(sorted(start))

    def get_flyweight(self, shared_start: Dict) -> Flyweight:
        key = self.get_key(shared_start)
        if not self._flyweights.get(key):
            print('元组不存在，创建')
            self._flyweights[key] = Flyweight(shared_start)
        else:
            print("元组存在.")
        return self._flyweights[key]

    def list_flyweithts(self) -> None:
        count = len(self._flyweights)
        print(f'享元数量为{count}')
        print(f'key值列表：' + '\n'.join(map(str, self._flyweights.keys())), end='')


def add_car_to_polic_database(
        factory: FlyweightFactory, plates: str, owner: str,
        brand: str, model: str, color: str) -> None:
    print('客户端：增加基础数据')
    fly=factory.get_flyweight([brand,model,color])
    fly.operation([plates,owner])

if __name__ == "__main__":
    """
    The client code usually creates a bunch of pre-populated flyweights in the
    initialization stage of the application.
    """

    factory = FlyweightFactory([
        ["Chevrolet", "Camaro2018", "pink"],
        ["Mercedes Benz", "C300", "black"],
        ["Mercedes Benz", "C500", "red"],
        ["BMW", "M5", "red"],
        ["BMW", "X6", "white"],
    ])

    factory.list_flyweithts()

    add_car_to_polic_database(
        factory, "CL234IR", "James Doe", "BMW", "M5", "red")

    add_car_to_polic_database(
        factory, "CL234IR", "James Doe", "BMW", "X1", "red")

    print("\n")

    factory.list_flyweithts()