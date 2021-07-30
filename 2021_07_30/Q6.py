import csv
def get_hwy_mpg_avg():
    with open('mpg.csv') as csv_file:
        file=list(csv.DictReader(csv_file))
    function=hwy_mileage(file)
    result=[]
    for c in function:
        sum_number=0
        count=0
        for i in file:
            if i['hwy']==c:
                sum_avg=sum_number+float(i['cty'])
                count=count+1
        result.append((c,sum_avg/count))
        result1= list(set(result.sort(key=lambda x:x[0])))
        return result1
def hwy_mileage(cyl):
    cylinder=[]
    for i in cyl:
        cylinder.append(i['cyl'])
    return list(cylinder)