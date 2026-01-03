# Linear Algebra

Implementing vectors, matrices, and other linear algebra concepts in pure Python to deeply understand the math behind AI/ML.

## Features

Currently implemented:

### Vectors
- Vector addition (`add`)
- Scalar multiplication (`scalar_multiply`)
- Magnitude calculation (`magnitude`)
- Unit vector computation (`unit_vector`)
- Dot product (`dot`)
- Angle between vectors (`angle_btn_vectors`)
- Cosine similarity (`cos_similarity`)

---

## Usage

### Vector Demo
Run the vector demo script to interactively test vector operations:

```bash
python3 -m examples.vector_demo
```

## Project Structure
### Key Files
- `src/linalg/vector.py`: Implementation of the `Vector` class and its operations.
- `src/linalg/input.py`: Utility functions for handling user input.
- `examples/vector_demo.py`: Example script demonstrating vector operations.

### Directory Structure
```bash
Linear_Algebra/
├─ src/
│  └─ linalg/
│     ├─ __init__.py
│     ├─ vector.py
│     └─ input.py
├─ examples/
│  └─ vector_demo.py
├─ README.md
└─ .gitignore
```
