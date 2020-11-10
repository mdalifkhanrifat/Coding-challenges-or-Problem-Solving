def digital_root(n):
    if n<10:
        return n
    sum = 0
    for digit in str(n):
        sum += int(digit)
        n=sum
    return digital_root(n)
