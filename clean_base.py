import xml.etree.ElementTree as ET
from html import unescape
import os
import re


def get_text(element):
    text = ''
    if element.text:
        text += unescape(element.text).strip()
    for child in element:
        if child.tail:
            text += unescape(child.tail).strip()
    
    return text

def parse_dialogue(xml_file):
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Find all dialogue elements
   # Find the parent element containing dialogues
    dialogue_parent = root.find('.//dialogueText')

    # Initialize variables
    current_line = ''
    result = []
    last_was_speech = False

    # Process each child element of the dialogue parent
    for child in dialogue_parent:
        if child.tag == 'dialogue':
            text = get_text(child)
            
            if text:
                # Add the dialogue text to the current line
                current_line += ' ' + text if current_line else text
                
                last_was_speech = True
        elif child.tag == 'nonSpeech':
            # If we've encountered a new speaker, append the current line and reset
            if current_line:
                result.append(re.sub(r'\n', ' ', current_line.strip())
)
                current_line = ''
                
            last_was_speech = False

    # Append the last line if it exists
    if current_line:
        result.append(current_line.strip())


    return '\n'.join(result)

# Apply to all text files in a directory
for filename in os.listdir("base_dataset"):
    filepath = os.path.join("base_dataset", filename)
    
    try:
        with open(os.path.join('cleaned', f'{re.sub('.xml', '', filename)}.txt'), "w", encoding="utf-8") as f:
            f.write(parse_dialogue(filepath))
    except UnicodeDecodeError:
        pass
    except Exception as error:
        print(f"Error when parsing {filename}")
        print(error)
        pass
