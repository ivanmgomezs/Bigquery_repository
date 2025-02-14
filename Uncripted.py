

# def decipher(message,keyword):
#     shift=find_shift(message,keyword)
#     decrypted_text=

def find_shift(message,keyword):
    len_message=len(message)
    len_keyword=len(keyword)
    for i in range(len(message)-len(keyword)+1):
        slice_ch=message[i:i+len(keyword)]
        # print(slice_ch)
        shift=calculate_shift(slice_ch,keyword)
        if shift is not None:
            return shift
    return None

def calculate_shift(message_segment,keyword):
    shift=ord(message_segment[0])-ord(keyword[0])
    for i in range(1,len(message_segment)):
        if (ord(message_segment[i])-ord(keyword[i])) != shift:
            return None
    return shift



print(find_shift('this is a test','test'))