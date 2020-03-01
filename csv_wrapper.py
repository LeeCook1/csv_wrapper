import os
import csv

class CSV_Wrapper:
    """
    Parameters:
        columns (List[str], optional): The columns are the columns for the csv and is
            alwasys the first row if exist

        header (str, optional): The header that should be at the top of the csv

        path (str): The location the csv should exist
        
        summary (str, optional): The text that should exist right below the header and 
            before the columns
        

    Attributes:
        columns (List[str]): The columns for the csv and is always the first 
            row if exist
        
        header (str): The header that should be at the top of the csv

        lines (List[str]): A list of the row lines excluding the header,
            summary, and columns
        
        path (str): The location of the csv if it exist, else None

        summary (str): The summary is the text that should exist right below
            the header and before the columns

    Functions:
        add_columns
        add_column
        add_data
        get_output
        set_header
        set_path
        set_summary
        write
    """
    
    def __init__(self, path=None, header="", summary="", columns=[]):
        self._output_rows = []
        self.lines = []
        self.path = self._check_path(path)
        self.header = header
        self.summary = summary
        self.columns = columns
        self._writer = None

    def set_header(self, header):
        """
        Sets the :attribute `header` with :param `header` 
        
        Parameters:
            header (str): The header that should be at the top of the csv

        """
        self.header = header

    def set_summary(self, summary):
        """
        Sets the :attribute `summary` with :param `summary` 
        
        Parameters:
            summary (str): The summary is the text that should exist right below
                the header and before the columns

        """
        self.summary = summary

    def set_path(self, path):
        """
        Sets the :attribute `path` with :param `path` 
        
        Parameters:
            path (str): The location of the csv if it exist, else None

        """
        self.path = self._check_path(path)
    
    def add_columns(self, columns):
        """
        Adds a list of column  names :param `columns` to the columns list that 
        will be display in the in the csv

        Parameters:
            columns (:obj:`list` of :obj:`str`)
        
        """
        assert isinstance(columns, (list,tuple))
        self.columns += columns

    def add_column(self, column: str):
        """
        Adds a new column name to the columns that will be listed on the in the csv
        
        Parameters:
            column (str)
        
        """
        self.columns.append(new_column)

    def add_data(self, *data):
        """
        Adds data that will be placed in the csv. Expects all parameters to be 
        a list or tuple. If one parameter is given, it will be stored as a
        row. If multiple parameters are given, the same index inside each 
        parameters' list will be combined and placed in a row.

        Parameters:
            *data: Variable parameter, each with :type `List`

        Examples:
            add_data(["a","b","c"])
                ### HEADER ###
                ### SUMMARY ###
                ### COLUMNS ###
                <Row 1>: a,b,c

            add_data(["a","b","c"], ["1","2","3"],["cat","dog"])
                ### HEADER ###
                ### SUMMARY ###
                ### COLUMNS ###
                <Row 1>: a,1,cat
                <Row 2>: b,2,dog
                <Row 3>: c,3


        """
        assert len(data) > 0:
        for arg in data:
            assert isinstance(arg, (list, tuple))
        self.lines += list(zip(*data))
    
    def display(self):
        """
        Displays the output that will be written to the csv
        
        """
        print(self._get_output())

    def _get_output(self):
        """
        Gets the output that will be written to the csv

        Returns:
            str: returns the output that will be written to the csv
        """
        if not self._output_rows: self._create_output() 
        return "\n".join(self._output_rows) if self._output_rows or ""

    def write(self):
        """
        Writes the output to the csv. If no file path passed, it will write to stdout.

        """
        self._create_output()
        file_obj = open(self.path, 'w+') if self.path else sys.stdout
        self.writer = csv.writer(file_obj)
        if self._output_rows:
            self.writer.writerows(self._output_rows) 
        if file_obj != sys.stdout: file_obj.close()

    def _check_path(self, path):
        """
        Checks :param `path` to see if it has a valid directory. If not, sets 
        path to None

        Parameters:
            path (str): The csv location

        Returns:
            str: If the path directory is valid, returns :param `path` else None
        
        """
        if path is None:
            return None
        elif not os.path.isdir(path):
            print("Directory for {} don't exist".format(path)) # Error
            return None
        return path

    def _create_output(self):
        """
        Creates the output from the attributes `header`, `summary`, `columns`, and `lines`.

        """
        output_rows = []
        output_rows += [ self.header ] if self.header else []
        output_rows += [ self.summary ] if self.summary else []
        output_rows += columns 
        output_rows += self.lines
        self._output_rows = output_rows
    
        
