"""Problem 15 -- Lattice Paths."""
import numpy


if __name__ == '__main__':
    n = 21
    n_path_array = numpy.zeros((n, n), dtype=numpy.int64)
    n_path_array[n-1, n-1] = 1
    to_process = [(n-1, n-2), (n-2, n-1)]

    while to_process:
        i, j = to_process.pop(0)
        if n_path_array[i, j]:
            continue
        path_count = 0
        if i < n-1:
            path_count += n_path_array[i+1, j]
        if j < n-1:
            path_count += n_path_array[i, j+1]

        n_path_array[i, j] = path_count

        if i > 0:
            to_process.append((i-1, j))
        if j > 0:
            to_process.append((i, j-1))

    print(n_path_array[0, 0])
