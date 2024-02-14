from prettytable import PrettyTable

class DisplayFormatter(object):
    
    @staticmethod
    def display_table(data, fields):
        """
        Display a list of dictionaries as a table on the console with selected fields.
        Parameters:
        - data: List of dictionaries
        - fields: List of selected fields to display
        """
        if not data or not fields:
            print("Data or fields cannot be empty.")
            return
        
        # Create a PrettyTable instance
        table = PrettyTable(fields)

        # Add rows to the table
        for row in data:
            table.add_row([row[field] for field in fields])

        # Print the table
        print(table)