import PyPDF2
import re

def extract_papers_from_pdf(pdf_path):
    try:
        reader = PyPDF2.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        # Look for research papers and publications
        lines = text.split('\n')
        papers = []
        
        for i, line in enumerate(lines):
            # Look for common paper patterns
            if any(keyword in line.lower() for keyword in ['paper', 'publication', 'conference', 'journal', 'acm', 'ieee', 'cikm', 'icml', 'neurips', 'aaai', 'ijcai', 'kdd', 'www', 'sigir']):
                # Get context (previous and next lines)
                context_start = max(0, i-3)
                context_end = min(len(lines), i+4)
                context = lines[context_start:context_end]
                papers.append('\n'.join(context))
        
        return papers, text
    except Exception as e:
        print(f"Error: {e}")
        return [], ""

if __name__ == "__main__":
    papers, full_text = extract_papers_from_pdf("Debanjan_Resume_2025 copy.pdf")
    
    print("=== RESEARCH PAPERS FOUND ===")
    for i, paper in enumerate(papers, 1):
        print(f"\n--- Paper {i} ---")
        print(paper)
        print("-" * 50)
    
    print("\n=== FULL TEXT (for manual search) ===")
    print(full_text) 