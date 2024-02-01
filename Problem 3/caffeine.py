'''
Name: Logan Roman
Lab Time: Thurs 2:00
'''
def caffeine():
    caffeine_mg = float(input())
    ''' Type your code here. '''
    caffeine_mg/=2
    print(f"After 6 hours: {caffeine_mg:.2f} mg")
    caffeine_mg/=2
    print(f"After 12 hours: {caffeine_mg:.2f} mg")
    caffeine_mg/=4
    print(f"After 24 hours: {caffeine_mg:.2f} mg")
if __name__ == "__main__":
    caffeine()