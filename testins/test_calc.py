import calc

def test_add():
    if calc.add(1, 2) == 3:
        print(f"test for add, True")
    else:
        print(f"test for add, False {calc.add(1, 2)}")

def test_sub():
    if calc.sub(5, 2) == 3:
        print(f"test for sub, True")
    else:
        print(f"test for sub, False {calc.sub(5, 2)}")

def test_mul():
    if calc.mul(5, 2) == 10:
        print(f"test for mul, True")
    else:
        print(f"test for mul, False {calc.mul(5, 2)}")

def test_div():
    if calc.div(10, 2) == 5:
        print(f"test for div, True {calc.div(10, 2)}")
    else:
        print(f"test for div, False {calc.div(10, 2)}")


if __name__ == "__main__":
    test_add()
    test_div()
    test_mul()
    test_div()
