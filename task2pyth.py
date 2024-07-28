class StudentGradeTracker:
    def __init__(self):
        self.grades = {}

    def add_grade(self, subject, grade):
        if subject in self.grades:
            self.grades[subject].append(grade)
        else:
            self.grades[subject] = [grade]

    def calculate_average(self):
        total_grades = 0
        count = 0
        for grades in self.grades.values():
            total_grades += sum(grades)
            count += len(grades)
        return total_grades / count if count != 0 else 0

    def get_letter_grade(self, average):
        if average >= 90:
            return 'A'
        elif average >= 80:
            return 'B'
        elif average >= 70:
            return 'C'
        elif average >= 60:
            return 'D'
        else:
            return 'F'

    def display_grades(self):
        print("\nStudent Grades:")
        for subject, grades in self.grades.items():
            print(f"{subject}: {grades}")

        average = self.calculate_average()
        letter_grade = self.get_letter_grade(average)
        print(f"\nAverage Grade: {average:.2f}")
        print(f"Letter Grade: {letter_grade}")

def main():
    tracker = StudentGradeTracker()

    while True:
        print("\n1. Add Grade")
        print("2. Calculate Average")
        print("3. Display Grades")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == '1':
            subject = input("Enter subject: ")
            try:
                grade = float(input("Enter grade: "))
                if 0 <= grade <= 100:
                    tracker.add_grade(subject, grade)
                else:
                    print("Grade must be between 0 and 100.")
            except ValueError:
                print("Invalid input! Please enter a number.")
        
        elif choice == '2':
            average = tracker.calculate_average()
            print(f"\nAverage Grade: {average:.2f}")
            letter_grade = tracker.get_letter_grade(average)
            print(f"Letter Grade: {letter_grade}")

        elif choice == '3':
            tracker.display_grades()

        elif choice == '4':
            break

        else:
            print("Invalid choice! Please enter a number between 1 and 4.")

if __name__ == "__main__":
    main()
