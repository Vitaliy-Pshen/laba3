def decoder(text):

    text_new = ''
    digit = ''
    step1 = -1



    for a in text:
            range_ = ord(a)
            if range_ in range(48,58):
                digit = digit + a
                continue
            elif digit != "":
                    digit = int(digit)
                    digit = digit + step1
                    digit = str(digit)
                    text_new = text_new + digit
                    digit = ""

            if range_ in range(97,122) or range_ in range(1072,1103) or range_ in range(65,90) or range_ in range(1040,1071) or range_ == "1168"or"1169"or"1028"or"1108"or"1031"or"1111": 
                if a == "A":                                                                                                                                                              
                                                                                                                                                                                        
                    a = "Z"                                                                                                                                                             
                    text_new = text_new + a
                    continue
                elif a == "a":
                    a = "z"
                    text_new = text_new + a
                    continue
                elif a == "А":
                    a = "Я"
                    text_new = text_new + a
                    continue
                elif a == "а":
                    a = "я"
                    text_new = text_new + a
                    continue
                else:
                    code_of_symbol = ord(a)
                    code_of_symbol += step1
                    a = chr(code_of_symbol)
                    text_new = text_new + a
                    continue
    if digit != "":
        digit = int(digit)
        digit = digit + step1
        digit = str(digit)
        text_new = text_new + digit
    return text_new
help(decoder)
while True:
    abc_text = input()
    abc_text = decoder(abc_text)
    print(abc_text)
