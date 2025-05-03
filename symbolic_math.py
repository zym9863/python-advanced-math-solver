"""
Symbolic Mathematics Module for Advanced Math Solver

This module provides functions for symbolic mathematical operations using SymPy.
"""

import sympy as sp
from sympy import symbols, Symbol, sympify, SympifyError
from sympy import diff, integrate, solve, limit, series
from sympy import sin, cos, tan, exp, log, sqrt
import numpy as np
import matplotlib.pyplot as plt
from typing import Union, List, Dict, Tuple, Any, Optional

# Define common symbols
x, y, z, t = symbols('x y z t')
default_symbol = x

def parse_expression(expr_str: str, symbol_str: str = 'x') -> Tuple[Any, Symbol]:
    """
    Parse a mathematical expression string into a SymPy expression.
    
    Args:
        expr_str: String representation of the mathematical expression
        symbol_str: String representation of the variable symbol (default: 'x')
        
    Returns:
        Tuple of (parsed expression, symbol)
    
    Raises:
        ValueError: If the expression cannot be parsed
    """
    try:
        # Create the symbol
        if symbol_str not in ['x', 'y', 'z', 't']:
            symbol = Symbol(symbol_str)
        else:
            symbol = {'x': x, 'y': y, 'z': z, 't': t}[symbol_str]
        
        # Parse the expression
        expr = sympify(expr_str)
        return expr, symbol
    except SympifyError as e:
        raise ValueError(f"Could not parse expression: {expr_str}. Error: {str(e)}")

def calculate_derivative(expr_str: str, symbol_str: str = 'x', order: int = 1) -> str:
    """
    Calculate the derivative of a mathematical expression.
    
    Args:
        expr_str: String representation of the mathematical expression
        symbol_str: Variable to differentiate with respect to (default: 'x')
        order: Order of the derivative (default: 1)
        
    Returns:
        String representation of the derivative
    """
    try:
        expr, symbol = parse_expression(expr_str, symbol_str)
        result = diff(expr, symbol, order)
        return str(result)
    except Exception as e:
        return f"Error calculating derivative: {str(e)}"

def calculate_integral(expr_str: str, symbol_str: str = 'x', 
                      lower_bound: Optional[float] = None, 
                      upper_bound: Optional[float] = None) -> str:
    """
    Calculate the integral of a mathematical expression.
    
    Args:
        expr_str: String representation of the mathematical expression
        symbol_str: Variable to integrate with respect to (default: 'x')
        lower_bound: Lower bound for definite integral (optional)
        upper_bound: Upper bound for definite integral (optional)
        
    Returns:
        String representation of the integral
    """
    try:
        expr, symbol = parse_expression(expr_str, symbol_str)
        
        if lower_bound is not None and upper_bound is not None:
            # Definite integral
            result = integrate(expr, (symbol, lower_bound, upper_bound))
        else:
            # Indefinite integral
            result = integrate(expr, symbol)
        
        return str(result)
    except Exception as e:
        return f"Error calculating integral: {str(e)}"

def solve_equation(equation_str: str, symbol_str: str = 'x') -> List[str]:
    """
    Solve an equation for the specified variable.
    
    Args:
        equation_str: String representation of the equation (e.g., "x**2 - 4 = 0" or "x**2 - 4")
        symbol_str: Variable to solve for (default: 'x')
        
    Returns:
        List of string representations of the solutions
    """
    try:
        # Check if the equation contains an equals sign
        if '=' in equation_str:
            left_side, right_side = equation_str.split('=', 1)
            left_expr, _ = parse_expression(left_side.strip(), symbol_str)
            right_expr, _ = parse_expression(right_side.strip(), symbol_str)
            equation = left_expr - right_expr
        else:
            # If no equals sign, assume it's set to zero
            equation, _ = parse_expression(equation_str, symbol_str)
        
        # Get the symbol
        if symbol_str not in ['x', 'y', 'z', 't']:
            symbol = Symbol(symbol_str)
        else:
            symbol = {'x': x, 'y': y, 'z': z, 't': t}[symbol_str]
        
        # Solve the equation
        solutions = solve(equation, symbol)
        
        # Convert solutions to strings
        return [str(sol) for sol in solutions]
    except Exception as e:
        return [f"Error solving equation: {str(e)}"]

def calculate_limit(expr_str: str, symbol_str: str = 'x', 
                   approach_value: Union[str, float] = 0, 
                   direction: str = '+') -> str:
    """
    Calculate the limit of an expression.
    
    Args:
        expr_str: String representation of the mathematical expression
        symbol_str: Variable for the limit (default: 'x')
        approach_value: Value that the variable approaches (default: 0)
        direction: Direction of approach ('+' for right, '-' for left, default: '+')
        
    Returns:
        String representation of the limit
    """
    try:
        expr, symbol = parse_expression(expr_str, symbol_str)
        
        # Handle special approach values like infinity
        if approach_value == 'inf' or approach_value == 'infinity':
            approach_value = sp.oo
        elif approach_value == '-inf' or approach_value == '-infinity':
            approach_value = -sp.oo
        
        # Calculate the limit
        if direction == '+':
            result = limit(expr, symbol, approach_value, dir='+')
        elif direction == '-':
            result = limit(expr, symbol, approach_value, dir='-')
        else:
            result = limit(expr, symbol, approach_value)
        
        return str(result)
    except Exception as e:
        return f"Error calculating limit: {str(e)}"

def calculate_series_expansion(expr_str: str, symbol_str: str = 'x', 
                              around_point: float = 0, 
                              num_terms: int = 5) -> str:
    """
    Calculate the series expansion of an expression.
    
    Args:
        expr_str: String representation of the mathematical expression
        symbol_str: Variable for the expansion (default: 'x')
        around_point: Point around which to expand (default: 0)
        num_terms: Number of terms in the expansion (default: 5)
        
    Returns:
        String representation of the series expansion
    """
    try:
        expr, symbol = parse_expression(expr_str, symbol_str)
        result = series(expr, symbol, around_point, num_terms)
        return str(result)
    except Exception as e:
        return f"Error calculating series expansion: {str(e)}"

def plot_expression(expr_str: str, symbol_str: str = 'x', 
                   x_range: Tuple[float, float] = (-10, 10),
                   num_points: int = 1000) -> Tuple[plt.Figure, plt.Axes]:
    """
    Create a plot of the expression.
    
    Args:
        expr_str: String representation of the mathematical expression
        symbol_str: Variable for the plot (default: 'x')
        x_range: Range of x values as (min, max) (default: (-10, 10))
        num_points: Number of points to plot (default: 1000)
        
    Returns:
        Tuple of (figure, axes) for the plot
    """
    try:
        expr, symbol = parse_expression(expr_str, symbol_str)
        
        # Convert symbolic expression to a numpy function
        f = sp.lambdify(symbol, expr, "numpy")
        
        # Generate x values
        x_vals = np.linspace(x_range[0], x_range[1], num_points)
        
        # Calculate y values, handling potential errors
        y_vals = []
        for x_val in x_vals:
            try:
                y_val = float(f(x_val))
                if np.isfinite(y_val):
                    y_vals.append(y_val)
                else:
                    y_vals.append(None)
            except:
                y_vals.append(None)
        
        # Create the plot
        fig, ax = plt.subplots(figsize=(10, 6))
        
        # Plot only valid points
        valid_indices = [i for i, y in enumerate(y_vals) if y is not None]
        valid_x = [x_vals[i] for i in valid_indices]
        valid_y = [y_vals[i] for i in valid_indices]
        
        if valid_x:
            ax.plot(valid_x, valid_y)
        
        # Add grid and labels
        ax.grid(True)
        ax.axhline(y=0, color='k', linestyle='-', alpha=0.3)
        ax.axvline(x=0, color='k', linestyle='-', alpha=0.3)
        ax.set_xlabel(symbol_str)
        ax.set_ylabel(f"{expr_str}")
        ax.set_title(f"Plot of {expr_str}")
        
        return fig, ax
    except Exception as e:
        # Return an error plot
        fig, ax = plt.subplots(figsize=(10, 6))
        ax.text(0.5, 0.5, f"Error plotting expression: {str(e)}", 
                ha='center', va='center', transform=ax.transAxes)
        return fig, ax
