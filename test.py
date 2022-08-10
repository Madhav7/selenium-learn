# def addi_tion(a, b):
#     return a+b
#
#
# c = addi_tion(5, 4)
# d = addi_tion(5, 6)
#
# print(c, d)

def isValid(s):
        stack = []
        dict = {"]":"[", "}":"{", ")":"("}
        for char in s:

            if char in dict.values():
                stack.append(char)
            elif char in dict.keys():
                if stack == [] or dict[char] != stack.pop():
                    return False
            else:
                return False
        return stack == []

print(str(isValid('[({)]')))
