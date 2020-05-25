def generate_numbers(n, m, prefix=None):
    prefix = prefix or []
    if m == 0:
        print(prefix)
        return

    for d in range(n):
        prefix.append(d)
        generate_numbers(n, m - 1, prefix)
        prefix.pop()


# Generate all permutation for N digits by length M
generate_numbers(3, 3)
