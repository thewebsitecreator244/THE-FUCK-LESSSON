points = float(input("how many points have you got?: "))
homan = float(input("out of how many?: "))
note = float(points*5/homan+1).__round__(1)
print("your note is", note)
