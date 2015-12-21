from xhtml2pdf import pisa
from jinja2 import Template
import os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def convertHtmlToPdf(data, sourceHtml, outputFilename):
    resultFile = open(outputFilename, "w+b")
    
    template = Template(open(os.path.join(base_dir, sourceHtml)).read())
    html  = template.render(data)
    
    pisaStatus = pisa.CreatePDF(
            html,
            dest=resultFile)
    resultFile.close()
    return pisaStatus.err

if __name__=="__main__":
    pisa.showLogging()
    convertHtmlToPdf(data, sourceHtml, outputFilename)