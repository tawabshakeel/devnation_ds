# QUESTION -- 01
patients = [[70, 1.8], [80, 1.9], [150, 1.7]]


def calculate_bmi(patient_weight, patient_height):
    return patient_weight / (patient_height ** 2)


for patient in patients:
    weight, height = patient
    bmi = calculate_bmi(height, weight)
    print("Patient's BMI is: %f" % bmi)
# -------------------------------------------------


# QUESTION -- 02
greeting = input("Hello, possible pirate! What's the password?")

if greeting in "Arr!":
    print("Go away, pirate.")
else:
    print("Greetings, hater of pirates!")
# -------------------------------------------------


# QUESTION -- 03
authors = {
    "Charles Dickens": "1870",
    "William Thackeray": "1863",
    "Anthony Trollope": "1882",
    "Gerard Manley Hopkins": "1889"
}

for date in authors.keys():
    print("%s" % date + " died in " + "%d." % int(authors[date]))
# -------------------------------------------------


# QUESTION -- 04
year = int(input("Greetings! What is your year of origin?"))

if year <= 1900:
    print("Woah, that's the past!")
elif 1900 < year < 2020:
    print("That's totally the present!")
else:
    print("Far out, that's the future!!")


# -------------------------------------------------


# QUESTION -- 05
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
# -------------------------------------------------


# QUESTION -- 06
exam_one = int(input("Input exam grade one: "))
exam_two = int(input("Input exam grade two: "))
exam_three = int(input("Input exam grade three: "))

grades = [exam_one, exam_two, exam_three]
my_sum = 0

for grade in grades:
    my_sum = my_sum + grade

avg = my_sum / len(grades)

if avg >= 90:
    letter_grade = "A"
elif 80 <= avg < 90:
    letter_grade = "B"
elif 69 < avg < 80:
    letter_grade = "C"
elif 69 >= avg >= 65:
    letter_grade = "D"
else:
    letter_grade = "F"

for grade in grades:
    print("Exam: " + str(grade))
    print("Average: " + str(avg))
    print("Grade: " + letter_grade)

if letter_grade == "F":
    print("Student is failing.")
else:
    print("Student is passing.")
