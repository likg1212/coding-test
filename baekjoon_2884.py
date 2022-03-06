h, m = input().split()
h = int(h)
m = int(m)

nm = m - 45

if nm < 0:
    h = h - 1
    m = 60 + nm
    
    if h < 0:
        h = 24-1
else:
    m = nm
print(h, m)
