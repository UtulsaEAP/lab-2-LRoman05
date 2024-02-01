'''
Name: Logan Roman
Lab Time: Thurs 2:00
'''
def real_estate():
    
    current_price = int(input())
    last_month_price = int(input())
    # Your code goes here
    print(f"This house is ${current_price}. The change is ${current_price-last_month_price} since last month.")
    print(f"The estimated monthly mortgage is ${current_price*0.00425:.2f}.")
if __name__ == "__main__":
    real_estate()