import os
import csv
import json

def generate_metadata():
    csv_file_path = 'skrapsclubtraits.csv'
    output_folder = 'metadata'
    
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    image_base_url = "https://raw.githubusercontent.com/skrapsclub/skrapsimages/main/images/"

    with open(csv_file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        
        for row in reader:
            token_id = row.get('New_ID')
            if not token_id:
                continue
                
            attributes = []
            for key, value in row.items():
                if key != 'New_ID' and value and value.lower() != 'none' and value != '-':
                    attributes.append({
                        "trait_type": key,
                        "value": value
                    })
            
            metadata = {
                "name": f"Skraps Club #{token_id}",
                "description": "Skraps Club NFT Collection generated via GitHub.",
                "image": f"{image_base_url}{token_id}.webp",
                "attributes": attributes
            }
            
            # File name without extensions (0, 1, 2, etc.)
            file_path = os.path.join(output_folder, str(token_id))
            with open(file_path, 'w', encoding='utf-8') as out_file:
                json.dump(metadata, out_file, indent=4)

if __name__ == "__main__":
    generate_metadata()
