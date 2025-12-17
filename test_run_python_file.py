from functions.run_python_file import run_python_file

def test_python_file():

    result = run_python_file("calculator", "main.py")
    print("Result of main file")
    print(result)
    print("")

    result = run_python_file("calculator", "main.py", ["3 + 5"])
    print("Result of main file")
    print(result)
    print("")

    result = run_python_file("calculator", "tests.py")
    print("Result of test file")
    print(result)
    print("")

    result = run_python_file("calculator", "../main.py")
    print("Result of ../main.py file")
    print(result)
    print("")

    result = run_python_file("calculator", "nonexistent.py")
    print("Result of nonexistent file")
    print(result)
    print("")

    result = run_python_file("calculator", "lorem.txt")
    print("Result of lorem file")
    print(result)
    print("")

if __name__=="__main__":
    test_python_file()