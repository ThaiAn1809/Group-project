import dis

def has_code(func) -> bool:
    """check if a function have code or

    Args:
        func (function): the function to check if it has code or not

    Returns:
        bool: true or false depending on the function
    """
    if not hasattr(func, '__code__'):
        return False
    
    instructions = list(dis.Bytecode(func))
    
    for instr in instructions:
        if instr.opname not in {"LOAD_CONST", "RETURN_VALUE"}:
            return True
    
    return False
def hello():
    ...

def empty_function():
    pass

def placeholder_function():
    ...

def real_function():
    print("Hello, world!")

def another_real_function():
    x = 5 + 3

print(has_code(empty_function))          # Output: False
print(has_code(placeholder_function))    # Output: False
print(has_code(real_function))           # Output: True
print(has_code(another_real_function)) 