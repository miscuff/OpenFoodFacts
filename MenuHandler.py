

class MenuHandler:

    def __init__(self):
        self.continue_program = True

    def show_menu(self):
        while self.continue_program:
            print("""
            1.Add a Student
            2.Delete a Student
            3.Look Up Student Record
            4.Exit/Quit
            """)
            ans = raw_input("What would you like to do? ")
            if ans == "1":
                print("\n Student Added")
            elif ans == "2":
                print("\n Student Deleted")
            elif ans == "3":
                print("\n Student Record Found")
            elif ans == "4":
                print("\n Goodbye")
            elif ans != "":
                print("\n Not Valid Choice Try again")