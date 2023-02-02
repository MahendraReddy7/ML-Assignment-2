def uplow(string):
    ul={"u_case":0, "l_case":0}
    for i in string:
        if i.isupper():
            ul["u_case"]+=1
        elif i.islower():
            ul["l_case"]+=1
        else:
            pass
    print("Input String : ", string)
    print("No. of Upper-case characters:", ul["u_case"])
    print("No. of lower-case characters:", ul["l_case"])

uplow("The quick Brow Fox")