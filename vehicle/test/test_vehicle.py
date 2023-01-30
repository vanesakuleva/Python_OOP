from project.vehicle import Vehicle
from unittest import TestCase, main


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(20.5, 150.6)

    def test_fuel_consumption_is_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_init(self):
        self.assertEqual(20.5, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(20.5, self.vehicle.capacity)
        self.assertEqual(150.6, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_car_without_enought_fuel_rise_exeption(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_car_with_enough_fuel_expect_fuel_decrease(self):
        self.vehicle.drive(5)
        needed_fuel = 5 * 1.25

        self.assertEqual(14.25, self.vehicle.fuel)

    def test_car_refuel_raise_exception_without_enough_capacity(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(300)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_car_with_enough_capacity_increase_fuel(self):
        self.vehicle.drive(5)
        self.vehicle.refuel(1)

        self.assertEqual(15.25,self.vehicle.fuel)

    def test_correct__str__(self):
        result = str(self.vehicle)
        expected = "The vehicle has 150.6 " \
               "horse power with 20.5 fuel left and 1.25 fuel consumption"

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
