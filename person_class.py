"""Person Class - Implement person class."""


class Person:
    """Person class."""

    initialAge = 0

    def __init__(self, initialAge):
        """__init__ function."""
        # Add some more code to run some checks on initialAge
        self.age = initialAge
        if self.age < 0:
            print("Age is not valid, setting age to 0.")
            self.age = 0

    def am_i_old(self):
        """am_i_old function."""
        # Do some computations in here and print out the correct statement to
        # the console
        if self.age < 13:
            print("You are young.")
        elif self.age >= 13 and self.age <= 18:
            print("You are a teenager.")
        else:
            print("You are old.")

    def year_passes(self):
        """year_passes function."""
        # Increment the age of the person in here
        self.age = self.age + 1


if __name__ == "__main__":
    age = 13
    p = Person(age)
    p.am_i_old()
    p.year_passes()
