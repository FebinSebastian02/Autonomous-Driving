from dataclasses import dataclass
from abc import ABC, abstractmethod
import time


# Todo: Define a basic class
class Vehicle:  # class Vehicle inherits Abstract class
    wheels = 4  # class attribute, eg: used for constants

    def __init__(self, speed, steer=0):  # self: reference to the current object, non-default arguments come before
        # default arguments. steer=10 overrides default argument.
        self._speed = speed  # without self, speed exists only within this __init__ function as it is not attributed
        # to the object
        self.__steer = steer  # instance attributes, private variable

    # Todo: Instance methods(functions inside a class)
    def accelerate(self, delta):
        self._speed += delta  # protected variable

    # Todo: Pythonic way
    @property  # creates the property, speed function can be accessed like attribute.
    def speed(self):  # getter
        return self._speed

    @speed.setter  # modifies the same property
    def speed(self, value):  # setter
        if value >= 0:
            self._speed = value

    """    # Todo: Getters and setters
        def set_speed(self, speed):
            if speed >= 0:
                self._speed = speed

        def get_speed(self):
            return self._speed"""

    # Todo: __str__: Converts object to a string while printing instead of giving unreadable output
    def __str__(self):
        return f"Vehicle Speed: {self._speed}"

    # Todo: __repr__: For developers/ debugging. Returns a meaningful string and not shown in console. Visible in logs.
    def __repr__(self):  # repr: representation of an object
        return f"Vehicle (Speed= {self._speed})"

    def move(self):
        print("Vehicle is moving")


# Todo: Inheritance: IS-A relation. eg: Car is a Vehicle. Car gets all attributes and methods of Vehicle.
class Car(Vehicle):
    # rule: if a child class doesn't have init function, it calls its parent's init function automatically.
    # super().fn_name() is used to call a method from its parent class.
    def __init__(self, speed, steer):
        super().__init__(speed, steer)  # calls init function in parent class

    def honk(self):
        print("Beep")

    # Todo: Method over-riding
    def move(self):  # same method names with same name/type of arguments
        print("Car moving")


class Truck(Vehicle):
    def move(self):
        print("Truck is moving")


# Todo: Composition: HAS-A relation.eg: Electric car has both battery and motor but Electric car is not battery and motor.
class Battery:
    def supply_power(self):
        print("Battery supplying power")


class Motor:
    def rotate(self):
        print("Motor rotating")


class Electric_Car:
    def __init__(self, battery, motor):
        self.battery = battery
        self.motor = motor

    def drive(self):
        self.battery.supply_power()
        self.motor.rotate()


class Conversions:
    conversion_count = 0  # class variable

    # Todo: Static method: Method that belongs to a class, but does not use instance(obj) and class(cls) data.
    # no access to class variables or instance variables.
    @staticmethod  # behaves like a normal function but is logically grouped inside a  class.
    def kmh_to_ms(velocity):  # no self here as it does not depend on any object.
        return velocity / 3.6

    # Todo: Class method: Method that belongs to a class, but use class(cls) data only. Uses class reference-cls
    # has access to class data. does not depends on object and does not use self.
    @classmethod
    def convert_and_count(cls, velocity):
        cls.conversion_count += 1
        vel = cls.kmh_to_ms(velocity)
        print(vel)


# Todo: Data Class: Used when class mainly stores data
@dataclass  # used when class only stores data and no other complex behavior/logic is involved.
class VehicleState:
    x_position: float
    y_position: float
    speed: float


@dataclass
class SensorPacket:
    sensor_name: str
    time_stamp: float
    value: float


# when data class is used,python internally generates __init__(self,x_position,y_position,speed) and __repr__(self)
# which returns a meaningful string.

# Todo: Abstraction: Only tells what to do and not how to do. Sensor should have a read() but no implementation given.#
# An abstract class is a class with at least one abstract method in it.
class Sensor(ABC):  # should inherit abstract class. Any sensor must implement read()
    @abstractmethod
    def read(self) -> SensorPacket:  # -> represents type hint. type hint tells humans(for easier readability)
        # what type of value the function is expected to return. Here, this function should return an object of type
        # SensorPacket. this read() should be implemented in child classes of Sensor.
        pass  # no implementation given.


class RadarSensor(Sensor):
    def read(self) -> SensorPacket:
        # reading radar data here
        return SensorPacket("Radar", time.time(), value=12.3)  # value eg: distance in metres.


class CameraSensor(Sensor):
    def read(self) -> SensorPacket:
        # reading camera data here
        return SensorPacket("Camera", time.time(), value=11.8)  # here, a new object of SensorPacket class is created
        # and returned.

def log_sensor(sensor: Sensor): # an object named sensor of class Sensor is expected here.
    packet = sensor.read()
    print(f"Sensor name: {packet.sensor_name}, Time: {packet.time_stamp:.2f}, Value: {packet.value}")
# Todo: Polymorphism function
def start_moving(vehicle):  # this parameter variable - vehicle can be any name. here, an object is received.
    vehicle.move()  # the objects we create should have their own move()


car = Vehicle(40, 10)  # creating an object. here, python internally does Vehicle.__init__(car,40)
print(car._speed)  # manually overriding encapsulation
car._speed = 50  # setter
car.accelerate(10)
# car.set_speed(100)
# print(car.get_speed())
car.speed = 100  # internally, python consider this as car.speed(100) where 100 is passed as value. python looks
# whether there is a setter for speed. calls setter
print(car.speed)  # with @property, the speed() can be accessed like attribute. calls getter
car.move()
c = Car(40, 10)  # rule: if a child class doesn't have init function, it calls its parent's init function
# automatically.
c.move()
c.honk()
print(c.speed)
t = Truck(10, 10)
start_moving(c)  # c and t are objects. so c is the vehicle here.
start_moving(t)  # here, t which is an object of truck is the vehicle here.

grid = Battery()
servo = Motor()
ec = Electric_Car(grid, servo)  # objects of battery and motor are passed
ec.drive()

print(car)  # here, printing an object gives a meaningful string due to __str__.
str_speed = repr(car)  # a meaningful string is returned due to __repr__
print(str_speed)

conv_velocity = Conversions.kmh_to_ms(72)  # static method called without passing object.
print(conv_velocity)

Conversions.convert_and_count(36)  # class method called without passing object.
print(Conversions.conversion_count)

state = VehicleState(10.5, 20.0, 60)  # data class is used here.
print(state)

radar = RadarSensor()
camera = CameraSensor()
log_sensor(radar)
log_sensor(camera)