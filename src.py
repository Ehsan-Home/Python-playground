# str = "ehsan\\n\m"

# str = input()
# # str = "\n\n\m"

# dict = {"name":str.encode()}

# str2 = dict["name"]

# # print(len(str))
# print(str)
# print(str2)

# bytes = input()
# bytes = b"^\x84\x7f5\x8e:%\x90\x8b\x85\xb6\x9a\x98T\xfbS\x98D;F@p\xd2\x10\xaf0\xf6_?\xbb\xd93\xddUMs]n\x16\xb0r\xe9%\x96\xbe\xa7\x1dE\xefv\x1a+\xda\xd5x\xc6\xb6N\xcdv\x8b\xb6=p\r&=K\x97\x04\xd9\x8c~\x10WU\xe4\x83B\xc8\xd0\xa1Pv/\xaf\xf7\xdfBFn\xc9\xdd\x97\xefA\x91\xdf\xb5mr\x96\x16\x1b\xdeo;5:W\x80\x1d*\xd9\xf8\xdc&\x14\x16f\xb1\x90\x14\x92\xa7\xa1g\x00"

# bytes = bytes.encode()

# print("-----")
# print(bytes)
# print("-----")

# str = bytes.decode('Latin')

# print("-----")
# print(str)

str = """^
 5:%
&=KÙ~WUäBÈÐ¡Pv/¯÷ßBFnÉÝïAßµmro;5:W*ÙøÜ&f±§¡g
"""

bytes = str.encode()

print(bytes)