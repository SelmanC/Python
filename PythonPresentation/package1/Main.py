
class Mensch:
    def __init__(self, groesse, alter):
        self.groesse = groesse
        self.alter = alter
        
    def __str__(self):
        return "Groeße = {0}, Alter = {1}".format(self.groesse, self.alter)

class Student(Mensch):
    
    def __init__(self, fach, semester, studenten_nr):
        self.fach = fach
        self.semester = semester
        self.__studenten_nr = studenten_nr
        
    def set_data(self, groesse, alter):
        Mensch.__init__(self, groesse, alter)
        
    def get_studenten_nr(self):
        return self.__studenten_nr
    
    def __str__(self):
        data_student = "{0}: Fach = {1}, Semester = {2}, ".format(self.__studenten_nr, self.fach, self.semester)
        data_mensch = Mensch.__str__(self)
        return data_student + data_mensch

if __name__ == "__main__":
    student = Student("Informatik", 6, 123456)
    student.set_data(180, 22)
    print(student)