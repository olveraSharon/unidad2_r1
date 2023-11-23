#Autor: Sharon Michelle Olvera Ibarra
#Descripción: Evaluando los resultados de los estudiantes
#Fecha: 21/11/2023

class StudentsDataException(Exception):
    pass


class WrongLine(StudentsDataException):
    def __init__(self, line_number, line_content):
        self.line_number = line_number
        self.line_content = line_content
        super().__init__(f"Error in line {line_number}: {line_content}")


class FileEmpty(StudentsDataException):
    def __init__(self, file_name):
        self.file_name = file_name
        super().__init__(f"The file '{file_name}' is empty.")


class StudentsDataProcessor:
    def __init__(self, file_name):
        self.file_name = file_name
        self.students_data = {}

    def process_file(self):
        try:
            with open(self.file_name, 'r') as file:
                lines = file.readlines()

                if not lines:
                    raise FileEmpty(self.file_name)

                for line_number, line in enumerate(lines, start=1):
                    self.process_line(line_number, line)

                self.print_report()

        except FileNotFoundError:
            print(f"The file '{self.file_name}' was not found.")
        except StudentsDataException as e:
            print(f"Error: {e}")

    def process_line(self, line_number, line):
        try:
            parts = line.strip().split()
            if len(parts) != 3:
                raise WrongLine(line_number, line)

            first_name, last_name, points_str = parts
            points = float(points_str)

            student_key = (first_name, last_name)
            self.students_data[student_key] = self.students_data.get(student_key, 0) + points

        except ValueError:
            raise WrongLine(line_number, line)

    def print_report(self):
        sorted_data = sorted(self.students_data.items(), key=lambda x: x[0])

        for student, total_points in sorted_data:
            first_name, last_name = student
            print(f"{first_name} {last_name} \t {total_points}")


# Solicitar al usuario el nombre del archivo
file_name = input("Ingrese el nombre del archivo del profesor Jekyll: ")

# Crear y procesar el objeto StudentsDataProcessor
processor = StudentsDataProcessor(file_name)
processor.process_file()