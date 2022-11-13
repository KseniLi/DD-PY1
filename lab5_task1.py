from pprint import pprint
d = [{"dec": i, "bin": bin(i), "oct": oct(i), "hex": hex(i)} for i in range(16)]
pprint(d)