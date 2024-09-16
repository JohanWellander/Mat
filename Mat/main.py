from food_list import *
import csv

dir = os.getcwd()
main_list = FoodList()
## Read file from livsmedelverket
file_name = "/Livsmedel.xlsx"
livsmedelslista = Livsmedelsverket()
livsmedelslista.read_excel_file(dir+file_name)
#print(livsmedelslista.food_list)

##Read food from receipt
#INSTALLERA TESSERACT https://github.com/UB-Mannheim/tesseract/wiki NÅGONSTANS. FYLL SEDAN I PATHEN <tess_path>:
new_list = FoodList()
tess_path = r'C:/Users/johwel01/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
kvitto = "kvitto3"
new_list.read_receipt(dir,kvitto, tess_path)

#print((new_list.grocery_list))


filtered_food = livsmedelslista.filter_food(new_list.grocery_list)
print(filtered_food)



# list.__str__()


