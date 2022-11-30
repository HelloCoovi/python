# 제한없이 인수를 받고
# 받은 인수를 모두 더해서 출력해라

def add(*args):
    print(sum(args))

add(1, 2, 3, 4)


# 이중 아스테리스트는 딕셔너리를 의미한다.
def calculate(num, **kwargs):
    print(kwargs)
    num += kwargs["add"]
    num *= kwargs["multiply"]
    print(num)

calculate(5, add = 3, multiply= 2)


class Car:
    def __init__(self, **kw):
        self.make = kw["make"]
        self.model = kw["model"]
        # get함수를 이용하면 인수를 넣지 않아도 오류가 뜨지않는다
        self.color = kw.get("color")


my_car = Car(make="Nissan", model="GT-R")
print(my_car.make)
print(my_car.color)