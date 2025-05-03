# Python 高级数学求解器

[English](README.md) | [中文](README_zh.md)

一个使用 Python、SymPy 和 Streamlit 构建的强大符号数学求解器。

## 功能特点

- **符号计算**：使用 SymPy 进行符号数学运算
- **用户友好界面**：易于使用的 Streamlit 网页界面
- **多种运算**：
  - 导数计算
  - 积分计算（定积分和不定积分）
  - 方程求解
  - 极限计算
  - 级数展开
  - 函数绘图

## 安装

1. 克隆此仓库：
   ```
   git clone https://github.com/zym9863/python-advanced-math-solver.git
   cd python-advanced-math-solver
   ```

2. 创建并激活虚拟环境：
   ```
   python -m venv venv
   
   # Windows 系统
   .\venv\Scripts\activate
   
   # macOS/Linux 系统
   source venv/bin/activate
   ```

3. 安装所需的包：
   ```
   pip install -r requirements.txt
   ```

## 使用方法

1. 启动 Streamlit 应用程序：
   ```
   streamlit run app.py
   ```

2. 打开您的网络浏览器并导航到终端中显示的 URL（通常是 http://localhost:8501）

3. 使用侧边栏选择您想要执行的数学运算

4. 输入您的数学表达式和参数，然后点击相应的按钮计算结果

## 输入格式

- 使用标准数学符号表示表达式
- 可用函数：sin、cos、tan、exp、log、sqrt 等
- 使用 ^ 或 ** 表示幂运算（例如，x^2 或 x**2）
- 对于方程，您可以使用 "x^2 - 4 = 0" 格式或简单地使用 "x^2 - 4"（假定等于零）

## 示例

- 导数：`x^2 + sin(x)`
- 积分：`x^2 + sin(x)`
- 方程：`x^2 - 4 = 0`
- 极限：`sin(x)/x` 当 x 趋近于 0
- 级数：`exp(x)` 在 x = 0 附近展开
- 绘图：`sin(x)` 从 x = -10 到 x = 10

## 许可证

MIT 许可证

## 致谢

- [SymPy](https://www.sympy.org/) - Python 符号数学库
- [Streamlit](https://streamlit.io/) - 创建 Web 应用程序的框架
- [Matplotlib](https://matplotlib.org/) - Python 绘图库
- [NumPy](https://numpy.org/) - Python 数值计算库
