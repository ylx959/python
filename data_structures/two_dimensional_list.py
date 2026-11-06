#matrix

fruits=["apple","orange","coconut","banana"]
vegetables=["celery","potatoes","carrots"]
meats=["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats] #list裡面放list就是二維結構

for collection in groceries:
    for food in collection:
        print(f"{food} ",end="")
    print()