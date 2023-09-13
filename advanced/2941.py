alpha_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
string = input()

for i in alpha_list:
    string = string.replace(i, "_")

print(len(string))
