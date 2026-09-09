def add_student(students):
    full_name = input("Ingrese el nombre completo del estudiante: ").upper().strip()
    section = input("Ingrese la sección del estudiante: ").upper().strip()
    spanish_grade = get_valid_grade("Español")
    english_grade = get_valid_grade("Inglés")
    social_studies_grade = get_valid_grade("Estudios Sociales")
    science_grade = get_valid_grade("Ciencias")
    student = {
        "full_name": full_name,
        "section": section,
        "spanish_grade": spanish_grade,
        "english_grade": english_grade,
        "social_studies_grade": social_studies_grade,
        "science_grade": science_grade,
    }
    students.append(student)


def get_valid_grade(subject):   
    while True:
        try:
            grade = int(input(f"Ingrese la nota de {subject}: "))
            if 0 <= grade <= 100:
                return grade
            else:
                print("La nota debe estar entre 0 y 100. Intente nuevamente.")
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")
    

def view_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return
    for student in students:
        print(f"Nombre: {student['full_name']}, Sección: {student['section']}, "
              f"Español: {student['spanish_grade']}, Inglés: {student['english_grade']}, "
              f"Estudios Sociales: {student['social_studies_grade']}, Ciencias: {student['science_grade']}")


def calculate_average(student):
    if not student:
        print("No hay estudiantes registrados.")
        return
    average = (student['spanish_grade'] + student['english_grade'] +
               student['social_studies_grade'] + student['science_grade']) / 4
    return average


def top_3_students(students):
    if not students:
        print("No hay estudiantes registrados.")
        return
    sorted_students = sorted(students, key=calculate_average, reverse=True)
    top_students = sorted_students[:3]
    print("Los 3 mejores estudiantes son:")
    for student in top_students:
        average = calculate_average(student)
        print(f"Nombre: {student['full_name']}, Promedio: {average:.2f}")


def calculate_general_average(students):
    if not students:
        print("No hay estudiantes registrados.")
        return
    total_average = sum(calculate_average(student) for student in students)
    general_average = total_average / len(students)
    print(f"Promedio general de los estudiantes: {general_average:.2f}")