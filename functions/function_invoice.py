def display_invoice(username,amount,due_date):
    print(f"Hello {username}")
    print(f"your bill of ${amount:.2f} is due:{due_date}") #.2f 顯示到小數第2位


display_invoice("Brocode",100.232,"01/01")


    