from config.database import Base
from sqlalchemy import Table, Column, Integer, ForeignKey, Date


# Tabla intermedia para la relación many-to-many entre Student y Subject
student_subject_association = Table(
    'student_subject_association',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('subject_id', Integer, ForeignKey('subjects.id'))
)

# Intermediate table for many-to-many relationship between Student and StudentProject
student_studentProject_association = Table (
    'students_student_projects_association',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('student_project_id', Integer, ForeignKey('student_projects.id'))
)

# Intermediate table for many-to-many relationship between Student and CollegeCareer
student_collegeCareer_association = Table (
    'students_college_careers_association',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('collegeCareer_id', Integer, ForeignKey('college_careers.id'))
)

# Intermediate table for many-to-many relationship between Student and ExtensionAvtivities
student_extensionActivities_association = Table (
    'students_extension_activities_association',
    Base.metadata,
    Column('student_id', Integer, ForeignKey('students.id')),
    Column('extension_activities_id', Integer, ForeignKey('extension_activities.id')),
    Column('date', Date)
)

# Intermediate table for many-to-many relationship between Subject and Grade
subjects_grades_association = Table (
    'subjects_grades_association',
    Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('grade_id', Integer, ForeignKey('grades.id')),
    Column('date', Date)
)

# Intermediate table for many-to-many relationship between Subject and CollegeCareer
subjects_college_careers_association = Table (
    'subjects_college_careers_association',
    Base.metadata,
    Column('subject_id', Integer, ForeignKey('subjects.id')),
    Column('college_career_id', Integer, ForeignKey('college_careers.id'))
)