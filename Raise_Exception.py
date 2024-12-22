def check_age(age):
    if age < 18:
        raise ValueError("Age must be at least 18.")
    return "Age is valid."

# Example usage
try:
    print(check_age(19))
except ValueError as e:
    print(f"Error: {e}")
