import unittest
import LA_Dice

class LivingAlchemyTest(unittest.TestCase):
    def test_equal_dice(self):
        for x in range(1,6):
            self.assertEqual(x, len(LA_Dice.DiceRoller.rollDice(x)))
    def test_combine_dice(self):

if __name__ == '__main__':
    unittest.main()
