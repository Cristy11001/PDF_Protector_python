import pypdf
import sys
import os

def protect_pdf(input_file, output_file, password):
    """
    Add password protection to a PDF file
    """
    try:
        # Check if input file exists
        if not os.path.exists(input_file):
            print(f"Error: File {input_file} not found")
            return False
        
        print(f"Reading PDF: {input_file}")
        
        # Open and process the PDF
        with open(input_file, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            pdf_writer = pypdf.PdfWriter()
            
            # Copy all pages
            for page in pdf_reader.pages:
                pdf_writer.add_page(page)
            
            # Add password protection
            pdf_writer.encrypt(user_password=password, use_128bit=True)
            
            # Save protected PDF
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)
        
        print(f"✓ Protected PDF created: {output_file}")
        print(f"✓ Password: {password}")
        return True
        
    except Exception as e:
        print(f"Error: {e}")
        return False

def check_protection(pdf_file):
    """
    Check if PDF is password protected
    """
    try:
        with open(pdf_file, 'rb') as file:
            pdf_reader = pypdf.PdfReader(file)
            
            if pdf_reader.is_encrypted:
                print(f"✓ {pdf_file} is password protected")
            else:
                print(f"✗ {pdf_file} is not password protected")
                
    except Exception as e:
        print(f"Error checking protection: {e}")

def main():
    """
    Main function - handle command line arguments
    """
    if len(sys.argv) < 2:
        print("PDF Protection Tool")
        print("Usage:")
        print("  python pdf_tool.py protect <input.pdf> <output.pdf> <password>")
        print("  python pdf_tool.py check <file.pdf>")
        print()
        print("Examples:")
        print("  python pdf_tool.py protect document.pdf protected.pdf mypassword")
        print("  python pdf_tool.py check document.pdf")
        return
    
    action = sys.argv[1]
    
    if action == "protect":
        if len(sys.argv) != 5:
            print("Usage: python pdf_tool.py protect <input.pdf> <output.pdf> <password>")
            return
        
        input_pdf = sys.argv[2]
        output_pdf = sys.argv[3]
        password = sys.argv[4]
        
        # Use different filenames
        if input_pdf == output_pdf:
            print("Error: Input and output files cannot be the same!")
            print("Use different filenames, e.g.:")
            print(f"python pdf_tool.py protect {input_pdf} {input_pdf.replace('.pdf', '_protected.pdf')} {password}")
            return
            
        protect_pdf(input_pdf, output_pdf, password)
    
    elif action == "check":
        if len(sys.argv) != 3:
            print("Usage: python pdf_tool.py check <file.pdf>")
            return
        
        pdf_file = sys.argv[2]
        check_protection(pdf_file)
    
    else:
        print("Unknown action. Use 'protect' or 'check'")

if __name__ == "__main__":
    main()
