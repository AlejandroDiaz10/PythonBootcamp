from car import Car


class TrafficManager:
    def __init__(self):
        self.car_list = []
        self.cars_speed = 0.1

    def create_car(self):
        new_car = Car()
        self.car_list.append(new_car)

    def move_traffic(self):
        for car in self.car_list:
            car.drive()

    def accident_detected(self, turtle):
        for car in self.car_list:
            if car.has_crashed(turtle):
                return True
        return False

    def clear_traffic(self):
        # We only keep a third of the cars created
        limit = int(len(self.car_list) / 3)
        for car in self.car_list[limit:]:
            car.clear_car()

        self.car_list = self.car_list[:limit]
        for car in self.car_list:
            car.reset_car()
