def Power(number,power):
    if power<=1:
        return 1
    else:
        return number*Power(number,power-1)
print(Power(int(input()),(int(input()))+1))