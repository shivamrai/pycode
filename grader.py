def gradingStudents(grades):
    # Write your code here
    for i in range(len(grades)):
        if grades[i] >= 38:
            multipleof5 = ((int)(grades[i] / 5) + 1) * 5
            roundOffDifference = multipleof5 - grades[i]
            if roundOffDifference < 3:
                grades[i] = grades[i] + roundOffDifference
    return grades


if __name__ == "__main__":
    grade = [73, 67, 38, 33]
    gradenew = gradingStudents(grade)
    print(gradenew)
