import pandas as pd
import csv
import json
import hashlib

# Converting excel file to csv
read_file = pd.read_excel(r'.\NFT-Naming-csv.xlsx')
read_file.to_csv(r'.\hngi9.csv', index=None, header=True)

# Creating output csv file and saving it in 'output' directory.....opening it and writing a header to it
output_csv = 'output/filename_output.csv'
open_file = open(output_csv, 'w')
writer = csv.writer(open_file)

# Reading the csv file. Omittin first row because it's headers
with open('hngi9.csv', 'r') as csv_file:
    read_csv = csv.reader(csv_file, delimiter=',')
    next(read_csv)
    data = [x for x in read_csv]


    # Creating json for each row in csv
    for row in data:
         if row[1] and row[2]:
            
            series_number = row[0]
            file_name = row[1]
            name= row[2]
            description= row[3]
            gender = row[4]
            attributes = row[5]
            uuid = row[6]

            # Creating a dictionary with the keys and values using the given json format
            json_file = {
                'format' : 'CHIP-0007',
                'name' : file_name.replace('-', ' ').title(),
                'description' : '',
                'minting_tool' : '',
                'series_number' : series_number,
                'sensitive_content' : False,
                'series_total' : data[-1][0],
                 "attributes": [
                    {
                        "trait_type": "gender",
                        "value": gender
                    }
                ],
                "collection": {
                    "name": "Zuri NFT tickets for free lunch",
                    "id": uuid,
                    "attributes": [
                        {
                            "type": "description",
                            "value": "Rewards for accomplishments during HNGi9"
                        }
                    ]
                },
            }

            # Creating a json file for each row in the csv file
            jsonObject = json.dumps(json_file, indent=4) # Converting the json file to a string.
            with open(f'json/{file_name}.json', 'w') as output:
                output.write(jsonObject)
            output.close()

           # Creating a hash of the json file and appending it to the csv file.
            hashString = hashlib.sha256(jsonObject.encode()).hexdigest()
           # Appending the file name to the csv file.
            row.append(hashString)
            writer.writerow(row)

# Closing the file.
open_file.close()