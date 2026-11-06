def create_name(first,last):
    first=first.capitalize()
    last=last.capitalize()
    return first+" "+last #return把結果交回給呼叫的地方

full_name=create_name("yang","lin hsuan")

print(f"Hello ! {full_name}")