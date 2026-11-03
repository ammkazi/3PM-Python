def total(*num):
    print(f"{type(num), num}")
    return sum(num)


# def avg(*)
total_num = total(1,43,23,54,124,23,423,451,43,2343,1232,12)
print(total_num)
print(total())

marks = [90,78,56]
print(total(*marks))


