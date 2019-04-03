# for i in range(10):
#     if i == 999:
#         break
# else:
#     print("Unbroken 1")

# for i in range(10):
#     if i == 5:
#         break
# else: 
#     print("Unbroken 2")
for i in range(10):
    try: 
        if 10 / i == 2.0:
            break
    except ZeroDivisionError:
        print(i,1)
    else:
        print(i,2)