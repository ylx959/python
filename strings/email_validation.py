gmail=input("Enter your gmail address: ")


if "@" in gmail and "." in gmail: #同時有@和.才算合法
    print("valid email")
else:
    print("Invalid email")