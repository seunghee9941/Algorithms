N = int(input())

for i in range(N):
    word = input()
    for j in range(len(word)-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                N -= 1
                break

print(N)
    
