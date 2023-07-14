from django.core.management.base import BaseCommand
from django.contrib.auth.models import Permission
from academy.models import Teacher, Student, Course, Subject, Subscription

class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument("--mode", type = str, help = "Mode: load / clear")
    
    def handle(self, *args, **options):
        print("Data inicial")

        self.seeds_subject(options.get('mode'))
        print("Subjects: ", Subject.objects.all().count())

        self.seeds_student(options.get('mode'))
        print("Students: ", Student.objects.all().count())

        self.seeds_course(options.get('mode'))
        print("Courses: ", Course.objects.all().count())

        self.seeds_teacher(options.get('mode'))
        print("Teachers: ", Teacher.objects.all().count())

    def seeds_subject(self, mode):
        if mode == "load" and Subject.objects.all().count() <= 0:
            self.seeds_course(mode)
            self.seeds_teacher(mode)

            ss = Subject()
            ss.course = Course.objects.get(name = "Matematica Avanzada")
            ss.teacher = Teacher.objects.get(first_name = "Pepito")
            ss.start_date = "2023-08-10"
            ss.save()

            ss = Subject()
            ss.course = Course.objects.get(name = "Literatura")
            ss.teacher = Teacher.objects.get(first_name = "Carlito")
            ss.start_date = "2023-10-15"
            ss.save()
        elif mode == "clear":
            Subject.objects.all().delete()

    def seeds_student(self, mode):
        if mode == "load" and Student.objects.all().count() <= 0:
            s = Student()
            s.username = "juancito"
            s.first_name = "Juancito"
            s.last_name = "Espinoza"
            s.email = "juan@gmail.com"
            s.is_staff = True
            s.is_active = True
            s.set_password("123456")
            s.save()
            perm = Permission.objects.get(name = "Can add subscription") #captura el permiso
            s.user_permissions.add(perm) #asigna el permiso

            s = Student()
            s.username = "ramiro"
            s.first_name = "Ramiro"
            s.last_name = "Espinoza"
            s.email = "ramiro@gmail.com"
            s.is_staff = True
            s.is_active = True
            s.set_password("123456")
            s.save()
            perm = Permission.objects.get(name = "Can add subscription") #captura el permiso
            s.user_permissions.add(perm) #asigna el permiso


        elif mode == "clear":
            Student.objects.all().delete()

    def seeds_course(self, mode):
        if mode == "load" and Course.objects.all().count() <= 0:
            c = Course()
            c.name = "Matematica Avanzada"
            c.description = "Una matematica pero avanzada"
            c.save()

            c = Course()
            c.name = "Literatura"
            c.description = "Literatura del siglo XI"
            c.save()
        elif mode == "clear":
            Course.objects.all().delete()


    def seeds_teacher(self, mode):
        # mode puede ser load o clear
        if mode == "load" and Teacher.objects.all().count() <= 0:
            # Verificamos que solo see creen docentes una sola vez
            t = Teacher()
            t.username = "pepito"
            t.first_name = "Pepito"
            t.last_name = "Alcachofa"
            t.bio = "Este es un bio del docente"
            t.is_staff = True
            t.is_active = True
            t.set_password('123456')
            t.save()

            t = Teacher()
            t.username = "carlito"
            t.first_name = "Carlito"
            t.last_name = "Alcachofa"
            t.is_staff = True
            t.is_active = True
            t.bio = "Este es un bio del docente"
            t.set_password('123456')
            t.save()
        elif mode == "clear":
            Teacher.objects.all().delete()

        