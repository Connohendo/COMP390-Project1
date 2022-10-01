import meteor_data_class

mass_list = []
year_list = []
meteor_list = []


def create_list(file_name):
    with open(f'{file_name}', 'r') as meteor_data:
        meteor_data.readline()
        for line in meteor_data:
            line = str(line)
            new_line = line.strip()
            line_list = new_line.split('\t')
            while len(line_list) <= 11:
                line_list.append(None)
            create_meteor_obj(line_list)

        for meteor in meteor_list:
            check_mass(meteor)
            check_year(meteor)

        print_results()


def create_meteor_obj(line_list):
    meteor_data_obj = meteor_data_class.MeteorDataEntry()
    meteor_data_obj.set_name(line_list[0])
    meteor_data_obj.set_id(line_list[1])
    meteor_data_obj.set_nametype(line_list[2])
    meteor_data_obj.set_recclass(line_list[3])
    meteor_data_obj.set_mass(line_list[4])
    meteor_data_obj.set_fall(line_list[5])
    meteor_data_obj.set_year(line_list[6])
    meteor_data_obj.set_reclat(line_list[7])
    meteor_data_obj.set_reclong(line_list[8])
    meteor_data_obj.set_geoloc(line_list[9])
    meteor_data_obj.set_states(line_list[10])
    meteor_data_obj.set_counties(line_list[11])
    meteor_list.append(meteor_data_obj)


def check_mass(meteor):
    mass = meteor.mass
    if mass.isnumeric() and int(mass) >= 2900000:
        mass_list.append(meteor)


def check_year(meteor):
    year = meteor.year
    if year is not None and year.isnumeric() and int(meteor.year) >= 2013:
        year_list.append(meteor)

def print_results():
    name = 'Name'
    mass = 'Mass (g)'
    print(f'{name:<24}{mass:<20}')
    print('=' * 34)
    for meteor in mass_list:
        name_label = meteor.name
        mass_label = meteor.mass
        print(f'{name_label:<24}{mass_label:<20}')

    print('\n')

    name = 'Name'
    mass = 'Year'
    print(f'{name:<24}{mass:<20}')
    print('=' * 34)
    for meteor in year_list:
        name_label = meteor.name
        year_label = meteor.year
        print(f'{name_label:<24}{year_label:<20}')