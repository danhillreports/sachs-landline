import csv
import json

expectancy = open('expectancy/expectancy.csv')
expectancy_reader = csv.DictReader(expectancy)

growth = open('growth/growth.csv')
growth_reader = csv.DictReader(growth)

data = open('countries.json')
data = json.load(data)


def calc_expectancy_color(val):
    val = float(val)
    if val <= 40:
        return "#870307"
    elif val > 40 and val < 55:
        return "#fc874c"
    elif val >= 55 and val < 70:
        return "#8f5082"
    elif val >= 70:
        return "#1b0fbd"
    else:
        return "#b0b0b0"


def calc_growth_color(val):
    val = float(val)
    if val <= -2.5:
        return "#870307"
    elif val > 2.5 and val < 0:
        return "#fc874c"
    elif val >= 0 and val < 2.5:
        return "#8f5082"
    elif val >= 2.5:
        return "#1b0fbd"
    else:
        return "#b0b0b0"


def process_csv(reader, metric):
    for row in reader:
        name = row['Country Name']
        for i in range(0, len(data['features'])):
            if data['features'][i]['properties']['name'] == name:
                data['features'][i]['properties'][metric] = {}
                val = row['2012']
                if val == '':
                    data['features'][i]['properties'][metric]['color'] = '#b0b0b0'
                else:
                    if metric == 'expectancy':
                        data['features'][i]['properties'][metric]['color'] = calc_expectancy_color(val)
                    else:
                        data['features'][i]['properties'][metric]['color'] = calc_growth_color(val)
                data['features'][i]['properties'][metric]['expectancy'] = val

process_csv(expectancy_reader, 'expectancy')
process_csv(growth_reader, 'growth')

print json.dumps(data)
