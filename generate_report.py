import pandas as pd
from fpdf import FPDF

# Load and analyze data
def analyze_data(file_path):
    """Read data from a CSV file and perform basic analysis."""
    try:
        data = pd.read_csv(file_path)
        numeric_data = data.select_dtypes(include='number')  # Only numeric columns
        summary = numeric_data.describe()  # Summary statistics for numeric columns
        return data, summary
    except FileNotFoundError:
        print("Error: File not found.")
        return None, None

# Generate PDF report
class PDFReport(FPDF):
    def header(self):
        self.set_font("Arial", "B", 14)
        self.cell(0, 10, "Automated Data Report", align="C", ln=True)
        self.ln(10)

    def footer(self):
        self.set_y(-15)
        self.set_font("Arial", "I", 8)
        self.cell(0, 10, f"Page {self.page_no()}", align="C")

    def add_section(self, title, content):
        self.set_font("Arial", "B", 12)
        self.cell(0, 10, title, ln=True)
        self.ln(5)
        self.set_font("Arial", "", 10)
        self.multi_cell(0, 10, content)
        self.ln(5)

def generate_report(data, summary, output_file):
    """Generate a PDF report with data analysis."""
    pdf = PDFReport()
    pdf.add_page()

    # Add introduction
    pdf.add_section("Introduction", "This report provides an analysis of the provided data.")

    # Add summary statistics
    pdf.add_section("Summary Statistics", summary.to_string())

    # Save the report
    pdf.output(output_file)
    print(f"Report generated: {output_file}")

# Main function
if __name__ == "__main__":
    # Path to the CSV file
    input_file = "d:/1/programing languages/codetech/task2/data.csv"  # Replace with your CSV file name
    output_file = "report.pdf"

    # Analyze data
    data, summary = analyze_data(input_file)

    if data is not None and summary is not None:
        # Generate PDF report
        generate_report(data, summary, output_file)
