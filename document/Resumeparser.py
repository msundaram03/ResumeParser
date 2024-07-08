import json
import PyPDF2

def parse_resume_to_json(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfFileReader(file)
        content = ""
        for page_num in range(reader.numPages):
            page = reader.getPage(page_num)
            content += page.extract_text()
    
    # A simple and generic example of parsing
    lines = content.split('\n')
    resume_dict = {
        "Name": lines[0].strip(),
        "Education": [],
        "Skills": [],
        "Experience": [],
        "Projects": [],
        "Certifications": []
    }
    
    current_section = None
    
    for line in lines[1:]:
        line = line.strip()
        if "EDUCATION" in line:
            current_section = "Education"
        elif "SKILLS" in line:
            current_section = "Skills"
        elif "EXPERIENCE" in line:
            current_section = "Experience"
        elif "PROJECTS" in line:
            current_section = "Projects"
        elif "CERTIFICATIONS" in line:
            current_section = "Certifications"
        elif current_section and line:
            resume_dict[current_section].append(line)
    
    return json.dumps(resume_dict, indent=4)

# Example usage
pdf_path = 'Resume.pdf'
json_output = parse_resume_to_json(pdf_path)
print(json_output)
