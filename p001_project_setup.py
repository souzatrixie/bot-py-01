from p002_get_values import P002_Get_Values
from p003_create_table import P003_Create_Table

class P001_Project_Setup:
    
    DolarValue, EuroValue = P002_Get_Values()
    P003_Create_Table(DolarValue, EuroValue)