import data
import menu
import actions

students = []

while True:
    option = menu.show_menu()
    if option == "1":
        actions.add_student(students)
    elif option == "2":
        actions.view_students(students)
    elif option == "3":
        actions.top_3_students(students)
    elif option == "4":
        actions.calculate_general_average(students)
    elif option == "5":
        data.export_students(students)
        print("\nEstudiantes exportados exitosamente a students.csv\n")
    elif option == "6":
        if data.import_students(students):
            print("\nEstudiantes importados exitosamente desde students.csv\n")
    elif option == "7":
        print("Programa finalizado!!!")
        break