import pytest
from src import moodbot


def test_calculate_sanity_scenarios():
    # Test typical day
    assert moodbot.calculate_sanity(2, 6) == 140
    # Test all-nighter (0 sleep)
    assert moodbot.calculate_sanity(4, 0) == 40
    # Test the floor (sanity shouldn't be negative)
    assert moodbot.calculate_sanity(0, -5) == 0
    # Test extreme caffeine
    assert moodbot.calculate_sanity(10, 8) == 260

def test_status_messages():
    # Test "Unstoppable" boundary
    assert moodbot.get_status(101) == "Unstoppable Scholar"
    # Test "Functional" boundaries
    assert moodbot.get_status(100) == "Functional Human"
    assert moodbot.get_status(50) == "Functional Human"
    # Test "Brain cell Not Found" boundaries
    assert moodbot.get_status(49) == "Error 404: Last Brain cell Not Found"
    assert moodbot.get_status(0) == "Error 404: Last Brain cell Not Found"

def test_excuse_generator():
    # Test the default excuse
    assert "machine" in moodbot.generate_excuse()
    # Test the dog excuse
    assert "dog" in moodbot.generate_excuse(dog_ate_homework=True)
    # Test that they are different
    assert moodbot.generate_excuse(True) != moodbot.generate_excuse(False)