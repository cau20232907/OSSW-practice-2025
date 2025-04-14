import tkinter as tk
from tkinter import messagebox

def calculate():
    """입력값을 가져와 계산하고 결과를 출력"""
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        operator = operator_var.get()

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                raise ZeroDivisionError
            result = num1 / num2
        else:
            messagebox.showerror("오류", "잘못된 연산 기호입니다.")
            return

        result_label.config(text=f"결과: {result}")
    except ValueError:
        messagebox.showerror("오류", "숫자를 올바르게 입력해주세요.")
    except ZeroDivisionError:
        messagebox.showerror("오류", "0으로 나눌 수 없습니다.")

# GUI 생성
root = tk.Tk()
root.title("사칙연산 계산기")

# 연산 기호 버튼 생성
def set_operator(op):
    operator_var.set(op)

button_frame = tk.Frame(root)
button_frame.grid(row=1, column=1, padx=10, pady=10)

plus_button = tk.Button(button_frame, text="+", command=lambda: set_operator('+'), width=5)
plus_button.grid(row=0, column=0, padx=2, pady=2)

minus_button = tk.Button(button_frame, text="-", command=lambda: set_operator('-'), width=5)
minus_button.grid(row=0, column=1, padx=2, pady=2)

multiply_button = tk.Button(button_frame, text="*", command=lambda: set_operator('*'), width=5)
multiply_button.grid(row=0, column=2, padx=2, pady=2)

divide_button = tk.Button(button_frame, text="/", command=lambda: set_operator('/'), width=5)
divide_button.grid(row=0, column=3, padx=2, pady=2)

# GUI 생성
root = tk.Tk()
root.title("사칙연산 계산기")

# 첫 번째 숫자 입력
tk.Label(root, text="첫 번째 숫자:").grid(row=0, column=0, padx=10, pady=10)
entry1 = tk.Entry(root)
entry1.grid(row=0, column=1, padx=10, pady=10)

# 연산 기호 선택
tk.Label(root, text="연산 기호:").grid(row=1, column=0, padx=10, pady=10)
operator_var = tk.StringVar(value='+')
operator_menu = tk.OptionMenu(root, operator_var, '+', '-', '*', '/')
operator_menu.grid(row=1, column=1, padx=10, pady=10)

# 두 번째 숫자 입력
tk.Label(root, text="두 번째 숫자:").grid(row=2, column=0, padx=10, pady=10)
entry2 = tk.Entry(root)
entry2.grid(row=2, column=1, padx=10, pady=10)

# 계산 버튼
calculate_button = tk.Button(root, text="계산", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

# 결과 출력
result_label = tk.Label(root, text="결과: ")
result_label.grid(row=4, column=0, columnspan=2, pady=10)

# GUI 실행
root.mainloop()