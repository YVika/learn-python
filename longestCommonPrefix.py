def longestCommonPrefix(strs: list[str]) -> str:
    strs.sort()

    prefix = ""

    for i in range(len(strs[0])):
        if strs[0][i] != strs[-1][i]:
            return prefix
        prefix += strs[0][i]
    return prefix


print(longestCommonPrefix(["flower", "flow", "flight"]))
print(longestCommonPrefix([""]))
