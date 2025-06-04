# a=0
# i=0
# while i<100:
#     a=a+1
#     print(a)
#     if a==87:
#         continue
#     i=i+1
    


a = 0
i = 0
seen_numbers = set()
output_count=0

while i < 100:
    a += 1
    print(a)
    output_count += 1

    if a in seen_numbers:
        print(f"Repeating number found: {a}")
        break  # Exit the loop if a repeating number is found
    seen_numbers.add(a)
    
    if a == 87:
        continue  # This will skip the current iteration, but `i` will not increment
    if a== 100:
        break

    i += 1

if i == 100:
    print("No repeating numbers found")

print("number of output is ",output_count)