import os
import argparse
from food_list import FoodList, Livsmedelsverket

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Manage your food list")
    parser.add_argument('--delete', nargs='+', help='Item(s) to delete from the food list')
    parser.add_argument('--add', nargs='+', help='Item(s) to add to the food list')
    args = parser.parse_args()

    # Initialize FoodList instance
    file_path = os.path.join(os.getcwd(), "main_food_list.xlsx")
    print(file_path)
    main_list = FoodList()

    # If --delete is provided, delete the specified items
    if args.delete:
        items_to_remove = args.delete
        main_list.delete_item(file_path, items_to_remove)

    elif args.add:
        items_to_add = args.add
        main_list.add_item(items_to_add)
        main_list.save_items(file_path)

    else:
        # Perform your regular script actions here if no command-line arguments are provided
        print("No command provided. Adding food from reciepts...")
        # Your existing code for processing receipts and saving items
        dir = os.getcwd()
        main_list = FoodList()
        
        # Read file from livsmedelverket
        file_name = "/Livsmedel.xlsx"
        livsmedelslista = Livsmedelsverket()
        livsmedelslista.read_excel_file(dir + file_name)
        livsmedelslista.clean()
        
        # Read food from receipt and compare with reference
        tess_path = r'C:/Users/johwel01/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
        for kvitto in os.listdir(dir + "/kvitton"):
            new_list = FoodList()
            new_list.read_receipt(dir + "/kvitton", kvitto, tess_path)
            main_list.add_item(livsmedelslista.filter_food(new_list.grocery_list))

        # Save new items to the Excel file
        main_list.save_items(file_path)

if __name__ == "__main__":
    main()
