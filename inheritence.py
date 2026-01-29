"""Inheritance - Demonstrate class inheritance."""


# hackerrank inheritence example
class Person:
    """Person class."""

    def __init__(self, firstName, lastName, idNumber):
        """__init__ function."""
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def print_person(self):
        """print_person function."""
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    """Student class."""

    #   Class Constructor
    #
    #   Parameters:
    #   firstName - A string denoting the Person's first name.
    #   lastName - A string denoting the Person's last name.
    #   id - An integer denoting the Person's ID number.
    #   scores - An array of integers denoting the Person's test scores.
    #
    # Write your constructor here
    def __init__(self, firstName, lastName, idNumber, scores):
        """__init__ function."""
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores
        Person.__init__(self, firstName, lastName, idNumber)

    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        """calculate function."""
        sumOfScores = 0
        for score in self.scores:
            sumOfScores += score
        average = sumOfScores / len(self.scores)
        grade = "F"
        if 90 <= average <= 100:
            grade = "O"
        elif 80 <= average < 90:
            grade = "E"
        elif 70 <= average < 80:
            grade = "A"
        elif 55 <= average < 70:
            grade = "P"
        elif 40 <= average < 55:
            grade = "D"
        else:
            grade = "T"
        return grade
