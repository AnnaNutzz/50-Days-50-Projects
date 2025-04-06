"""
Data extraction from any excel sheet
For my own Quality of Life
"""

import pandas as pd
import numpy as np


"""
faculty finding for project
"""

# Load the Excel sheet
sheet_data = pd.read_excel("D:/Coding/Python/50 days 50 projects/files for codes/faculties_project.xlsx")

# Clean column names by stripping whitespace (if any)
sheet_data.columns = sheet_data.columns.str.strip()

# Relevant topics for the project focus
relevant_topics = [
    "AI", "Machine Learning", "Deep Learning", "Natural Language Processing",
    "Education Technology", "Generative adversarial networks", "Education",
    "Assistive Technology", "Convolution neural network", "Generative AI"
]

# Function to check if any relevant topic matches in a row
def match_relevant_topics(row):
    # Check for topics from 'Topic 1' to 'Topic 4'
    topics = [row[f"Topic {i}"] for i in range(1, 5)]
    return any(topic for topic in topics if pd.notna(topic) and topic in relevant_topics)

# Filter rows where any relevant topic matches
filtered_professors = sheet_data[sheet_data.apply(match_relevant_topics, axis=1)]

# Select the top 50 professors, prioritize by the most matching topics
top_professors = filtered_professors.head(20)

# Display the selected professors
print(top_professors[["Sr. No.", "Name", "Cabin/Cubical Number", "Topic 1", "Topic 2", "Topic 3", "Topic 4"]])
