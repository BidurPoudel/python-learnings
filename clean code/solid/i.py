class Printable:
    def printing():
        pass

class Scannable:
    def printing():
        pass
    
class BasicPrinter(Printable):
    def print(self):
        print("Printing...")

class AdvancedPrinter(Printable, Scannable):
    def print(self):
        print("Printing...")
    def scan(self):
        print("Scanning...")