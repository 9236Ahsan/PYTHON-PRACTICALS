import numpy as np
y=np.array(['we','are','here','for','learning'],dtype=np.str)
en=np.char.encode(y,'cp500')
de=np.char.decode(en,'cp500')
print("after encoding the array\n")
print(en)
print("after decoding the encoded array")
print(de)