# Install and update spaCy
!pip install -U spacy

# Download the english language model
!python -m spacy download en

# Import required packages
import spacy
from spacy import displacy
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import pandas as pd