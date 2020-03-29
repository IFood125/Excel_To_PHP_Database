#For situations where excel CVS format doesn't work
import xlrd 
  
# Give the location of the file 
loc = (r'YOUR EXCEL FILE PATH HERE') 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0)
#Please be sure that all values entered are text
for i in range(1,sheet.nrows):
    a=[]
    for k in range(sheet.ncols):
        a += [sheet.cell_value(i, k)]
    a = tuple(a)
    #Populate fields
    #Separate each column like so
    #(`column1` ,`column2`, etc.....)
    #include %s up to the number of columns you have
    #you may also insert default values for certain columns
    print("INSERT INTO `YOUR_DATABASE_NAME` (`POPULATE WITH COLUMNS HERE`) VALUES ('%s', '%s');" % a) 
