if __name__ == '__main__':
    flag = "flag{hacking_for_fun}"
    new = []
    for i in range(len(flag)):
        if 105 == ord(flag[i]) or ord(flag[i]) == 114:
            new.append(chr(49))
        else:
            new.append(flag[i])
    for k in new:
        print(k, end="")
