# dict = dictionary
rus_to_eng = {"ананас": "pineapple", "собака": "dog", "питон": "python"}
# dict elements--pairs key-value
# get elements:
print(rus_to_eng["ананас"])
# change elements
rus_to_eng["собака"] = "hound"
print(rus_to_eng)
# add elements:
rus_to_eng["привет"] = "hello"
print(rus_to_eng)
# len
print(len(rus_to_eng))
# remove elements
del rus_to_eng["привет"]
print(rus_to_eng)
rus_to_eng.pop("собака")
print(rus_to_eng)
# for loop with dict
for i in rus_to_eng:
    print(i)
# i-key
for key, value in rus_to_eng.items():
    print(f'{key}:{value}')
