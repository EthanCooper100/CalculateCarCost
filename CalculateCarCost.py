indication = True
while indication:
    Car_Cost = {
        "Toyota": {
            "4Runner": {
                "2024": 40705 
                },
            "bZ4X": {
                "2024": 43070
                },
            "Camry": {
                "2024": 26420
                },
            "Corolla": {
                "2024": 22050
                },
            "Crown": {
                "2024": 40350
                },
            "GR86": {
                "2024": 29300
                },
            "Highlander": {
                "2024": 39270
                },
            "Venza": {
                "2024": 35070
                },
            "Land Cruiser": {
                "2024": 55950
                },
            "Mirai": {
                "2024": 50190
                },
            "Prius": {
                "2024": 27950
                },
            "RAV4": {
                "2024": 28675
                },
            "Sequoia": {
                "2024": 61275
                },
            "Sienna": {
                "2024": 37685
                },
            "Supra": {
                "2024": 46440
            }

            } #Retrieved from Toyota
        # "Honda": 31187, #Retrieved from CarEdge
        # "Chevrolet": 39705, #Retrieved from CarEdge
        # "Nissan": 38105 #Retrieved from CarEdge
    }
    def information(name, model, year, cost):
        return(f'${Car_Cost[name][model][year]}')
        
    name = input("What Car Cost do you want to know: ")
    while name not in Car_Cost.keys():
        print(f'Not in the list!')
        name = input("What Car Cost do you want to know: ")
    model = input("What Model: ")
    while model not in Car_Cost[name].keys():
        print(f'Not in the list!')
        model = input("What Model: ")
    year = str(input("What Year: "))
    while year not in Car_Cost[name][model].keys():
        print(f'Not in the list!')
        year = input("What Year: ")
    most_expensive_car_price = 0
    most_expensive_car_name = ''
    most_cheapest_car_price = 0
    most_cheapest_car_name = ''
    total_cost_combined = 0
    count = 0
    for x in Car_Cost.values():
        #print(x)
        for a, y in x.items():
            #print(y)
            for z in y.values():
                #print(z)
                if z > most_expensive_car_price:
                    most_expensive_car_price = z
                    most_expensive_car_name = a
                    most_cheapest_car_price = most_expensive_car_price
    for x in Car_Cost.values():
        #print(x)
        for a, y in x.items():
            #print(y)
            for z in y.values():
                #print(z)
                if z < most_cheapest_car_price:
                    most_cheapest_car_price = z
                    most_cheapest_car_name = a
                total_cost_combined += z
                count += 1
    average_cost = total_cost_combined / count
    print(f'{year} {name} {model} car price: {information(name, model, year, 2)}')
    print(f'Most expensive car for {name}: {most_expensive_car_name} ${most_expensive_car_price}')
    print(f'Most cheapest car for {name}: {most_cheapest_car_name} ${most_cheapest_car_price}')
    print(f'Average cost of a {name}: ${average_cost}')
    indication = input("Do you want to continue? Press Y for yes and N for no: ")
    while indication != "Y" and indication != "N":
        print("Invalid")
        indication = input("Do you want to continue? Press Y for yes and N for no: ")
    if indication == "N": 
        indication = False
print("Thank you for using this tool! Created by Ethan Cooper!")