import random,string
def generate_password(length,use_letters=True,use_digits=True,use_symbols=True):
    character_pool=''
    if use_letters:
        character_pool+=string.ascii_letters 
    if use_digits:
        character_pool+=string.digits        
    if use_symbols:
        character_pool+=string.punctuation
    if not character_pool:
      raise ValueError("At least one character type must be selected.")
    return''.join(random.choice(character_pool) for _ in range(length))
def get_user_input():
    try:
        length=int(input("Enter desired password length: "))
        if length<=0:
            raise ValueError 
        use_letters=input("Include Letters?(YES(y)/NO(n)): ").strip().lower()=='y'
        use_digits=input("Include Digits?(YES(y)/NO(n)): ").strip().lower()=='y'
        use_symbols=input("Include Symbols?(YES(y)/NO(n)): ").strip().lower()=='y'
        password=generate_password(length,use_letters,use_digits,use_symbols)
        print(f"\nGenerated Password:{password}")
    except ValueError:
        print("Invalid input.Please enter a positive integer for length.")
if __name__ == "__main__":
    get_user_input()