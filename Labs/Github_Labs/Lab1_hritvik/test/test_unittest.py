import sys
import os
import unittest

# Get the path to the project's root directory
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.append(project_root)

from src import moodbot

class TestMoodBot(unittest.TestCase):

    # --- Tests for calculate_sanity ---
    def test_sanity_normal_day(self):
        """Test a standard day with coffee and sleep."""
        self.assertEqual(moodbot.calculate_sanity(2, 7), 160)

    def test_sanity_all_nighter(self):
        """Test 4 coffees but 0 sleep."""
        self.assertEqual(moodbot.calculate_sanity(4, 0), 40)

    def test_sanity_negative_floor(self):
        """Ensure sanity doesn't drop below 0 even with negative sleep."""
        self.assertEqual(moodbot.calculate_sanity(0, -5), 0)

    # --- Tests for get_status ---
    def test_status_unstoppable(self):
        """Check the 'Unstoppable' boundary at 101."""
        self.assertEqual(moodbot.get_status(101), "Unstoppable Scholar")

    def test_status_functional_high(self):
        """Check the 'Functional' boundary at exactly 100."""
        self.assertEqual(moodbot.get_status(100), "Functional Human")

    def test_status_functional_low(self):
        """Check the 'Functional' boundary at exactly 50."""
        self.assertEqual(moodbot.get_status(50), "Functional Human")

    def test_status_brain_not_found(self):
        """Check the 'Error 404' boundary at 49."""
        self.assertEqual(moodbot.get_status(49), "Error 404: Last Brain cell Not Found")

    # --- Tests for generate_excuse ---
    def test_excuse_contains_dog(self):
        """Check if the dog flag returns the correct excuse keywords."""
        result = moodbot.generate_excuse(dog_ate_homework=True)
        self.assertIn("dog", result.lower())
        self.assertIn("python", result)

    def test_excuse_contains_dimension(self):
        """Check the default excuse keywords."""
        result = moodbot.generate_excuse(dog_ate_homework=False)
        self.assertIn("machine", result)

if __name__ == '__main__':
    unittest.main()