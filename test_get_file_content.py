from config import MAX_CHARS
from functions.get_file_content import get_file_content

def test_content():
    
    lorem_result = get_file_content("calculator", "lorem.txt")
    
    # print("DEBUG len:", len(lorem_result))
    # print("DEBUG tail:", lorem_result[-120:])
    assert lorem_result.endswith(
    f'[...File "lorem.txt" truncated at {MAX_CHARS} characters]'
    )
    assert len(lorem_result) > MAX_CHARS


    result = get_file_content("calculator","main.py")
    print("Result of main file")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/calculator.py")
    print("Result of 'pkg/calculator' file")
    print(result)
    print("")

    result = get_file_content("calculator", "/bin/cat")
    print("Result for '/bin' directory")
    print(result)
    print("")

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    print("Result for pkg directory")
    print(result)
    print("")


if __name__ == "__main__":
    test_content()