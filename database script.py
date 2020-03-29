import xlrd 
  
# Give the location of the file 
loc = (r'C:\Users\Franky Jiang\Documents\Workspace\AndroidChallenge.xlsx') 
  
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(0) 
sheet.cell_value(0, 0) 
for i in range(1,sheet.nrows):
    a=[]
    for k in range(sheet.ncols):
        a += [sheet.cell_value(i, k)]
    a = tuple(a)
    print("INSERT INTO `labs` (`id`, `Title`, `latitude`, `longitude`, `address`, `city`, `country`, `created_at`, `updated_at`) VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', NULL, NULL);" % a) 
