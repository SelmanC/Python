import unittest
from package1 import *

class Test(unittest.TestCase):


    def setUp(self):
        print("StartTest!")
        self.student = Main.Student("Informatik", 6, 123456)
        self.student.set_data(180, 22)
        pass


    def testName(self):
        test_string = ("123456: Fach = Informatik, Semester = 6, "
                      "Groeße = 180, Alter = 22")
        self.assertEqual(str(self.student), test_string)
        pass
    
    
    def tearDown(self):
        print("EndTest!")



if __name__ == "__main__":
    unittest.main()