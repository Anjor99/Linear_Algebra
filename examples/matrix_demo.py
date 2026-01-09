from src.linalg.input import Input
from src.linalg.matrix import Matrix

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
        
    def transposeM1():
        print("\nTranspose of Matrix M1:")
        m1.transpose().show()
        
    def transposeM2():
        print("\nTranspose of Matrix M2:")
        m2.transpose().show()

    def exit_program():
        print("Exiting program.")
        exit()

    def inverseM1():
        print("\nInverse of Matrix M1:")
        m1.inverse().show()

    def inverseM2():
        print("\nInverse of Matrix M2:")
        m2.inverse().show()
        
    def detM1():
        print("\nDeterminant of Matrix M1:")
        print(m1.det())
        
    def detM2():
        print("\nDeterminant of Matrix M2:")
        print(m2.det())
        
    def generate_identity():
        size = int(input("Enter size for identity matrix: "))
        print(f"\nIdentity Matrix of size {size}:")
        Matrix.generate_identity(size).show()

    actions = {
        "1": add,
        "2": mul_ab,
        "3": mul_ba,
        "4": show_mat,
        "5": change_matrices,
        "6": transposeM1,
        "7": transposeM2,
        "8": inverseM1,
        "9": inverseM2,
        "10": generate_identity,
        "11": detM1,
        "12": detM2,
        "13": exit_program
    }

    while True:
        print("\nChoose an operation:")
        print("1. Add matrices (M1 + M2)")
        print("2. Multiply matrices (M1 × M2)")
        print("3. Multiply matrices (M2 × M1)")
        print("4. Show matrices")
        print("5. Change matrices")
        print("6. Transpose M1")
        print("7. Transpose M2")
        print("8. Inverse of M1")
        print("9. Inverse of M2")
        print("10. Generate identity matrix")
        print("11. Determinant of M1")
        print("12. Determinant of M2")
        print("13. Exit")

        choice = input("Enter your choice (1-13): ")

        try:
            actions[choice]()

        except ValueError as e:
            print("Operation failed:", e)
            print("Try a different operation.")

if __name__ == "__main__":
    main()
