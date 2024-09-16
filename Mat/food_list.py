import pytesseract
from PIL import Image
import os
import csv
import re
import string
import pandas as pd

class FoodList():

    def __init__(self):
        self.grocery_list = []
        

    def delete_item(self, item:string):
        if type(item) is list:
            for i in item:
                index = self.grocery_list.index(i.capitalize())
              
                self.grocery_list.pop(index)
        else:
            index = self.grocery_list.index(item.capitalize())
            self.grocery_list.pop(index)

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
    
    def read_receipt(self, dir,image, tess_path):
        image = Image.open(f"{dir}/{image}.png")
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
    
    def filter_food(self,new_list:list):
        filtered_food = self.food_list[self.food_list["Livsmedel"].isin(new_list)]
        return filtered_food.Livsmedel.unique()
    
    

        
