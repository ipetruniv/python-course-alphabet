
def import_p(filename: str):
   try:
       with open(filename, "rb") as file:
           return pickle.load(file)
   except Exception as e:
       print("Import failed:", e)

def less(*arg):

    return

class Programmer:

    def __init__(self, name, language="Python", position="Junior", age=int(16)) -> None:
        self.name = name
        self.language = language
        self.position = position
        self.age = age

    # <=
    def __le__(self, other):
        return float(self.age()) <= float(other.age())

    # >=
    def __ge__(self, other):
        return  float(self.age()) >= float(other.age())

    # <
    def __lt__(self, other):
        return  float(self.age()) < float(other.age())



    def __gt__(self, other):



        if float(self.age()) > float(other.age()):
            return True
        else:
            return False

    # ==



    def __eq__(self, other):
        if float(self.age()) == float(other.age()):
            return True
        else:
            return False

    # !=



    def __ne__(self, other):
        if float(self.age()) != float(other.age()):
            return True
        else:
            return False


