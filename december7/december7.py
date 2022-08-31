def main(start_x, end_x, start_y, end_y, point, current_order, O):
    length = (end_x - start_x) // 3
    assert (end_y - start_y) // 3 == length

    if current_order == O:
        return "b"

    if length == 0:
        return "b"

    x, y = point

    condition_x0 = start_x <= x < start_x + length
    condition_x1 = start_x + length <= x < start_x + 2 * length
    condition_x2 = start_x + 2 * length <= x < start_x + 3 * length

    condition_y0 = start_y <= y < start_y + length
    condition_y1 = start_y + length <= y < start_y + 2 * length
    condition_y2 = start_y + 2 * length <= y < start_y + 3 * length

    if condition_x0 and condition_y0:
        return main(
            start_x,
            start_x + length,
            start_y,
            start_y + length,
            point,
            current_order + 1,
            O,
        )
    elif condition_x1 and condition_y0:
        return main(
            start_x + length,
            start_x + 2 * length,
            start_y,
            start_y + length,
            point,
            current_order + 1,
            O,
        )
    elif condition_x2 and condition_y0:
        return main(
            start_x + 2 * length,
            start_x + 3 * length,
            start_y,
            start_y + length,
            point,
            current_order + 1,
            O,
        )

    elif condition_x0 and condition_y1:
        return main(
            start_x,
            start_x + length,
            start_y + length,
            start_y + 2 * length,
            point,
            current_order + 1,
            O,
        )

    elif condition_x1 and condition_y1:
        return "w"

    elif condition_x2 and condition_y1:
        return main(
            start_x + 2 * length,
            start_x + 3 * length,
            start_y + length,
            start_y + 2 * length,
            point,
            current_order + 1,
            O,
        )
    elif condition_x0 and condition_y2:
        return main(
            start_x,
            start_x + length,
            start_y + 2 * length,
            start_y + 3 * length,
            point,
            current_order + 1,
            O,
        )

    elif condition_x1 and condition_y2:
        return main(
            start_x + length,
            start_x + 2 * length,
            start_y + 2 * length,
            start_y + 3 * length,
            point,
            current_order + 1,
            O,
        )

    elif condition_x2 and condition_y2:
        return main(
            start_x + 2 * length,
            start_x + 3 * length,
            start_y + 2 * length,
            start_y + 3 * length,
            point,
            current_order + 1,
            O,
        )


if __name__ == "__main__":
    D, O, N = map(int, input().strip().split(" "))
    colors = []
    for _ in range(N):
        point = list(map(int, input().strip().split(" ")))
        colors.append(main(0, 3 ** D, 0, 3 ** D, point, 0, O))
    print(" ".join(colors))
