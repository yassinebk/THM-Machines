for x in range(1, 256):
    if "{:02x}".format(x) not in ['07', '2e','a0' ]:
        print("\\x" + "{:02x}".format(x), end='')
print()
