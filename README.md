
This tool takes input folder path and lists out all the input files in the given folder. Those input files are
loaded in the code and generated target file. A new column is added in the target file which has values of Insert(I), Update(U) and Delete(D). 

Steps to generate the target.xlsx file:

1. To run the code, 
git clone https://github.com/hariniavd/Exercise1.git

2. And then run "python main.py"
Make sure you have python installed in the system.

3. If any error raises to install pandas/openpyxl run the above commands:
pip install pandas
pip install openpyxl



Libraries Used in the feature:

1. pandas:

Pandas is an open source Python package that is most widely used for data science/data analysis and machine learning tasks. It is built on top of another package named Numpy, which provides support for multi-dimensional arrays.

I have used this library for performing calculations on XL sheets. Pandas gives quicker solutions and calcuates millions of data in very less time. Performance wise, pandas is most considerable library for fast results.

2. openpyxl:

The Openpyxl library is used to write or read the data in the excel file and many other tasks. An excel file that we use for operation is called Workbook that contains a minimum of one Sheet and a maximum of tens of sheets.
