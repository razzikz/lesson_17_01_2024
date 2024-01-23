def find(s):
    length = len(s)
    if length > 140:
        return "Big length str"
    for elem in range(1, length):
        num = int(s[:elem])
        str_num = str(num)
        if 0 < int(str_num) < 1000000000:
            pass
        else:
            return "small num"
        while len(str_num) < length:
            num += 1
            str_num += str(num)
        if str_num == s:
            return int(s[:elem])
    return int(s)


print(find("123456789101112131415"))
print(find("72637236"))
print(find("1112"))