import csv

def fix_turnstile_data(filenames):
    for name in filenames:
        f_in = open(name, 'r')
        f_out = open('updated_' + name, 'w')

        reader = csv.reader(f_in, delimiter=',')
        writer = csv.writer(f_out, delimiter=',')

        for line in reader:
            number_of_line = int(round(len(line[3:])/5))
            lines = []
            for i in range(number_of_line):
                start_idx = 3+5*i
                updated_data = line[:3] + line[start_idx: start_idx+5]
                lines.append(updated_data)

            for l in lines:
                writer.writerow(l)

        f_in.close()
        f_out.close()
