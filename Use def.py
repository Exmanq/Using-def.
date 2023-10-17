print("Let's consider companies that produce decent microphones.")
def name_company(name_company1,name_company2,name_company3):
    print(f"The first company is ours:{name_company1}")
    print(f"The second company is also ours:{name_company2}")
    print(f"And finally, the third company is also ours:{name_company3}")

name_company("Hyperx","Ritmix","Razer")

print("Great, now let's look at their financial state in dollars:")

def bank_company(company,bank):
    print(f"At the moment, {company} has assets worth:{bank}")

bank_company("Hyperx", "700 million dollars")
bank_company("Ritmix", "500 million dollars")
bank_company("Razer", "550 million dollars")

def owners(owner_company,owner_age):
    print(f"First owner: {owner_company}, His age is: {owner_age}")

owners("Jonas Jerebko","37" )

def bank_sum(bank,num1=0,num2=0,num3=0):
     print(f"The bank of three companies amounts to:{bank}")
     print(int(num1)+int(num2)+int(num3))

bank_sum(bank="",num1=700, num2=500,num3=550)
    