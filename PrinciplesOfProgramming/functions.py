__author__ = "Kranthi"

def main():
    message1()
    message2()
    print("end of main stmts")


def message1():
    print("print stmt from message1")

def message2():
    print("print stmt from message2")
    message1()
    print("end of message2 function")


main()