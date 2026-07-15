print(bool(0))
print(bool('a'))
print(bool(None))
print(bool([]))
print(bool(()))
print(bool({}))

print(0 or print(88) or 888)
print(0 or 999 or print(99))

x=True and 9  # 9
y=False or True or 8 # True 1
z = x * 3 + y * 2 # 9 * 3 + 1 * 2
print(z)  # 29