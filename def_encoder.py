def encoder(text):
    
    text_new = ''
    digit = ''
    step1 = 1


    
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

           
            if range_ in range(97,123) or range_ in range(1072,1104) or range_ in range(65,91) or range_ in range(1040,1072) or range_ == "1168"or"1169"or"1028"or"1108"or"1031"or"1111": ###IMPORTANT NOTE:
                if a == "Z":                                                                                                                                                               ###LAST RANGE DEFINITION IS FOR CHARACTERS
                    a = "A"                                                                                                                                                                   ### WHICH ARE ADDED RECENTLY IN CHARSET SO THEY HAVE
                    text_new = text_new + a                                                                                                                                                      ### CODE NOT IN UKR ALPHABET RANGE
                    continue                                                                                                                                                                           ###WE WILL DEFINE THEM WITH OTHER CHARACTERS
                                                                                                                                                                                                       ### DECODER WILL DECODE THIS CHARACTERS NORMALLY
                elif a == "z":
                    a = "a"
                    text_new = text_new + a
                    continue
                elif a == "Я":
                    a = "А"
                    text_new = text_new + a
                    continue
                elif a == "я":
                    a = "а"
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
help(encoder)
while True:
    abc_text = input()
    abc_text = decoder(abc_text)
    print(abc_text)
           

