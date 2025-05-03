"""
Python高数求解器 - Streamlit界面

此应用程序提供了一个用户友好的界面，用于使用SymPy进行符号数学运算。
"""

import streamlit as st
import sympy as sp
from sympy import symbols, Symbol, sympify
import matplotlib.pyplot as plt
import numpy as np
import io
from symbolic_math import (
    calculate_derivative, calculate_integral, solve_equation,
    calculate_limit, calculate_series_expansion, plot_expression
)

# 设置页面配置
st.set_page_config(
    page_title="Python高数求解器",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Add custom CSS
st.markdown("""
<style>
    .katex-html {
        text-align: center;
    }
    .stApp {
        max-width: 1200px;
        margin: 0 auto;
    }
    h1, h2, h3 {
        text-align: center;
    }
    .operation-section {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
</style>
""", unsafe_allow_html=True)

# 标题和介绍
st.title("Python高数求解器")
st.markdown("""
此应用程序允许您执行各种符号数学运算：
- 求导
- 积分
- 解方程
- 极限
- 级数展开
- 函数绘图

使用标准符号输入您的数学表达式。
""")

# 侧边栏操作选择
st.sidebar.title("运算")
operation = st.sidebar.radio(
    "选择运算",
    ["求导", "积分", "解方程", "极限", "级数展开", "函数绘图"]
)

# 常用变量
common_symbols = ["x", "y", "z", "t"]
custom_symbol = st.sidebar.text_input("自定义符号（如需）", "")
if custom_symbol and custom_symbol not in common_symbols:
    symbol_options = common_symbols + [custom_symbol]
else:
    symbol_options = common_symbols

# Function to display mathematical expressions
def display_math(expr_str):
    try:
        expr = sympify(expr_str)
        st.latex(expr)
    except:
        st.write(expr_str)

# Function to display a list of mathematical expressions
def display_math_list(expr_list):
    for i, expr_str in enumerate(expr_list):
        try:
            expr = sympify(expr_str)
            st.latex(expr)
        except:
            st.write(expr_str)

# 根据选择的操作显示主要内容
if operation == "求导":
    st.header("求导计算器")
    st.markdown("计算函数的导数。")

    col1, col2 = st.columns(2)

    with col1:
        expr = st.text_input("输入函数:", "x^2 + sin(x)")
        symbol = st.selectbox("对变量求导:", symbol_options)

    with col2:
        order = st.number_input("导数阶数:", min_value=1, max_value=10, value=1)

    if st.button("计算导数"):
        result = calculate_derivative(expr, symbol, order)

        st.subheader("结果:")
        st.markdown(f"函数的{order}阶导数:")
        display_math(expr)
        st.markdown(f"关于变量 {symbol} 的导数是:")
        display_math(result)

elif operation == "积分":
    st.header("积分计算器")
    st.markdown("计算函数的积分。")

    col1, col2 = st.columns(2)

    with col1:
        expr = st.text_input("输入函数:", "x^2 + sin(x)")
        symbol = st.selectbox("对变量积分:", symbol_options)

    with col2:
        integral_type = st.radio("积分类型:", ["不定积分", "定积分"])

        if integral_type == "定积分":
            lower_bound = st.text_input("下限:", "0")
            upper_bound = st.text_input("上限:", "1")
        else:
            lower_bound = None
            upper_bound = None

    if st.button("计算积分"):
        if integral_type == "定积分":
            try:
                lower = float(sympify(lower_bound))
                upper = float(sympify(upper_bound))
                result = calculate_integral(expr, symbol, lower, upper)
            except:
                result = "错误: 无效的积分上下限"
        else:
            result = calculate_integral(expr, symbol)

        st.subheader("结果:")
        if integral_type == "不定积分":
            st.markdown("函数的不定积分:")
        else:
            st.markdown(f"函数在 {lower_bound} 到 {upper_bound} 的定积分:")

        display_math(expr)
        st.markdown(f"关于变量 {symbol} 的积分是:")
        display_math(result)

elif operation == "解方程":
    st.header("方程求解器")
    st.markdown("求解特定变量的方程。")

    equation = st.text_input("输入方程 (例如, 'x^2 - 4 = 0' 或 'x^2 - 4'):", "x^2 - 4 = 0")
    symbol = st.selectbox("求解变量:", symbol_options)

    if st.button("求解方程"):
        solutions = solve_equation(equation, symbol)

        st.subheader("结果:")
        st.markdown("方程的解:")
        display_math(equation)
        st.markdown(f"关于变量 {symbol} 的解为:")

        if solutions:
            display_math_list(solutions)
        else:
            st.write("未找到解")

elif operation == "极限":
    st.header("极限计算器")
    st.markdown("计算函数的极限。")

    col1, col2 = st.columns(2)

    with col1:
        expr = st.text_input("输入函数:", "sin(x)/x")
        symbol = st.selectbox("关于变量:", symbol_options)

    with col2:
        approach_value = st.text_input("趋近值:", "0")
        direction = st.radio("方向:", ["双侧", "右侧 (+)", "左侧 (-)"])

        dir_map = {
            "双侧": None,
            "右侧 (+)": "+",
            "左侧 (-)": "-"
        }
        direction_param = dir_map[direction]

    if st.button("计算极限"):
        result = calculate_limit(expr, symbol, approach_value, direction_param)

        st.subheader("结果:")
        st.markdown(f"函数的极限:")
        display_math(expr)

        approach_text = f"当 {symbol} 趋近于 {approach_value}"
        if direction != "双侧":
            approach_text += f" {direction}"

        st.markdown(approach_text + " 时的极限是:")
        display_math(result)

elif operation == "级数展开":
    st.header("级数展开")
    st.markdown("计算函数的级数展开。")

    col1, col2 = st.columns(2)

    with col1:
        expr = st.text_input("输入函数:", "exp(x)")
        symbol = st.selectbox("关于变量:", symbol_options)

    with col2:
        around_point = st.text_input("展开点:", "0")
        num_terms = st.number_input("项数:", min_value=1, max_value=20, value=5)

    if st.button("计算级数"):
        result = calculate_series_expansion(expr, symbol, float(around_point), int(num_terms))

        st.subheader("结果:")
        st.markdown(f"函数的级数展开:")
        display_math(expr)
        st.markdown(f"在 {symbol} = {around_point} 处展开 {num_terms} 项的结果是:")
        display_math(result)

elif operation == "函数绘图":
    st.header("函数绘图器")
    st.markdown("绘制数学函数图像。")

    col1, col2 = st.columns(2)

    with col1:
        expr = st.text_input("输入函数:", "sin(x)")
        symbol = st.selectbox("关于变量:", symbol_options)

    with col2:
        x_min = st.number_input("X 最小值:", value=-10.0)
        x_max = st.number_input("X 最大值:", value=10.0)

        if x_min >= x_max:
            st.error("X 最小值必须小于 X 最大值")

    if st.button("绘制函数") and x_min < x_max:
        try:
            fig, ax = plot_expression(expr, symbol, (x_min, x_max))
            st.pyplot(fig)
        except Exception as e:
            st.error(f"绘制函数出错: {str(e)}")

# 页脚
st.markdown("---")
st.markdown("Python高数求解器 - 由 SymPy 和 Streamlit 提供支持")
