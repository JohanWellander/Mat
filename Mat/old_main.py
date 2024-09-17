from food_list import *
import csv


dir = os.getcwd()
main_list = FoodList()
## Read file from livsmedelverket
#---------------------------------------------------------------------------------------------------------
#Create reference
file_name = "/Livsmedel.xlsx"
livsmedelslista = Livsmedelsverket()
livsmedelslista.read_excel_file(dir+file_name)
livsmedelslista.clean()
#---------------------------------------------------------------------------------------------------------
##Read food from receipt and compare with reference
#INSTALLERA TESSERACT https://github.com/UB-Mannheim/tesseract/wiki NÅGONSTANS. FYLL SEDAN I PATHEN <tess_path>:
new_list = FoodList()
tess_path = r'C:/Users/johwel01/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'
for kvitto in os.listdir(dir+"/kvitton"):
    new_list.read_receipt(dir+"/kvitton",kvitto, tess_path)
    main_list.add_item(livsmedelslista.filter_food(new_list.grocery_list))
#---------------------------------------------------------------------------------------------------------
#main_list.grocery_list = livsmedelslista.filter_food(main_list.grocery_list)
#---------------------------------------------------------------------------------------------------------
# Saving new item
file_path = os.path.join(os.getcwd(), "main_food_list.xlsx")
main_list.save_items(file_path)

#---------------------------------------------------------------------------------------------------------
# Delete items
thing_to_remove = ["chips", "broccoli", "filmjölk"]
main_list.delete_item(file_path,thing_to_remove)

thing_to_remove = "ciabatta"
main_list.delete_item(file_path,thing_to_remove)


#print(type(main_list.grocery_list))









# list.__str__()


