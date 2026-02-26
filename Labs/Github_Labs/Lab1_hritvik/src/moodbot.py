def calculate_sanity(coffee_cups, hours_slept):
    """Calculates sanity level. Sanity cannot be negative."""
    score = (coffee_cups * 10) + (hours_slept * 20)
    return max(0, score)

def get_status(sanity_score):
    """Returns a status string based on the sanity score."""
    if sanity_score > 100:
        return "Unstoppable Scholar"
    elif sanity_score >= 50:
        return "Functional Human"
    else:
        return "Error 404: Last Brain cell Not Found"

def generate_excuse(dog_ate_homework=False):
    """Generates a highly believable excuse for late submissions."""
    if dog_ate_homework:
        return "My dog got eaten by a python."
    return "The code worked on my machine, but my machine is broken."