
amount=int(input("Enter the amount of money: "))
thous_n=amount // 1000
amount %= 1000

five_hun_n=amount // 500
amount %= 500

hun_n=amount // 100
amount %= 100

print("1000 notes:",thous_n)
print("500 notes:",five_hun_n)
print("100 notes:",hun_n)
