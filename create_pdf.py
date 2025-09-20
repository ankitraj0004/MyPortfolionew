from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.platypus import Paragraph, Spacer, Image
from reportlab.lib.units import inch
import os

def create_cv():
    # Create a PDF document
    c = canvas.Canvas("ANKIT_CV.pdf", pagesize=letter)
    width, height = letter
    
    # Set up styles
    styles = getSampleStyleSheet()
    title_style = ParagraphStyle(
        'Title',
        parent=styles['Heading1'],
        fontSize=24,
        spaceAfter=20,
        alignment=TA_CENTER
    )
    
    heading_style = ParagraphStyle(
        'Heading2',
        parent=styles['Heading2'],
        fontSize=16,
        spaceAfter=10,
        textColor='#4f46e5',
        spaceBefore=20
    )
    
    normal_style = styles['Normal']
    
    # Add content
    title = Paragraph("<b>ANKIT KUMAR MANJHI</b>", title_style)
    title.wrapOn(c, width-100, height)
    title.drawOn(c, 50, height-100)
    
    # Contact Information
    contact = [
        "Email: akankitraj04@gmail.com",
        "Phone: +91 9471242674",
        "Location: Paniora, Khordha, India"
    ]
    
    y_position = height - 150
    for line in contact:
        p = Paragraph(line, normal_style)
        p.wrapOn(c, width-100, 50)
        p.drawOn(c, 50, y_position)
        y_position -= 20
    
    # Add a line
    c.line(50, y_position-20, width-50, y_position-20)
    
    # Add Education Section
    edu = Paragraph("<b>EDUCATION</b>", heading_style)
    edu.wrapOn(c, width-100, 50)
    edu.drawOn(c, 50, y_position-50)
    
    education = [
        "<b>Bachelor of Technology in Computer Science</b>",
        "Gandhi Institute For Technology, Bhubaneswar",
        "2021 - 2025 | CGPA: 8.5/10"
    ]
    
    y_position -= 70
    for line in education:
        p = Paragraph(line, normal_style)
        p.wrapOn(c, width-100, 50)
        p.drawOn(c, 50, y_position)
        y_position -= 15
    
    # Add Skills Section
    skills = Paragraph("<b>SKILLS</b>", heading_style)
    skills.wrapOn(c, width-100, 50)
    skills.drawOn(c, 50, y_position-30)
    
    skill_list = [
        "• Programming: Python, JavaScript, Java",
        "• Web Development: HTML, CSS, React, Node.js",
        "• Database: MySQL, MongoDB",
        "• Tools: Git, VS Code, Postman"
    ]
    
    y_position -= 50
    for skill in skill_list:
        p = Paragraph(skill, normal_style)
        p.wrapOn(c, width-100, 50)
        p.drawOn(c, 50, y_position)
        y_position -= 15
    
    c.save()
    print("CV PDF generated successfully!")

if __name__ == "__main__":
    create_cv()
