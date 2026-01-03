from src.linalg.input import Input

def main():
    try:
        print("Create Vector v1")
        input_data = Input()
        v1 = input_data.read_vector("v1")

        print("\nCreate Vector v2")
        v2 = input_data.read_vector("v2")

        print("\nVector v1:", v1.components)
        print("Vector v2:", v2.components)

    
        v3 = v1.add(v2)
        print("\nv1 + v2 =", v3.components)
        v4 = v1.dot(v2)
        print("\nv1.v2 =", v4)
        angle = v1.angle_btn_vectors(v2)
        print("\nAngle between v1 and v2 (radians):", angle)
        cos_sim = v1.cos_similarity(v2)
        print("\nCosine Similarity between v1 and v2:", cos_sim)

        scalar = float(input("\nEnter scalar value: "))
        v4 = v1.scalar_multiply(scalar)
        print(f"{scalar} * v1 =", v4.components)

        print("\nMagnitude of v1:", v1.magnitude())
        print("Unit vector of v1:", v1.unit_vector().components)
    except ValueError as e:
        print("Error: ",e)


if __name__ == "__main__":
    main()
