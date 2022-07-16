text = input().lower()
count = 0

if text.count("sand"):
    count += text.count("sand")
if text.count("water"):
    count += text.count("water")
if text.count("fish"):
    count += text.count("fish")
if text.count("sun"):
    count += text.count("sun")

print(count)