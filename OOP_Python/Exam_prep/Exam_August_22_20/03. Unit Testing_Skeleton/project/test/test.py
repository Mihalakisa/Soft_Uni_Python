from unittest import TestCase
from project.student_report_card import StudentReportCard


class StudentReportCardTest(TestCase):
    def setUp(self) -> None:
        student_name = 'Pesho'
        school_year = 6
        self.student_card = StudentReportCard(student_name, school_year)

    def test_student_init(self):
        self.assertEqual('Pesho', self.student_card.student_name)
        self.assertEqual(6, self.student_card.school_year)
        self.assertEqual({}, self.student_card.grades_by_subject)

    def test_student_name_error_msg_empty_string(self):
        with self.assertRaises(ValueError) as error:
            self.student_card.student_name = ''
        self.assertEqual("Student Name cannot be an empty string!", str(error.exception))

    def test_student_year_lower_than_one_or_greater_than_twelve(self):
        with self.assertRaises(ValueError) as error:
            self.student_card.school_year = 0
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

        with self.assertRaises(ValueError) as error:
            self.student_card.school_year = 13
        self.assertEqual("School Year must be between 1 and 12!", str(error.exception))

    def test_add_grade(self):
        subject = 'Math'

        self.student_card.add_grade(subject, 5)
        self.assertTrue(subject in self.student_card.grades_by_subject)
        self.student_card.add_grade(subject, 3)
        self.assertEqual(1, len(self.student_card.grades_by_subject))
        self.assertTrue(2, len(self.student_card.grades_by_subject[subject]))

    def test_average_grade_by_subject(self):
        subject = 'Math'
        average_grade = 4
        self.student_card.add_grade(subject, 5)
        self.student_card.add_grade(subject, 3)
        result = self.student_card.average_grade_by_subject()
        self.assertEqual(f"{subject}: {average_grade:.2f}\n".strip(), result)
        self.assertTrue(subject in self.student_card.grades_by_subject)
        self.assertEqual([5, 3], self.student_card.grades_by_subject[subject])

    def test_average_grade_for_all_subjects(self):
        subject = 'Math'
        self.student_card.add_grade(subject, 5)
        self.student_card.add_grade(subject, 3)
        result = self.student_card.average_grade_for_all_subjects()
        self.assertEqual(f"Average Grade: {8/ 2 :.2f}", result)
        self.assertTrue(subject in self.student_card.grades_by_subject)
        self.assertEqual([5, 3], self.student_card.grades_by_subject[subject])

    def test_repr(self):
        subject = 'Math'
        self.student_card.add_grade(subject, 5)
        self.student_card.add_grade(subject, 3)
        result_all_grades = self.student_card.average_grade_by_subject()
        result_all_subjects = self.student_card.average_grade_for_all_subjects()

        report = f"Name: {self.student_card.student_name}\n" \
                 f"Year: {self.student_card.school_year}\n" \
                 f"----------\n" \
                 f"{result_all_grades}\n" \
                 f"----------\n" \
                 f"{result_all_subjects}"

        self.assertEqual(repr(self.student_card), report)