def checkPalindrome(word):
    i = 0
    j = len(word) - 1
    isPalindrome = True
    while i != j:
        if word[i] != word[j]:
            isPalindrome = False
            break
        i += 1
        j -= 1
    print(f"checkPalindrome({word}) = {isPalindrome}")


word = input()
checkPalindrome(word)
