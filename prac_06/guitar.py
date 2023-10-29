"""

"""
CURRENT_YEAR = 2023
VINTAGE_AGE = 60


class Guitar:
    """Store details of a guitar."""

    def __init__(self, name="", year=0, cost=0):
        """Model a Guitar from the given fields."""
        self.name = name
        self.year = year
        self.cost = cost

    def __str__(self):
        """Return string format of a Guitar."""
        return "My guitar: {}, first made in ({}) , worth ${:,.2f}".format(self.name, self.year, self.cost)

    def get_age(self):
        """Get the age of a guitar based on the CURRENT_YEAR."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if a Guitar is 60 or more years old."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        return self.year < other.year
