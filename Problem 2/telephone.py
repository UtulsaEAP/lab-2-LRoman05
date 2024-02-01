'''
Name: Logan Roman
Lab Time: Thurs 2:00
'''
def telephone():
    phone_number = int(input())
    ''' Type your code here. '''
    print(f"({phone_number//10000000}) {(phone_number//10000)%1000}-{phone_number%10000}")
if __name__ == "__main__":
    telephone()