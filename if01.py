def main(a,b,c):
    """
    Find the largest of the numbers.
    Args:
        a: First number.
        b: Second number.
        c: Third number.
    Returns:
        int: return answer.
    """
    if a>b:
        return a
    if b>c:
        return b
    if c>a:
        return c
print(main(1,4,2))