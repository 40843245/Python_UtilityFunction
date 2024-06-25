from elements import Elements

import os 
import csv
import pandas
import numpy
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages

class FileHandler():

    class Path():
        @staticmethod
        def get_fullpath(directory,filename,filename_ext):
            if os.path.exists(directory) != True:
                raise ValueError('The '+directory+' does NOT find_one_check_exist.')
            if os.path.isdir(directory) != True:
                raise ValueError('The '+directory+' is NOT a directory.')
            fullfilename = os.path.join(directory,filename + filename_ext)
            return fullfilename
        
    class Writer():
      @staticmethod
      def get_fullpath(fullfilename,data:str):
        with open(fullfilename,'w') as file:
            file.write(str(data))
    
      @staticmethod 
      def write_csv_file(fullfilename,fields:list ,data:list[dict]):
        with open(fullfilename, 'w') as csvfile:
            # creating a csv dict writer object
            writer = csv.DictWriter(csvfile, fieldnames=fields)
            # writing headers (field names)
            writer.writeheader()
            # writing data rows
            writer.writerows(data)

      @staticmethod 
      def write_html_file_by_pandas(fullfilename,fields:list ,data:list[dict]):
        with open(fullfilename, 'w') as file:
            # arr = numpy.array(data)
            dataframe = pandas.DataFrame(data=data,columns=fields,index=None,dtype=None)
            dataframe.to_html(file)
            
      @staticmethod
      def write_pdf_file_by_matplotlib(fullfilename,fields:list ,data:list[dict]):
        df = pandas.DataFrame(data, columns = fields)

        #https://stackoverflow.com/questions/32137396/how-do-i-plot-only-a-table-in-matplotlib
        (fig, ax) =plt.subplots(figsize=(12,4))
        ax.axis('tight')
        ax.axis('off')
        my_table = ax.table(cellText=df.values,colLabels=df.columns,loc='center')

        #https://stackoverflow.com/questions/4042192/reduce-left-and-right-margins-in-matplotlib-plot
        pp = PdfPages(fullfilename)
        pp.savefig(fig, bbox_inches='tight')
        pp.close()
            
    class Reader():       
      @staticmethod
      def read_txt_file(fullfilename:str):
        if os.path.exists(fullfilename) != True:
            raise ValueError('The '+fullfilename+' does NOT find_one_check_exist.')
        if os.path.isfile(fullfilename) != True:
            raise ValueError('The '+fullfilename+' is NOT a file.')
        file = open(fullfilename, 'r')
        data = file.read()
        file.close()
        return data
             
      @staticmethod
      def read_csv_file_by_pandas(fullfilename:str):
        if os.path.exists(fullfilename) != True:
            raise ValueError('The '+fullfilename+' does NOT find_one_check_exist.')
        if os.path.isfile(fullfilename) != True:
            raise ValueError('The '+fullfilename+' is NOT a file.')     
        csv_data = pandas.read_csv(fullfilename,index_col=False)
        csv_data.reset_index(drop=True,inplace=True)
        if Elements.is_empty(src=csv_data) == True:
            raise ValueError('csv_data can NOT be null or empty.')  
        return csv_data
    
      @staticmethod
      def read_csv_file_as_json_by_pandas(fullfilename:str):
        csv_data = FileHandler.Reader.read_csv_file_by_pandas(fullfilename=fullfilename)
        json_data = csv_data.to_json()
        return json_data
        
      @staticmethod
      def read_csv_file_by_csv_reader(fullfilename:str,):
        if os.path.exists(fullfilename) != True:
            raise ValueError('The '+fullfilename+' does NOT exist.')
        if os.path.isfile(fullfilename) != True:
            raise ValueError('The '+fullfilename+' is NOT a file.')
        
        file = open(fullfilename,'r') 
        csv_data =csv.reader(file, delimiter=',')
        if Elements.is_empty(src=csv_data) == True:
            raise ValueError('csv_data can NOT be null or empty.')        
        return csv_data

    class Converter():
        @staticmethod
        def csv_to_html_by_pandas(fullfilename:str,dest_fullfilepath:str):
            if os.path.exists(fullfilename) != True:
                raise ValueError('The '+fullfilename+' does NOT find_one_check_exist.')
            if os.path.isfile(fullfilename) != True:
                raise ValueError('The '+fullfilename+' is NOT a file.')
            if fullfilename.endswith('.csv') != True:
                raise ValueError('The '+fullfilename+' is NOT a .csv file.')
            if dest_fullfilepath.endswith('.html') != True:
                raise ValueError('The '+dest_fullfilepath+' is NOT a .html file.')
            csv_data = pandas.read_csv(fullfilename) 
            csv_data.to_html(dest_fullfilepath)  

if __name__ == '__main__':
    json_data = [{'_id': '666f9cdfc7751f196775c1b4', 'username': 'username1', 'accountname': 'accountn', 'email_name': 'jayw711k@gmail.com', 'password_name': 'password1', 'active': 'True', 'filename_ext': 'csv'}]
    fields = list(json_data[0].keys())
    print(fields)
    fullfilename = 'C:\\Users\\40843\\flask_projects\\tax_site\\output\\1.pdf'
    FileHandler.Writer.write_pdf_file_by_matplotlib(fullfilename=fullfilename,fields=fields,data=json_data)

