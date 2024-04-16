# Define the mapping from Kazakh names to English names
name_map = {
    'Абай': 'Abay',
    'Ақмола': 'Akmola',
    'Ақтөбе': 'Aktobe',
    'Алматы': 'Almaty',
    'Атырау': 'Atyrau',
    'Батыс Қазақстан': 'West Kazakhstan',
    'Жамбыл': 'Zhambyl',
    'Жетісу': 'Zhetisu',
    'Қарағанды': 'Karagandy',
    'Қостанай': 'Kostanay',
    'Қызылорда': 'Kyzylorda',
    'Маңғыстау': 'Mangystau',
    'Павлодар': 'Pavlodar',
    'Солтүстік Қазақстан': 'North Kazakhstan',
    'Түркістан': 'Turkistan',
    'Ұлытау': 'Ulytau',
    'Шығыс Қазақстан': 'East Kazakhstan',
    'Астана қаласы': 'Nur-Sultan city',
    'Алматы қаласы': 'Almaty city',
    'Шымкент қаласы': 'Shymkent city'
}

# Define file paths
input_csv = '../archive/source.csv'
output_csv = '../data/higher_education.csv'

# Open the input CSV file and read from it
with open(input_csv, 'r', encoding='utf-8') as file:
    lines = file.readlines()

# Process each line, replacing the region/city name using the map
processed_lines = []
for line in lines:
    parts = line.strip().split(',')
    if parts[0] in name_map:
        parts[0] = name_map[parts[0]]
    processed_line = ','.join(parts)
    processed_lines.append(processed_line)

# Open the output CSV file and write to it
with open(output_csv, 'w', encoding='utf-8') as file:
    for line in processed_lines:
        file.write(line + '\n')

print("Data has been processed and saved to", output_csv)
