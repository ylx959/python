#dictionary==a collection of {key:value pairs ordered and changable no duplicates}


capitals={"USA":"washington D.C.",
            "India":"New Delhi",
            "China":"Beijing",
            "Russia":"moscow"}

#print(dir(capitals))
#print(help(capitals))

#print(capitals.get("USA"))

#capitals.update({"Germany":"Berlin"})
#capitals.update({"Japan":"Tokyo"})

#capitals.pop("China")
#capitals.clear()

#key=capitals.keys()


#print(capitals)
#for key in capitals.keys():
   # print(key)

#for value in capitals.values():
    #print(value)
for key,value in capitals.items():
    print(f"{key}:{value}")
