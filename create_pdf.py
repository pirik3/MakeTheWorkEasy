from fpdf import FPDF
import pathlib
from os.path import join
import pandas as pd

class PDF(FPDF):
    def __init__(self):
        super(PDF, self).__init__()
        self.set_font("Arial", size=8)
        # NEW
        self.page_width = self.w - 2 * 1.5 #how much it is up to you
        self.epw = self.page_width / 3
    
    def create_table_from_rows(self, rows):
        once = True
        line_height = self.font_size * 1.5
        col_width = self.epw / 2

        #self.add_page() #add a new page before creating the table

        for row in rows:
            for datum in row:
                if datum != None:
                    if once:
                        self.set_fill_color(230, 230, 230)
                        self.multi_cell(col_width, line_height, datum, border=1, fill=True)
                    else:
                        self.multi_cell(col_width, line_height, datum, border=1)
                col_width = self.epw 
            once = False
            col_width = self.epw
            self.ln(line_height)
        
    # Page footer
    def footer(self):
        # Position at 1.5 cm from bottom
        self.set_y(-15)
        # Arial italic 8
        self.set_font('Arial', '', 8)
        # Page number
        self.cell(0, 10, '©VELOCITY Rüzgar Enerji Servisleri Sanayi ve Tic.A.S.', 0, 0, 'L')
        self.set_x(self.l_margin)
        self.cell(0, 10, 'Page' + str(self.page_no()) + '/{nb}', 0, 0, 'R')
        
    def header(self):
        self.set_x(-15)
        # Arial italic 8
        self.set_font('Arial', '', 8)
        # Page number
        self.set_text_color(255,0,0)
        self.cell(0, 10, 'Confidential' , 0, 0, 'R')
        self.set_y(self.l_margin)
        self.cell(10, 10, 'Confidential' , 0, 0, 'L')
        
    def page1(self):
        ##Page 1
        data = ("Authors(s)", "Inspection Company", "Report ID")
        pdf.add_page()
        pdf.image(r"C:\Users\pirik3\Pictures\pr.png", 0,20,210)

        pdf.set_font('Arial', 'B', 22)
        pdf.cell(0, 180, 'Velocity Findings Report' , 0, 0, 'C')
        pdf.set_xy(30,190)
        pdf.set_font('Arial', 'B', 15)
        #pdf.create_table_from_rows((['Author(s)','Inspection Company','Report ID'],))
        epw = pdf.w - pdf.l_margin

        
    def page2(self):
        ##Page 2
        pdf.add_page()
        
    def table(self):
        try:
            self.add_page()
            self.set_font('Times', '', 10.0)
            epw = pdf.w - pdf.l_margin
            col_width = epw/5
            data1 = [{'ip': '192.168.0.1', 'name': 'cloud', 'used_percent': 100.0,'percent': 100.0,'value':6497693752875},
                     {'ip': '192.168.0.2', 'name': 'mitakaDZGFGASSCCGSTHAG', 'used_percent': 97.0, 'percent': 100.0, 'value':6497693752875597265917}]
            df = pd.DataFrame(data1)
            s = df['ip']
            v = df['name']
            c = df['used_percent']
            d = df['percent']
            e = df['value']
            data = [df,[s[0], v[0], c[0], d[0],e[0]], [s[1], v[1], c[1], d[1], e[1]]]
            th = pdf.font_size
            count = 0
            self.set_text_color(0, 0, 0)
            self.set_fill_color(255, 255, 255)
            for row in data:
                count += 1
                for datum in row:
                    if count == 1:
                        self.set_fill_color(70, 130, 180)
                        self.set_font('Times', '', 10)
                        self.cell(col_width, 2*th, str(datum), border=1, align='L', fill=1)
                    else:
                        self.set_font('Times', '', 11)
                        self.multi_cell(col_width, 2*th, str(datum), border=1, align='L', fill=0)
                self.ln(2 * th)
            self.ln(2* th)
        except Exception as e:
            print(f"Exception {e}")

# Instantiation of inherited class
pdf = PDF()
pdf.alias_nb_pages()
pdf.page1()
pdf.page2()
pdf.table()
pdf.output('tuto2.pdf', 'F')
