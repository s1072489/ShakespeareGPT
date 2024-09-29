import os
import re

# Fix files
for filename in os.listdir("cleaned"):
	filepath = os.path.join("cleaned", filename)
	
	with open(os.path.join('cleaned', filename), "r+", encoding="utf-8") as f:
		text = f.read()

		# Remove excessive whitespaces
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)
		text = re.sub(r'  ', ' ', text)

		# Update file
		f.seek(0)
		f.write(text)


		f.truncate()    


# Make main file
for filename in os.listdir("cleaned"):
	filepath = os.path.join("cleaned", filename)
	
	with open(os.path.join('cleaned', filename), "r", encoding="utf-8") as f:
		text = f.read()

		with open("large_dataset.txt", 'a', encoding="utf-8") as dataset:
			dataset.write(text+"<|endoftext|>")
