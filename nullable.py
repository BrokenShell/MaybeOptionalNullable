def divide(a: float, b: float) -> float:
    if b is None:
        raise ValueError("Denominator cannot be None")
    return a / b


result = divide(10, 2)  # 5.0
# result = divide(10, None)  # Raises ValueError
