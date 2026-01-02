from src.linalg.input import Input

def main():
    print("Create Vector v1")
    input_data = Input()
    v1 = input_data.read_vector("v1")

    print("\nCreate Vector v2")
    v2 = input_data.read_vector("v2")

    print("\nVector v1:", v1.components)
    print("Vector v2:", v2.components)

    try:
        v3 = v1.add(v2)
        print("\nv1 + v2 =", v3.components)
    except ValueError as e:
        print("Error:", e)

    scalar = float(input("\nEnter scalar value: "))
    v4 = v1.scalar_multiply(scalar)
    print(f"{scalar} * v1 =", v4.components)

    print("\nMagnitude of v1:", v1.magnitude())
    print("Unit vector of v1:", v1.unit_vector().components)


if __name__ == "__main__":
    main()
