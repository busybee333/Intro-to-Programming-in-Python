import Vector

v1 = Vector.Vector(2,7)
print(v1)

v2 = Vector.Vector(1,5)
print(v2)

totalplus = v1 + v2
print(totalplus)

totalminus = v1 - v2
print(totalminus)

totalmult = v1 * v2
print(totalmult)

iseq = v1 == v2
print(iseq)

mag = Vector.Vector.magnitude(v1)
print(mag)

uni = Vector.Vector.unit(v1)
print(uni)

v3 = Vector.Vector(1)
print(v3)

totalplus = v1 + v3
print(totalplus)