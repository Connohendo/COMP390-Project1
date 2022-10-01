import meteor_data_class

mass_list = []
year_list = []


def create_list(file_name):
    with open(f'{file_name}', 'r') as meteor_data:
        meteor_data.readline()
        for line in meteor_data:
            line = str(line)
            new_line = line.strip()
            line_list = new_line.split('\t')
            meteor_data_obj = check_mass(line_list)
            mass_list.append(meteor_data_obj)


def check_mass(line_list):
    if line_list[4].isnumeric() and int(line_list[4]) > 29000000:
        meteor_data_obj = meteor_data_class.MeteorDataEntry(line_list[0], line_list[1], line_list[2], line_list[3],
                                                            line_list[4], line_list[5], line_list[6], line_list[7],
                                                            line_list[8], line_list[9], line_list[10], line_list[11])
        return meteor_data_obj
    else:
        return


def check_year():
    return "hi"

