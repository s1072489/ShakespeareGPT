# Script to clean up training data from Project Gutenberg

import re


with open("shakespeare_dataset.txt", 'r+', encoding="utf8") as file:
    text = file.read()

    # Remove indentations at start of lines
    text = re.sub(r'^[ \t]+', '', text, flags=re.MULTILINE)
    
    # Remove tags []
    text = re.sub(r'\[.*?\]', '', text)
        
    # Remove ACT _ lines
    text = re.sub(r'^ACT\s+[IVXLCDM]+\s*$', '', text, flags=re.MULTILINE)
    # text = re.sub(r'^Actus.*$', '', text, flags=re.MULTILINE)
        
    # Remove SCENE _ lines
    text = re.sub(r'^SCENE\s+([IVXLCDM]+\.)?\s*.*$', '', text, flags=re.MULTILINE)
    text = re.sub(r'^SCENE:.*\n', '', text)
    # text = re.sub(r'^Scaena\s+([IVXLCDM]+\.)?\s*.*$', '', text, flags=re.MULTILINE)

    # Remove NAME.\n lines (speakers)
    text = re.sub(r'^[A-Z\s]+?\.\n', '', text, flags=re.MULTILINE)

    # Remove ENTER directions
    text = re.sub(r'^ENTER.*\n', '', text)
    text = re.sub(r'^Enter.*\n', '', text)

    # Remove excessive newlines
    text = re.sub(r'\n\n\n', '\n\n', text)

    # Update file
    file.seek(0)
    file.write(text)
    file.truncate()    
