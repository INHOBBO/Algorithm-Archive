def solution(phone_book):
    phone_dic = {}
    for phone_number in phone_book:
        phone_dic[phone_number] = 1 

    for phone_number in phone_book: #1번 순회: phone_number = '119'
        temp = ""
        for number in phone_number: # number = '1'
            temp += number # temp = '1'
            if temp in phone_dic and temp != phone_number: # '1' in '119' and '1' != '119'
                return False
                
    return True

