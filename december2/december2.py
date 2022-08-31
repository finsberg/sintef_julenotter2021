def main(X, N):
    """Sort houses for Santa and his team

    Parameters
    ----------
    X : Iterable[int]
        Sequence of houses to ordered
    N : int
        Size of X

    Returns
    -------
    str
        Sequence of houses ordered as Santa requested
    """
    # Handle the N = 1 case separately
    if N == 1:
        return list(X)[0]

    # Sort X
    X = sorted(X)
    # Allocate output array
    Y = [None] * N

    # Handle case if N is odd
    n = 0 if N % 2 == 0 else 1
    # Loop through array and fill in the values
    for i, (x_low, x_high) in enumerate(zip(X[: (N + n) // 2], X[(N + n) // 2 :])):
        Y[N - 2 * i - 1 - n] = x_high
        Y[2 * i] = x_low

    # If N is odd we are missing the middle value of X which
    # should be the last value of Y
    if n:
        Y[-1] = X[(N - 1) // 2]

    return " ".join(map(str, Y))


if __name__ == "__main__":
    N = int(input())
    X = map(int, input().strip().split(" "))
    print(main(X, N))