rr = open("data.txt", "r")

def divide(st, d):
    li = []
    st += d
    while len(st) > 0:
        n = st.index(d)
        we = st[:n]
        if we != "":
            li.append(we)
        st = st[n+len(d):]
    return li

rw = str(rr.read())

def convertfloat(li):
    ll = []
    for k in li:
        ll.append(float(k))
    return ll

li = divide(rw, "\n")
print(convertfloat(li))

