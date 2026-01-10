from src.linalg.input import Input
from src.linalg.matrix import Matrix
from src.linalg.vector import Vector


def main():
    input_data = Input()

    # -------------------------
    # Matrix Initialization
    # -------------------------
    m1 = input_data.read_matrix("M1")
    m2 = input_data.read_matrix("M2")

    # -------------------------
    # Helper display functions
    # -------------------------
    def show_matrix(name, matrix):
        print(f"\nMatrix {name}:")
        matrix.show()

    def show_result(title, matrix):
        print(f"\n{title}")
        matrix.show()

    # -------------------------
    # Basic Operations
    # -------------------------
    def add_matrices():
        show_result("Result of M1 + M2:", m1.add(m2))

    def multiply_m1_m2():
        show_result("Result of M1 × M2:", m1.multiply(m2))

    def multiply_m2_m1():
        show_result("Result of M2 × M1:", m2.multiply(m1))

    def show_matrices():
        show_matrix("M1", m1)
        show_matrix("M2", m2)

    def change_matrices():
        nonlocal m1, m2
        print("\nRe-enter matrices:")
        m1 = input_data.read_matrix("M1")
        m2 = input_data.read_matrix("M2")

    # -------------------------
    # Matrix Properties
    # -------------------------
    def transpose_m1():
        show_result("Transpose of M1:", m1.transpose())

    def transpose_m2():
        show_result("Transpose of M2:", m2.transpose())

    def inverse_m1():
        show_result("Inverse of M1:", m1.inverse())

    def inverse_m2():
        show_result("Inverse of M2:", m2.inverse())

    def det_m1():
        print("\nDeterminant of M1:", m1.det())

    def det_m2():
        print("\nDeterminant of M2:", m2.det())

    def generate_identity():
        size = int(input("Enter size for identity matrix: "))
        show_result(f"Identity Matrix ({size}×{size}):",
                    Matrix.generate_identity(size))

    # -------------------------
    # Eigenvalue & Eigenvector Demo (NEW)
    # -------------------------
    def eigen_demo_m1():
        print("\nEigen Analysis for M1 (2×2 only):")

        eigs = m1.eigenvalues_2x2()
        if eigs is None:
            print("No real eigenvalues (likely a rotation matrix).")
            return

        for lam in eigs:
            v = m1.eigenvector_2x2(lam)
            is_valid = m1.is_eigenvector(v, lam)

            print(f"\nEigenvalue λ = {lam}")
            print(f"Eigenvector v = {v.components}")
            print(f"Verification Ax ≈ λx : {is_valid}")

    # -------------------------
    # Exit
    # -------------------------
    def exit_program():
        print("Exiting program.")
        exit()

    # -------------------------
    # Menu Actions
    # -------------------------
    actions = {
        "1": add_matrices,
        "2": multiply_m1_m2,
        "3": multiply_m2_m1,
        "4": show_matrices,
        "5": change_matrices,
        "6": transpose_m1,
        "7": transpose_m2,
        "8": inverse_m1,
        "9": inverse_m2,
        "10": generate_identity,
        "11": det_m1,
        "12": det_m2,
        "13": eigen_demo_m1,
        "14": exit_program,
    }

    # -------------------------
    # Main Loop
    # -------------------------
    while True:
        print("\nChoose an operation:")
        print("1.  Add matrices (M1 + M2)")
        print("2.  Multiply matrices (M1 × M2)")
        print("3.  Multiply matrices (M2 × M1)")
        print("4.  Show matrices")
        print("5.  Change matrices")
        print("6.  Transpose M1")
        print("7.  Transpose M2")
        print("8.  Inverse of M1")
        print("9.  Inverse of M2")
        print("10. Generate identity matrix")
        print("11. Determinant of M1")
        print("12. Determinant of M2")
        print("13. Eigenvalues & Eigenvectors of M1 (2×2)")
        print("14. Exit")

        choice = input("Enter your choice (1-14): ")

        try:
            actions[choice]()
        except KeyError:
            print("Invalid choice. Please select a valid option.")
        except ValueError as e:
            print("Operation failed:", e)


if __name__ == "__main__":
    main()
