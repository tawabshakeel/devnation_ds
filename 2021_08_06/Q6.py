import csv

def all_distinct_vehicle_classes(csv_all_data):
    all_classes_list = []
    for i in csv_all_data:
        if i not in all_classes_list:
            all_classes_list.append(i['class'])
    return all_classes_list
def get_hwy_mpg_avg():
    with open('mpg.csv') as mpg_csv:
        csv_all_data = list(csv.DictReader(mpg_csv))
    all_dist_classes = all_distinct_vehicle_classes(csv_all_data)
    final_list = []
    for vehicle_class in all_dist_classes:
        milage_sum = 0
        car_counter = 0
        for data_row in csv_all_data:
            if data_row['class'] == vehicle_class:
                milage_sum += float(data_row['hwy'])
                car_counter += 1
        final_list.append((vehicle_class, milage_sum / car_counter))
        final_list.sort(key=lambda x: x[1])

    return final_list