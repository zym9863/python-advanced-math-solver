# Python Advanced Math Solver

[English](README.md) | [中文](README_zh.md)

A powerful symbolic mathematics solver built with Python, SymPy, and Streamlit.

## Features

- **Symbolic Computation**: Perform symbolic mathematical operations using SymPy
- **User-Friendly Interface**: Easy-to-use Streamlit web interface
- **Multiple Operations**:
  - Derivatives
  - Integrals (definite and indefinite)
  - Equation Solving
  - Limits
  - Series Expansions
  - Function Plotting

## Installation

1. Clone this repository:
   ```
   git clone https://github.com/zym9863/python-advanced-math-solver.git
   cd python-advanced-math-solver
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv

   # On Windows
   .\venv\Scripts\activate

   # On macOS/Linux
   source venv/bin/activate
   ```

3. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Start the Streamlit application:
   ```
   streamlit run app.py
   ```

2. Open your web browser and navigate to the URL displayed in the terminal (usually http://localhost:8501)

3. Use the sidebar to select the mathematical operation you want to perform

4. Enter your mathematical expression and parameters, then click the corresponding button to calculate the result

## Input Format

- Use standard mathematical notation for expressions
- Available functions: sin, cos, tan, exp, log, sqrt, etc.
- Use ^ or ** for exponentiation (e.g., x^2 or x**2)
- For equations, you can use the format "x^2 - 4 = 0" or simply "x^2 - 4" (which is assumed to equal zero)

## Examples

- Derivative: `x^2 + sin(x)`
- Integral: `x^2 + sin(x)`
- Equation: `x^2 - 4 = 0`
- Limit: `sin(x)/x` as x approaches 0
- Series: `exp(x)` around x = 0
- Plot: `sin(x)` from x = -10 to x = 10

## License

MIT License

## Acknowledgments

- [SymPy](https://www.sympy.org/) - Python library for symbolic mathematics
- [Streamlit](https://streamlit.io/) - Framework for creating web applications
- [Matplotlib](https://matplotlib.org/) - Plotting library for Python
- [NumPy](https://numpy.org/) - Numerical computing library for Python
