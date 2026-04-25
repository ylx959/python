#matrix

fruits=["apple","orange","cococut","banana"]
vegetables=["celery","potatoes","carrots"]
meats=["chicken","fish","turkey"]

groceries=[fruits,vegetables,meats]

for collection in groceries:
    for food in collection:
        print(f"{food} ",end="")
    print()