def check_key(message,keyword):
    message_real=message#lower(message)
    keyword_real=keyword#lower(keyword)
    message_array=message_real.split()
    for i in range(1,26):
        new_key=''
        for k in keyword:
            if k.isupper():
                new_key+=chr((ord(k) - ord('A') + i) % 26 + ord('A'))
            else:
                new_key+=chr((ord(k) - ord('a') + i) % 26 + ord('a'))
        for j in message_array:
            if j==new_key:
                return i
    return 0

# def gen_key(message,keyword):
#     for i in range(0,26):
#         new_key=''
#         for k in keyword:
#             if k.isupper():
#                 new_key+=chr((ord(k) - ord('A') - i) % 26 + ord('A'))
#             else:
#                 new_key+=k
#         if check_key(message,new_key):
#             return i

def uncrypted(message,keyword):
    position=check_key(message,keyword)
    un_message=''
    for letter in message:
        if letter.isupper():
            un_message+=chr((ord(letter)-ord('A')-position) % 26 + ord('A'))
        else:
            un_message+=chr((ord(letter)-ord('a')-position) % 26 + ord('a'))
    return un_message

print(uncrypted('wklv lv d whvw','test'))

