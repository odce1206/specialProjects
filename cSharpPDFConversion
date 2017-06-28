using System;
using System.IO;
using System.Diagnostics;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.UI;
using System.Web.UI.WebControls;
using PdfSharp;
using PdfSharp.Pdf.IO;
using PdfSharp.Pdf;
using PdfSharp.Drawing;
using SelectPdf;
using System.Drawing;
using System.Drawing.Printing;


namespace pdfMerge
{
    public partial class _default : System.Web.UI.Page {

        protected void Page_Load(object sender, EventArgs e) {
            htmlAPDF();
            List<string> filePDFs = new List<string>();
            string[] arrayPDFPOutput = Directory.GetFiles(@"C:\Users\pee.ti3\Desktop", "testOutput.pdf");
            string[] arrayPDF = Directory.GetFiles(@"C:\Users\pee.ti3\Downloads", "*.pdf");
            filePDFs.AddRange(arrayPDFPOutput); 
            filePDFs.AddRange(arrayPDF);
            string[] arrayFinal = filePDFs.ToArray();
            MergePDFs(@"C:\Users\pee.ti3\desktop\factursFinal.pdf", arrayFinal);
            File.Delete(@"C:\Users\pee.ti3\Desktop\testOutput.pdf");
            Response.Clear();
            string filePath = @"C:\Users\pee.ti3\desktop\factursFinal.pdf";
            Response.ContentType = "application/pdf";
            Response.WriteFile(filePath);
            Response.End();
            
        }
        //protected void btnOK_Click(object sender, EventArgs e) {
        //    Process p = new Process();
        //    p.StartInfo = new ProcessStartInfo()
        //    {
        //        CreateNoWindow = true,
        //        Verb = "print",
        //        FileName = @"C:\Users\pee.ti3\desktop\pedf122.pdf" //put the correct path here
        //    };
        //    p.Start();
        //}

        //public void pd_PrintPage(object sender, PrintPageEventArgs e)
        //{
        //    string labelPath = ((PrintDocument)sender).DocumentName;
        //    e.Graphics.DrawImage(new Bitmap(labelPath), 0, 0);
        //}


        public static void htmlAPDF() {
            // -------- Convertir HTML de solicitudes a PDF --------
            HtmlToPdf converter = new HtmlToPdf();
            // convert the url to pdf 
            SelectPdf.PdfDocument doc = converter.ConvertUrl("http://cablesmtymxdev2/scripts/cgiip.exe/WService=xcmsafin/Flujo_FM_qad2011/comp_otras.w?DomainCode=MFGCMSA&ref=155506&num_sistema=11&h_sesion=1098541&global_user=0000136&entidad=2000");
            // save pdf document 
            doc.Save(@"C:\Users\pee.ti3\Desktop\testOutput.pdf");
            // close pdf document 
            doc.Close();
        }

        public static void MergePDFs(string targetPath, params string[] pdfs) {
            // -------- Unir todos los PDFs de la ruta en uno solo --------
            using (PdfSharp.Pdf.PdfDocument targetDoc = new PdfSharp.Pdf.PdfDocument()) {
                foreach (string pdf in pdfs) {
                    using (PdfSharp.Pdf.PdfDocument pdfDoc = PdfReader.Open(pdf, PdfDocumentOpenMode.Import)) {
                        for (int i = 0; i < pdfDoc.PageCount; i++) {
                            targetDoc.AddPage(pdfDoc.Pages[i]);
                        }
                    }
                }
                targetDoc.Save(targetPath);
            }


        }

        

    }
}
