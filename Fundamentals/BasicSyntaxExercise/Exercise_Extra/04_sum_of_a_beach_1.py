input_str = input()
lower_string = input_str.lower()

counter = lower_string.count("sun") + lower_string.count("fish") + lower_string.count("sand")\
          + lower_string.count("water")

print(counter)