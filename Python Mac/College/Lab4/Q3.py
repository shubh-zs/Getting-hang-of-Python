# Use the names of three cities as keys in your dictionary. Create a dictionary of information about each city and include the country that the city is in

delhi = {"Country":"India","population":"32 Million","fact":"Delhi is known for its intense growth factor and pollution."}
tokyo = {"Country":"Japan","population":"37 Million","fact":"Most populous city in the World."}
osaka = {"Country":"Japan","population":"20 Million","fact":"The pink leaf fall ddolage is vary popular in the World."}

city = {"Delhi":delhi, "Tokyo":tokyo, "Osaka":osaka}

for i in city:
    print("The chosen city is : ",i,"\n\n\tFacts about this city are as follows : ") 
    for j,k in city[i].items():
        print("\t",j.title()," : ",k,end="\n")
    
