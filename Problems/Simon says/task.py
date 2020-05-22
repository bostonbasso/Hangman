def what_to_do(instructions):
    instructions = instructions.strip()
    if instructions.startswith('Simon says'):
        return 'I {0}'.format(instructions[11:].strip())
    elif instructions.endswith('Simon says'):
        return 'I {0}'.format(instructions[:instructions.index('Simon says')])
    else:
        return "I won't do it!"
