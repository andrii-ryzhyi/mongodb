from mongoengine import *
connect("students")


class Grades(EmbeddedDocument):
    grades = DictField()


class Person(Document):
    name = StringField(max_length=30, required=True)
    surname = StringField(max_length=30, required=True)

    meta = {'allow_inheritance': True}


    @classmethod
    def create(cls, **kwargs):
        return cls(**kwargs).save()

    @classmethod
    def read(cls, id=None, **kwargs):
        if id:
            return cls.objects(id=id)
        else:
            return tuple(cls.objects(name=kwargs["name"], surname=kwargs["surname"]))

    @classmethod
    def update(cls, current, updated=None):
        objects = cls.read(**current)
        for object in objects:
            for key, value in updated.items():
                object[key] = value
            object.save()

    @classmethod
    def delete(cls, obj=None, **kwargs):
        if isinstance(obj, cls):
            cls.objects(id=obj.id).delete()
            print(f"Object {obj} deleted")
        else:
            cls.objects(name=kwargs["name"], surname=kwargs["surname"]).delete()


class Mentor(Person):
    faculty = StringField()
    level = StringField()

class Student(Person):
    faculty = StringField(max_length=30)
    group = StringField(max_length=20)
    mentor = ReferenceField(Mentor, reverse_delete_rule=CASCADE)
    grades = EmbeddedDocumentField(Grades)
    subjects = ListField(StringField(max_length=30))


subjects = ["java", "c++", "linux"]
grades_list = {"java": 4, "c++": 3, "linux": 5}
grade = Grades()
grade.grades = grades_list
student = Student(name="Andrii", surname="Ryzhyi", faculty="Programming", group="1")
mentor = Mentor(name="Mentor", surname="Mentor", level="Middle").save()
student.mentor = mentor
student.grades = grade
student.save()

#CRUD OPERATIONS

st = Student.create(**{"name": "Insert", "surname": "Test"})
print(st.id)
print(type(st))

st_list = Student.read(**{"name": "Insert", "surname": "Test"})
for student in st_list:
    print(student)

Student.delete(**{"name": "Insert", "surname": "Test"})

Student.update({"name": "Andrii", "surname": "Ryzhyi"}, {"name": "Andrew"})
