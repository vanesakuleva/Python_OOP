from project.truck_driver import TruckDriver
import unittest


class TestTruckDriver(unittest.TestCase):
    def test_init_with_valid_data(self):
        truck = TruckDriver("Test", 5)

        self.assertEqual("Test", truck.name)
        self.assertEqual(5, truck.money_per_mile)
        self.assertEqual({}, truck.available_cargos)
        self.assertEqual(0, truck.earned_money)
        self.assertEqual(0, truck.miles)

    def test_earned_money(self):
        truck = TruckDriver("Test", 5)
        with self.assertRaises(ValueError) as er:
            TruckDriver("Test", 10)
            truck.earned_money = -5
        self.assertEqual(f"Test went bankrupt.", str(er.exception))

    def test_if_correct_add_cargo_offered(self):
        truck = TruckDriver("Test", 10)
        truck.add_cargo_offer("Ekont", 20)
        truck.add_cargo_offer("Spidi", 20)
        self.assertEqual(truck.available_cargos, {"Ekont": 20, "Spidi": 20})


    def test_for_rise_exeption_if_cargo_is_alredy_added(self):
        with self.assertRaises(Exception) as ex:

            truck = TruckDriver("Test", 10)
            truck.add_cargo_offer("Ekont", 20)
            truck.add_cargo_offer("Ekont", 20)
        self.assertEqual("Cargo offer is already added.", str(ex.exception) )

    def test_if_adding_correctrly_return(self):
        truck = TruckDriver("Test", 10)
        result = truck.add_cargo_offer("Ekont", 20)
        self.assertEqual(result, "Cargo for 20 to Ekont was added as an offer.")



    def test_for_check_activities(self):
        truck = TruckDriver("Test", 10)
        truck.miles = 1
        truck.earned_money = 1000000
        truck.eat(1)
        truck.sleep(1)
        truck.pump_gas(1)
        truck.repair_truck(1)
        self.assertEqual(truck.repair_truck(1), None)
        self.assertEqual(truck.check_for_activities(1),None)
        self.assertEqual(truck.earned_money, 1000000)

    def test_for_check_activities_one(self):
        truck = TruckDriver("Test", 10)
        truck.miles = 250
        truck.earned_money = 1000000
        truck.eat(250)
        truck.sleep(250)
        truck.pump_gas(250)
        truck.repair_truck(250)
        self.assertEqual(truck.repair_truck(1), None)
        self.assertEqual(truck.check_for_activities(1), None)
        self.assertEqual(truck.earned_money, 999980)

    def test_for_drive_best_cargo_offer(self):

            truck = TruckDriver("Test", 10)
            truck.miles=250
            truck.available_cargos = {"Ekont": 20, "Spidi": 20}
            truck.drive_best_cargo_offer()

            self.assertEqual(truck.drive_best_cargo_offer() , "Test is driving 20 to Ekont.")

    def test_for_drive_best_cargo_offer_one(self):

            truck = TruckDriver("Test", 10)
            truck.miles=0
            truck.available_cargos = {}
            truck.drive_best_cargo_offer()

            self.assertEqual(truck.drive_best_cargo_offer() ,"There are no offers available."
)



    def test_for_check_eat(self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 100
        result = truck.eat(250)
        res= truck.earned_money
        self.assertEqual(result, None)
        self.assertEqual(res, 80)

    def test_if_mile_dont_equal (self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 100
        result = truck.eat(23)
        res = truck.earned_money
        self.assertEqual(res, 100)


    def test_for_sleep(self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 600
        result = truck.sleep(150)
        res= truck.earned_money
        self.assertEqual(result, None)
        self.assertEqual(res, 600)

    def test_for_sleep_with_correct(self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 600
        result = truck.sleep(1000)
        res= truck.earned_money
        self.assertEqual(result, None)
        self.assertEqual(res, 555)


    def test_for_pump_gas(self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 600
        result = truck.pump_gas(250)
        res= truck.earned_money
        self.assertEqual(result, None)
        self.assertEqual(res, 600)


    def test_if_mile_is_equal (self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 600
        result = truck.pump_gas(1500)
        res = truck.earned_money
        self.assertEqual(res, 100)

    def test_if_repair_truck (self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 10000
        result = truck.repair_truck(150)
        res = truck.earned_money
        self.assertEqual(res, 10000)

    def test_if_repair_truck_correct (self):
        truck = TruckDriver("Test", 10)
        truck.earned_money = 10000
        result = truck.repair_truck(10000)
        res = truck.earned_money
        self.assertEqual(res, 2500)

    def test_for__repr_correct(self):
        truck = TruckDriver("Test", 10)
        result = repr(truck)
        expected = "Test has 0 miles behind his back."
        self.assertEqual(expected, result)

    def test_for__repr_correct_with_miles(self):
        truck = TruckDriver("Test", 10)
        truck.miles = 100
        result = repr(truck)
        expected = "Test has 100 miles behind his back."
        self.assertEqual(expected, result)


if __name__== "__main__":
    unittest.main()