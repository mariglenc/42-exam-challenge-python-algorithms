# Python Set Operations - quick reference you can run
# Run:  python3 set_operations.py

a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print("a =", a)
print("b =", b)
print()

# & intersection -> items in BOTH
print("a & b :", a & b)          # {3, 4}

# | union -> items in EITHER (duplicates merged)
print("a | b :", a | b)          # {1, 2, 3, 4, 5, 6}

# - difference -> in A but NOT B (order matters!)
print("a - b :", a - b)          # {1, 2}
print("b - a :", b - a)          # {5, 6}

# ^ symmetric difference -> in ONE but not both
print("a ^ b :", a ^ b)          # {1, 2, 5, 6}
print()

# Word-method versions (same results, sometimes clearer)
print("a.intersection(b)        :", a.intersection(b))          # a & b
print("a.union(b)               :", a.union(b))                 # a | b
print("a.difference(b)          :", a.difference(b))            # a - b
print("a.symmetric_difference(b):", a.symmetric_difference(b))  # a ^ b
print()

# True/False tests
print("a.issubset(b)   :", a.issubset(b))     # is every item of a also in b?
print("a.issuperset(b) :", a.issuperset(b))   # does a contain all of b?
print("a.isdisjoint(b) :", a.isdisjoint(b))   # do they share nothing?
print()

# The "=" versions modify the set in place:
#   a &= b   means   a = a & b   (keep only shared)
#   a |= b   means   a = a | b   (add all of b)
#   a -= b   means   a = a - b   (remove b's items)
#   a ^= b   means   a = a ^ b   (keep the odd-ones-out)
c = {1, 2, 3, 4}
c &= b
print("c after c &= b :", c)     # {3, 4}

# Memory hooks:
#   &  -> "and"  (in both)
#   |  -> "or"   (in either)
#   -  -> minus  (take away)
#   ^  -> odd one out (in exactly one)