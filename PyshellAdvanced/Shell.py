programs = open(
    "C:\\Users\\adamm\\Documents\\GitHub\\Music-game\\PyshellAdvanced\\Program.txt",
    "w+"
)

class Functions:
    def addToCode(self, code):
        programs.write(code + "\n")
        programs.flush()

    def loadProgram(self):
        programs.seek(0)
        return programs.read()

    def runProgram(self):
        programs.seek(0)
        exec(programs.read())

    def run(self):
        print('Python shell v1.0. Wpisz "edit" aby edytować program lub "run" aby go uruchomić.')
        while True:
            command = input(">>> ").lower()

            if command == "edit":
                code = input("Podaj komendę do dodania:\n")
                self.addToCode(code)

            elif command == "run":
                self.runProgram()

shell = Functions()
shell.run()
