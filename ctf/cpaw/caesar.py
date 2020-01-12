def caesar(target, shift_num):
    decrypted = []
    for i in target:
        if i.isalpha():
            decrypted.append(chr(ord(i) - shift_num))
        else:
            decrypted.append(i)
    return "".join(decrypted)


if __name__ == "__main__":
    print(caesar("fsdz{Fdhvdu_flskhu_lv_fodvvlfdo_flskhu}", 3))
