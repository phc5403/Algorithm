def solution(numbers):
    answer = ""
    temp = ""
    
    digits = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

    for n in numbers:
        temp += n
        
        if temp in digits:
            # print(temp, type(temp), digits.index(temp), type(digits.index(temp)))
            
            answer += str(digits.index(temp))
            temp = ""
    
    return int(answer)