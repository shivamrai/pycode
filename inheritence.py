#hackerrank inheritence example
class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
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
        super().__init__(firstName, lastName, idNumber)
        self.scores = scores    
        Person.__init__(self, firstName, lastName, idNumber)
    #   Function Name: calculate
    #   Return: A character denoting the grade.
    #
    # Write your function here
    def calculate(self):
        sumOfScores = 0
        for score in self.scores:
            sumOfScores+=score
        average = sumOfScores/len(self.scores)
        grade = 'F'
        if(average >= 90 and average <= 100):
            grade = 'O'
        elif(average >=80 and average < 90):
            grade = 'E'
        elif(average >=70 and average < 80):
            grade = 'A'
        elif(average >=55 and average < 70):
            grade = 'P'
        elif(average >=40 and average < 55):
            grade = 'D'
        else: grade = 'T'
        return grade