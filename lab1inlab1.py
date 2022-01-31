def printAllCombinations(pattern,i=0):
    if not pattern:
        return
    if i==len(pattern):
        print(''.join(pattern))
        return
    if pattern[i]=='?':
        for ch in '01':
            pattern[i]=ch
            printAllCombinations(pattern,i+1)
            pattern[i]='?'
    else:
        printAllCombinations(pattern,i+1)
pattern=input()
printAllCombinations(list(pattern))