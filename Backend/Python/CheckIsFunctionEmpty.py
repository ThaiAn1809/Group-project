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