"""
Start: 5:23 PM
Stop: 6:10 PM
"""


class ProgrammingLanguage:
    """Display programming language information ."""

    def __init__(self, name, typing, reflection, year):
        """Pick a ProgrammingLanguage from the info given."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def __str__(self):
        return "{}, {} Typing, Reflection={}, First appeared in {}".format(self.name, self.typing, self.reflection,
                                                                           self.year)

    def is_dynamic(self):
        """Determine if language is dynamically typed."""
        return self.typing == "Dynamic"


p1 = ProgrammingLanguage("Java", "Dynamic", True, 1991)
print(p1)
