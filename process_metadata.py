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
            if token_id is None or token_id.strip() == '':
                continue
                
            attributes = []
            for key, value in row.items():
                # Checking if value exists, is not empty, and is not a placeholder
                if key != 'New_ID' and value and value.strip() != '' and value.strip() != '-' and value.lower() != 'none':
                    attributes.append({
                        "trait_type": key,
                        "value": value.strip()
                    })
            
            metadata = {
                "name": f"Skraps Club #{token_id}",
                "description": "Skraps Club NFT Collection generated via GitHub.",
                "image": f"{image_base_url}{token_id}.webp",
                "attributes": attributes
            }
            
            # File without extension
            file_path = os.path.join(output_folder, str(token_id))
            with open(file_path, 'w', encoding='utf-8') as out_file:
                json.dump(metadata, out_file, indent=4)

if __name__ == "__main__":
    generate_metadata()
