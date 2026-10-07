import csv


def export_students(students):

    with open("students.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["full_name","section", "spanish_grade", "english_grade", "social_studies_grade", "science_grade"])

        for student in students:

            writer.writerow([student["full_name"], student["section"], student["spanish_grade"], student["english_grade"], student["social_studies_grade"], student["science_grade"]])

def import_students(students):

    try:
        with open("students.csv", "r", newline="", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            students.clear()  # Limpiar la lista antes de importar
            for row in reader:
                student = {"full_name": row["full_name"], "section": row["section"], "spanish_grade": int(row["spanish_grade"]), "english_grade": int(row["english_grade"]), "social_studies_grade": int(row["social_studies_grade"]), "science_grade": int(row["science_grade"])}
                students.append(student)
    except FileNotFoundError:
        print("El archivo students.csv no existe.")
        
        return False

    return True