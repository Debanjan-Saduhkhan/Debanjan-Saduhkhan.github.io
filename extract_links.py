import PyPDF2
import re

def extract_publication_links(pdf_path):
    try:
        reader = PyPDF2.PdfReader(pdf_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        
        # Extract publications with their links
        publications = []
        
        # Split by lines and look for publications
        lines = text.split('\n')
        
        for i, line in enumerate(lines):
            # Look for publications with links
            if '(Link)' in line or 'DOI:' in line or 'http' in line:
                # Get the full publication context
                context_start = max(0, i-2)
                context_end = min(len(lines), i+3)
                context = lines[context_start:context_end]
                
                # Find the actual publication title
                pub_text = ' '.join(context)
                
                # Extract DOI if present
                doi_match = re.search(r'DOI:\s*([^\s,]+)', pub_text)
                doi = doi_match.group(1) if doi_match else None
                
                # Extract any URLs
                url_match = re.search(r'http[s]?://[^\s]+', pub_text)
                url = url_match.group(0) if url_match else None
                
                publications.append({
                    'text': pub_text,
                    'doi': doi,
                    'url': url,
                    'has_link': '(Link)' in pub_text
                })
        
        return publications
    except Exception as e:
        print(f"Error: {e}")
        return []

if __name__ == "__main__":
    pubs = extract_publication_links("Debanjan_Resume_2025 copy.pdf")
    
    print("=== PUBLICATIONS WITH LINKS ===")
    for i, pub in enumerate(pubs, 1):
        print(f"\n--- Publication {i} ---")
        print(f"Text: {pub['text'][:200]}...")
        print(f"DOI: {pub['doi']}")
        print(f"URL: {pub['url']}")
        print(f"Has Link: {pub['has_link']}")
        print("-" * 50) 