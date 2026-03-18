file = open("city.txt", "r")

total_area = 0

for line in file:
    city, population, area = line.split()
    population = float(population)
    area = float(area)

    print("City:", city, "Population:", population, "Area:", area)

    if population > 10:
        print("Population > 10 lakhs:", city)

    total_area = total_area + area

print("Total area of all cities:", total_area)

file.close()