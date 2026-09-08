def add(a, b):
    return a + b


def application():
    print("================================")
    print("       PYTHON CI/CD DEMO")
    print("================================")

    result = add(10, 20)

    print("10 + 20 =", result)
    print("Application executed successfully!")


if __name__ == "__main__":
    application()