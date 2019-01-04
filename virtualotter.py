import datetime
import re

class Request():

    def __init__(self, question):
        self.failed_request = "\nI'm sorry but I cannot understand the request"
        self.question = str(question).lower()

    def interpret(self):
        if self.question != "":

            task = ""
            try:
                task = re.search("(date|times|plus|minus|time|multipl|div)", self.question).group(0)
            except:
                print(self.failed_request)
                return

            if task == "date":
                return ("\nToday is " + str(datetime.datetime.now().day) + "/" + str(datetime.datetime.now().month) + "/" + str(datetime.datetime.now().year))
            elif task == "time":
                return ("\nIt is now " + str(datetime.datetime.now().hour) + ":" + str(datetime.datetime.now().minute))
            elif task in ["plus", "minus", "times", "multipl", "div"]:
                try:
                    x = int(re.findall("([0-9]+)", self.question)[0])
                    y = int(re.findall("([0-9]+)", self.question)[1])
                except:
                    print(self.failed_request)
                    return

                if task == "div":
                    return ("\nThe answer is " + str(x / y))
                elif task == "minus":
                    return ("\nThe answer is " + str(x - y))
                elif task == "times" or task == "multipl":
                    return ("\nThe answer is " + str(x * y))
                elif task == "plus":
                    return ("\nThe answer is " + str(x + y))

def main():
    print("Hello, my name is Otter. I can assist with simple arithmetic and the current date or time.")
    while True:
        user_input = input("What can I help you with? ")
        if user_input == "Quit":
            break
        else:
            new_request = Request(user_input)
        if new_request.interpret() != None:
            print(new_request.interpret())


if __name__ == "__main__":
    main()
