from src.linalg.input import Input

def main():
    try:
        input_data = Input()
        m1 = input_data.read_matrix("M1")
        m2 = input_data.read_matrix("M2")
        m3 = m1.add(m2)
        m1.show()
        print("+")
        m2.show()
        print("=")
        m3.show()
    except ValueError as e:
        print("Error: ",e)


if __name__ == "__main__":
    main()
