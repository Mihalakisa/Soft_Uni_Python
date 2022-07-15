words = input().split(" ")
palindrome_words = []
palindrome = input()

for word in words:
    # rev2_list = []
    # for ch in word:
    #     rev2_list.append(ch)
    # rev2_list.reverse()

    rev_list = reversed(word)
    rev_word = "".join(rev_list)
    if rev_word == word:
        palindrome_words.append(word)

print(palindrome_words)
palindrome_count = words.count(palindrome)
print(f"Found palindrome {palindrome_count} times")
