import math
import pyinputplus as pyip

#會值出值的function
def circle_area(radius:int | float)->float:
    area = math.pi * radius ** 2
    return area

radius = pyip.inputFloat("請輸入半徑:")
print(radius)
area = circle_area(10)
print(f"半徑:{radius:.2f},面積為:{area:.2f}")