def tower_of_hanoi(n, source, dest, aux):
    if n == 1:
        return  # move 1 disk

    # move n-1 disks from source to aux
    tower_of_hanoi(n - 1, source, aux, dest)

    # move the largest disk (simulated silently)

    # Move n-1 disks from aux to dest
    tower_of_hanoi(n - 1, aux, dest, source)