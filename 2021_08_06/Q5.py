import csv
def all_distinct_cylinders(csv_all_data):
    all_cylinders_list = []
    for ele in csv_all_data:
        if ele['cyl'] not in all_cylinders_list:
            all_cylinders_list.append(ele['cyl'])

    return all_cylinders_list

def get_city_mpg_avg():
    #   Reading CSV file
    with open('mpg.csv') as mpg_csv:
        csv_all_data = list(csv.DictReader(mpg_csv))

    all_dist_cylinders = all_distinct_cylinders(csv_all_data)

    resultant_list = []
    for cyl in all_dist_cylinders:
        milage_sum = 0
        car_counter = 0

        for i in csv_all_data:
            if i['cyl'] == cyl:
                milage_sum += float(i['cty'])
                car_counter += 1
        resultant_list.append((cyl, milage_sum / car_counter))
        resultant_list.sort(key=lambda x: x[0])

    return resultant_list