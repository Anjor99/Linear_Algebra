from src.linalg.input import Input

def main():
    input_data = Input()

    # Read matrices once
    m1 = input_data.read_matrix("M1")
    m2 = input_data.read_matrix("M2")

    def add():
        print("\nResult of M1 + M2:")
        result = m1.add(m2)
        result.show()

    def mul_ab():
        print("\nResult of M1 x M2:")
        result = m1.multiply(m2)
        result.show()
        
    def mul_ba():
        print("\nResult of M2 x M1:")
        result = m2.multiply(m1)
        result.show()

    def show_mat():
        print("\nCurrent Matrices:")
        print("\nMatrix M1:")
        m1.show()
        print("\nMatrix M2:")
        m2.show()
        
    def change_matrices():
        print("\nChanging matrices...")
        nonlocal m1, m2
        m1 = input_data.read_matrix("M1")
        m2 = input_data.read_matrix("M2")

    def exit_program():
        print("Exiting program.")
        exit()

    actions = {
        "1": add,
        "2": mul_ab,
        "3": mul_ba,
        "4": show_mat,
        "5": change_matrices,
        "6": exit_program
    }

    while True:
        print("\nChoose an operation:")
        print("1. Add matrices (M1 + M2)")
        print("2. Multiply matrices (M1 × M2)")
        print("3. Multiply matrices (M2 × M1)")
        print("4. Show matrices")
        print("5. Change matrices")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        try:
            actions[choice]()

        except ValueError as e:
            print("Operation failed:", e)
            print("Try a different operation.")

if __name__ == "__main__":
    main()
