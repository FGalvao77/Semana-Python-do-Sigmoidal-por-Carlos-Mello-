# -*- coding: utf-8 -*-
"""Class 2 - Generating PDF report with Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1X6fSVfZC6d00BIW0UGTQ9ykJQreApgTV
"""

# installing the library needed to generate pdf reports
!pip install pdf_reports -q

# importing the other necessary libraries
import pandas as pd
from datetime import datetime
from pdf_reports import pug_to_html, write_report

"""Importing the files - `"control_de_abacates.xlsx"` and `"modelo_relatorio.pug"` into the colab environment. This last file will be our **standard template** for generating the report in pdf"""

# loading the database into the variable "sales_abacates"
sales_abacates = pd.read_excel('controle_de_abacates.xlsx')

# viewing the first 10 lines of the file
sales_abacates.head(10)

# extracting the current date, with the "datetime" function with the "datetime.now (). date ()" commands 
# and the result instantiating in the "today" variable
today = datetime.now().date()

# viewing the result stored in the "today" variable
print(today)

# creating a variable named "html" to generate our report 
# and then we will use the "pug_to_html" function and passing our model with an argument
html = pug_to_html('modelo_de_relatorio.pug', 
                   planilha = sales_abacates,
                   hoje = today)

# viewing the "html" variable
html

# now it is necessary to export this html to a pdf file
# for that, we will use the function "write_report"
write_report(html, 'controle_abacates_relatorio_01.pdf')

"""if it is necessary to update the report due to a new file. Just run the above commands step by step.

For a practical example we will use the file `"controle_abacates_atualizado.xlsx"`.

**Let's see how it works!**
"""

# loading the database into the variable "sales_abacates"
new_sales = pd.read_excel('controle_de_abacates_atualizado.xlsx')

# viewing the first 10 lines of the file
new_sales.head(10)

# extracting the current date, with the "datetime" function with the "datetime.now (). date ()" commands 
# and the result instantiating in the "today" variable
today = datetime.now().date()

# viewing the result stored in the "today" variable
print(today)

# creating a variable named "html" to generate our report 
# and then we will use the "pug_to_html" function and passing our model with an argument
html = pug_to_html('modelo_de_relatorio.pug', 
                   planilha = new_sales,
                   hoje = today)

# viewing the "html" variable
html

# now it is necessary to export this html to a pdf file
# for that, we will use the function "write_report"
write_report(html, 'controle_abacates_relatorio_02.pdf')