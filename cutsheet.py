import os
import csv

class CSV_Wrapper:
    """
    
    Parameters:
        path:
        header:
        summary:
        columns:

    Attributes:
       lines:
       path:
       header:
       summary:
       columns:
       writer: 
    """
    
    def __init__(self, path, header="", summary="", columns=[]):
        self.lines = []
        self.output_rows = []
        self.path = path 
        self.header = header
        self.summary = summary
        self.columns = columns
        self.writer = None

    def set_header(self, header):
        """
        Sets the  
        
        Parameters:
            header (str):

        """
        self.header = header

    def set_summary(self, summary):
        """
        Sets the  
        
        Parameters:
            summary (str):

        """
        self.summary = summary

    def set_path(self, path):
        """
        Sets the  
        
        Parameters:
            path (str):

        """
        self.path = path
    
    def add_columns(self, columns):
        """
        
        Parameters:
            columns (:obj:`list` of :obj:`str`)
        
        """
        assert isinstance(columns, (list,tuple))
        self.columns += columns

    def add_column(self, column: str):
        """
        
        Parameters:
            column (str)
        
        """
        self.columns.append(new_column)

    def add_data(self, *data):
        """
        
        Parameters:
            *data: 
        """
        assert len(data) > 0:
        for arg in data:
            assert isinstance(arg, (list, tuple))
       self.lines += list(zip(*data))

    def write(self):
        """
        """
        with open(self.path, 'w+') as file_obj:
            output_rows = []
            output_rows += [ self.header ] if self.header else []
            output_rows += [ self.summary ] if self.summary else []
            output_rows += columns 
            output_rows += self.lines
            self.writer = csv.writer(file_obj)
            self.writer.writerows(output_rows)
