def soma(*num):
    tot = 0
    for c in num:
        tot += c
    return tot


def multiplica(*num):
    tot = 1
    for c in num:
        tot *= c
    return tot


def subtrai(*num):
    tot = 0
    for c in num:
        tot -= c
    return tot