# 🔢 Matrix Operations Tool

A simple interactive Python application using NumPy to perform basic matrix operations.

## ✨ Features

- ➕ Matrix Addition
- ➖ Matrix Subtraction
- ✖️ Matrix Multiplication
- 🔁 Transpose of a Matrix
- 🧮 Determinant Calculation
- 🧑‍💻 Interactive CLI interface

## 🧰 Technologies Used

- **Python 3**
- **NumPy**

## 🖥️ How to Run

1. Clone this repository:

```bash
git clone https://github.com/your-username/matrix-tool.git
cd matrix-tool
```

2. Install dependencies:

```bash
pip install numpy
```

3. Run the program:

```bash
python matrix_tool.py
```

## 📂 Project Structure

```
matrix-tool/
├── matrix_tool.py         # Main Python script
├── Python_July.pdf        # Supporting documentation or notes
├── README.md              # Project documentation
└── .gitignore             # Ignored files (e.g., __pycache__)
```

## 📄 Sample Output

```
🔢 Matrix Operations
1. Add
2. Subtract
3. Multiply
4. Transpose
5. Determinant
6. Exit
Choose an option: 1

Enter size of Matrix A (rows cols): 2 2
Enter 2 rows (space-separated values):
1 2
3 4

Enter size of Matrix B (rows cols): 2 2
Enter 2 rows (space-separated values):
5 6
7 8

A + B:
[[ 6.  8.]
 [10. 12.]]
```

## 📘 Notes

- The program handles input validation and matrix shape mismatches.
- Determinant is only computed for square matrices.

## 📬 Contact

Created by [Your Name] – feel free to reach out via GitHub or email for suggestions or improvements.