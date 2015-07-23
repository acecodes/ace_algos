import sqlite3
from os import system


class Student:

    def __init__(self, first_name, last_name, score1, score2, score3, score4, score5):
        self.first_name = first_name
        self.last_name = last_name
        self.score1 = score1
        self.score2 = score2
        self.score3 = score3
        self.score4 = score4
        self.score5 = score5

    def rank(self):
        grades = [self.score1, self.score2, self.score3, self.score4]
        sorted(grades)
        return grades

    def average(self):
        grades = [self.score1, self.score2, self.score3, self.score4]
        return int(sum(grades) / len(grades))

    def grade(self):
        letters = [(100, "A+"), (95, "A"), (90, "A-"), (89, "B+"), (85, "B"), (80, "B-"),
                   (79, "C+"), (75, "C"), (70, "C-"), (69, "D+"), (65, "D"), (60, "D-"), (59, "F")]

        if self.average() <= 59:
            return "F"

        for grades, letters in letters:
            if self.average() == grades:
                return letters
            elif (self.average() >= grades and abs(self.average()) - abs(grades) < 4 or abs(self.average()) - abs(grades) >= 2):
                return letters

    def __call__(self):
        print("{first} {last}: ".format(
            first=self.first_name, last=self.last_name)),
        for items in self.rank():
            print(str(items) + " "),


class Database:

    def __init__(self, title):
        self.title = title

    def create_db(self):

        system("""rm {title}.db""".format(title=self.title))

        conn = sqlite3.connect("{title}.db".format(title=self.title))
        cursor = conn.cursor()

        cursor.executescript("""

            CREATE TABLE {title} (FirstName char(50), 
                      LastName char(50), 
                      Average INT(3),
                      Grade char(2), 
                      Score1 INT(3), 
                      Score2 INT(3), 
                      Score3 INT(3), 
                      Score4 INT(3), 
                      Score5 INT(3));

            """.format(title=self.title))

        conn.commit()
        cursor.close()
        conn.close()

    def student_insert(self, student_obj):
        conn = sqlite3.connect("{title}.db".format(title=self.title))
        cursor = conn.cursor()
        result = cursor.fetchall()

        cursor.execute("""INSERT INTO Grades (FirstName, LastName, Average, Grade, Score1, Score2, Score3, Score4, Score5)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)""", (student_obj.first_name, student_obj.last_name, student_obj.average(), student_obj.grade(), student_obj.score1,
                                           student_obj.score2, student_obj.score3, student_obj.score4, student_obj.score5))

        conn.commit()
        cursor.close()
        conn.close()

    def __call__(self):
        conn = sqlite3.connect("{title}.db".format(title=self.title))
        cursor = conn.cursor()
        result = cursor.fetchall()

        grades = cursor.execute(
            '''SELECT * FROM Grades ORDER BY Average DESC;''')

        for results in grades:
            for students in results:
                print(str(students).ljust(5)),
            print

        conn.commit()
        cursor.close()
        conn.close()


if __name__ == "__main__":
    Bob = Student("Bob", "Smith", 69, 69, 69, 69, 65)
    Jane = Student("Jane", "Doe", 81, 79, 99, 59, 45)
    Grades = Database("Grades")
    Grades.create_db()
    Grades.student_insert(Bob)
    Grades.student_insert(Jane)
    print(Grades())
