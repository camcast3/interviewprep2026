def encode_rle(s):

    encoded = ''
    current_char = None
    current_char_count = 0
    
    for char in s:
        if char.isalnum():
            if char == current_char:
                current_char_count += 1
            else:
                if current_char is not None:
                    encoded += current_char
                    encoded += str(current_char_count)
                current_char = char
                current_char_count = 1
    
    if current_char is not None and char.isalnum():
        encoded += current_char
        encoded += str(current_char_count)

    return encoded