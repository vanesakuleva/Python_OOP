from unittest import TestCase, main
from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero("hero", 1, 100, 100)
        self.enemy = Hero("enemy", 1, 50, 50)

    def test_init_work(self):
        self.assertEqual("hero", self.hero.username)
        self.assertEqual(1, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(100, self.hero.damage)

    def test_battle_exception_for_same_fighter(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle('hero')
            self.assertEqual("You cannot fight yourself", self.hero.battle)

    def test_battle_exception_with_lower_or_equal_to(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle("enemy")
            



if __name__ == '__main__':
    main()
