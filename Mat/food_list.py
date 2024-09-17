import pytesseract
from PIL import Image
import os
import csv
import re
import string
import pandas as pd
import xlsxwriter
import openpyxl




class FoodList():

    def __init__(self):
        self.grocery_list = []
        self.workbook = openpyxl.Workbook()
        

    def delete_item(self,file_path, item:string):
        if os.path.exists(file_path):
            df = pd.read_excel(file_path)
           
            if type(item) is list:
                for i in item:
                    # Remove rows where the 'Livsmedel' column contains `i`
                    df = df[df['Livsmedel'] != i]
                    print(f"deleted {i}")
            else:
                # Remove rows where the 'Livsmedel' column contains `item`
                df = df[df['Livsmedel'] != item]
                print(f"Deleted {item}")

            # Save the updated DataFrame back to the Excel file
            df.to_excel(file_path, index=False)
            print(f"Updated file saved to {file_path}")
        else:
            print(f"No file exist at {file_path}")


        

    def add_item(self, item: string):
        if type(item) is list:
            for i in item:
                self.grocery_list.append(i.lower())
        else:
            self.grocery_list.append(item.lower())

    def sort(self):
        self.grocery_list.sort()

    def __str__(self) -> str:
        print(self.grocery_list)

    def get_size(self):
        return len(self.grocery_list)
    
    def check_exist(self, new_list):
        pass

    def remove_non_letters(self, list):
        pass


    def save_items(self, file_path):
        self.grocery_list.sort()
        if os.path.exists(file_path):
            print("Adding groceries to list")
            df = pd.read_excel(file_path)
       
            df = df[df['Livsmedel'].notna() & (df['Livsmedel'] != '')]
          
            new_items = []

            # Iterate over the grocery list and collect new items to add
            for word in self.grocery_list:
                # Check if the word is in the 'Livsmedel' column
                if word in df["Livsmedel"].values:  # Use .values to check contents
                    #print("Already exists, moving on")
                    pass
                else:
                    #print("Adding item to list")
                    # Collect new items in a list of dictionaries
                    new_items.append({"Livsmedel": word})
            # If there are new items, concatenate them to the DataFrame
            if new_items:
                # Convert new items to a DataFrame and concatenate
                new_items_df = pd.DataFrame(new_items)
                print(f"New items added: {new_items_df["Livsmedel"]}")
                df = pd.concat([df, new_items_df], ignore_index=True)

            # Save the updated DataFrame to the Excel file
                df.to_excel(file_path, index=False)
            else:
                print("Nothing new to add, bye bye")
        else:
            print("Creating main_food_list.xlsx with existing food")
            self.grocery_list.sort()
            df = pd.DataFrame({"Livsmedel": self.grocery_list})
            df.to_excel(file_path, index=False)
            print(f"Created {file_path} with initial data.")

           
        
    def read_receipt(self, dir,image, tess_path):
        image = Image.open(f"{dir}/{image}")
        pytesseract.pytesseract.tesseract_cmd = tess_path
        self.grocery_list = pytesseract.image_to_string(image, lang="swe").lower().split()
         
    def remove_non_letters(self, input_string):
        # Use regular expression to remove all non-letter characters except spaces
        cleaned_string = re.sub(r'[^a-öA-Ö\s]', '', input_string)
        return cleaned_string



class Livsmedelsverket():
    def __init__(self):
        self.food_list = pd.DataFrame()
       

    def read_excel_file(self, file_path):
        livsmedelslista = pd.read_excel(io=file_path,usecols="A",skiprows=2) #Reads the file
        food_list = [word for item in livsmedelslista["Livsmedelsnamn"] for word in self.remove_non_letters(item).split()] # Remove weird things
        food_list = [row for row in food_list if all(len(word) >= 3 for word in row.split())] #Erase single letters
        food_list = [word.lower() for word in food_list]
        self.food_list = pd.DataFrame({"Livsmedel": food_list})
    

    def remove_non_letters(self, input_string):
        # Use regular expression to remove all non-letter characters except spaces
        cleaned_string = re.sub(r'[^a-öA-Ö\s]', '', input_string)
        return cleaned_string
    
    def clean(self): # Remove random words
        cleaned_words = []
        bad_words = ["röd", "gul", "svart", "grön", "blå", "ica", "och", "för","eko", "brun", "pulver"]
        for word in self.food_list["Livsmedel"]: 
            if word not in bad_words:
                 cleaned_words.append(word)
        self.food_list = pd.DataFrame({"Livsmedel": cleaned_words})

    
    def filter_food(self,new_list:list):
        filtered_food = self.food_list[self.food_list["Livsmedel"].isin(new_list)]
        return list(filtered_food.Livsmedel.unique())
    
    

        
