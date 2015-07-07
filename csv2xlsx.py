import os
import glob
import csv
import argparse
from xlsxwriter.workbook import Workbook

def arguments():

    parser = argparse.ArgumentParser()
    parser.add_argument('--path', default = os.getcwd(), help = "Path to CSV files")
    parser.add_argument('--outname', default = None, help = "Name of output XLSX file") 
    return parser.parse_args()

def wrap_csvs(csvpath, outname):
   
    directory_path = os.path.abspath(csvpath)
    
    if outname is None:
        filename = os.path.basename(directory_path + ".xlsx")
    else:
        filename = outname

    workbook_name = os.path.join(directory_path, filename)
    workbook = Workbook(workbook_name)

    for c in glob.glob(os.path.join(csvpath, "*.csv")):
        sheetname = os.path.basename(c[:c.rfind(".")])
        print("Adding {} to {}".format(c, workbook_name)) 
        worksheet = workbook.add_worksheet(sheetname)
    
        with open(c, 'r') as f:
            reader = csv.reader(f)
        
            for rindex, row in enumerate(reader):
                for cindex, col in enumerate(row):
                    try:
                        worksheet.write(rindex,cindex, float(col))
                    except ValueError:
                        worksheet.write(rindex, cindex, col)

    workbook.close()

def main():

    args = arguments()
    wrap_csvs(args.path, args.outname)

if __name__ == "__main__":
    main()
