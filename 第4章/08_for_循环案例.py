# coding=utf-8

# 单次字符串加密解密的程序
# 字符串加密程序
# encrypted_content = input('请输入要加密的内容：')
# secret = chr(ord(encrypted_content) + 1)
# print(f'加密出来的内容：{secret}')
#
# # 字符串解密程序
# decrypted_content = input('请输入要解密的内容：')
# secret = chr(ord(decrypted_content) - 1)
# print(f'解密出来的内容：{secret}')

# # 字符串加密程序
# encrypted_content = input('📝请输入要加密的内容：')
# secret = ''
# for s in encrypted_content:
#     secret = secret + chr(ord(s) + 1)
# print(f'㊙️经过加密后的内容为：{secret}')
#
# # 字符串解密程序
# decrypted_content = input('📝请输入要解密的内容：')
# secret = ''
# for s in decrypted_content:
#     secret += chr(ord(s) - 1)
# print(f'📃经过解密后的内容为：{secret}')

# For Example：
# # 加密代码
# text = input('📝请输入要加密的文字：')
# secret = ''
# for t in text:
#     secret += chr(ord(t) + 1)
# print(f'㊙️经过加密后的内容为：{secret}')
#
# # 解密代码
# secret = input('📝请输入要解密的文字：')
# text = ''
# for s in secret:
#     text += chr(ord(s) - 1)
# print(f'📃经过解密后的内容为：{text}')

text = input('📝请输入要加密的文字：')
secret = ''
for t in text: # 遍历用户输入的字符串
    secret += chr(ord(t) + 1)
print(f'㊙️经过加密后的内容为：{secret}')

secret = input('📝请输入要解密的文字：')
text = ''
for s in secret:
    text += chr(ord(s) - 1)
print(f'📃经过解密后的内容为：{text}')