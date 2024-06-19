import xlsxwriter
import os

class P003_Create_Table:
    def __init__(self):
        self.caminho_arquivo = "C:\\"
        self.planilha = xlsxwriter.Workbook(self.caminho_arquivo)
        self.sheet1 = self.planilha.add_worksheet()

    def T01_write_headers(self):
        self.sheet1.write("A1", "Valor Dólar")
        self.sheet1.write("B1", "Euro")

    def T02_write_values(self, DolarValue, EuroValue):
        self.sheet1.write("A2", DolarValue)
        self.sheet1.write("B2", EuroValue)

    def T03_close_and_open(self):
        self.planilha.close()
        os.startfile(self.caminho_arquivo)