"""You can use this class to represent how classy someone
or something is.
"Classy" is interchangable with "fancy".
If you add fancy-looking items, you will increase
your "classiness".
Create a function in "Classy" that takes a string as
input and adds it to the "items" list.
Another method should calculate the "classiness"
value based on the items.
The following items have classiness points associated
with them:
"tophat" = 2
"bowtie" = 4
"monocle" = 5
Everything else has 0 points.
Use the test cases below to guide you!"""


class Classy:
    """Classy class."""

    def __init__(self):
        """__init__ function."""
        self.items = []

    def add_item(self, stringObj):
        """add_item function."""
        self.items.append(stringObj)

    def get_classiness(self):
        """get_classiness function."""
        points = 0
        for i in self.items:
            if i == "tophat":
                points = points + 2
            elif i == "bowtie":
                points = points + 4
            elif i == "monocle":
                points = points + 5
            else:
                points = points + 0
        return points


# Test cases
me = Classy()

# Should be 0
print(me.get_classiness())


me.add_item("tophat")
# Should be 2
print(me.get_classiness())

me.add_item("bowtie")
me.add_item("jacket")
me.add_item("monocle")
# Should be 11
print(me.get_classiness())

me.add_item("bowtie")
# Should be 15
print(me.get_classiness())
