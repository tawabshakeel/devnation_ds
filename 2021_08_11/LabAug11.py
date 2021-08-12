# Question 1

patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(weight, height):
    return weight / (height ** 2)


for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)

# Question 2

greeting = input("Hello, possible pirate! What's the password?")

if greeting in ["Arrr!"]:
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")

# Question 3

authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"}

for author in authors:
    print("%s" % author + " died in " + authors[author])

# Question 4

year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print("Woah, that's the past!")
elif year > 1900 & year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")


# Question 5

class Person:
    def __init__(self, first_name, last_name):
        self.first = first_name
        self.last = last_name

    def speak(self):
        print("My name is " + self.first + " " + self.last)


me = Person("Brandon", "Walsh")
you = Person("Ethan", "Reed")

me.speak()
you.speak()

#Question 6

exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_3 = int(input("Input exam grade three: "))
grades = [exam_one, exam_two,exam_3]
sum = 0

for grade in grades:
    sum = sum + grade

    avg = sum / len(grades)

    if avg >= 90:
        letter_grade = "A"
    elif avg >= 80 and avg < 90:
        letter_grade = "B"
    elif avg > 69 and avg < 80:
        letter_grade = "C"
    elif avg <= 69 and avg >= 65:
        letter_grade = "D"
    else:
        letter_grade = "F"



print("Exam: " + str(grades))
print("Average: " + str(avg))
print("Grade: " + letter_grade)

if letter_grade == "F":
    print ("Student is failing.")
else:
    print ("Student is passing.")
