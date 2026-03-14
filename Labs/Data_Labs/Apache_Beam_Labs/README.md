# Lab: Data Processing with Apache Beam
## Project Overview
In this lab, I built a data pipeline using Apache Beam (Python SDK) to process and analyze multiple text files. The goal was to take raw, unstructured text and transform it into a meaningful dataset by counting the frequency of every word used across different documents.

## What I Did
Environment Setup: Configured a Python environment and installed the apache_beam library.

Data Ingestion: Programmatically downloaded two different public text files (Project Gutenberg eBooks) into a local directory.

Pipeline Construction: Built a data processing pipeline that:

Read multiple files simultaneously using file patterns.

Tokenized the text into individual words using Regular Expressions.

Normalized the data by converting all text to lowercase.

Aggregated the results using a MapReduce style logic (Pairing words with 1 and summing them by key).

Data Output: Formatted the final counts into a readable string and saved them as partitioned text files.

## Key Learnings (Apache Beam)
Through this lab, I gained hands-on experience with the following core concepts:
The Pipeline Object: I learned that a Pipeline represents the entire sequence of data processing steps, from reading the data to writing the output.
PCollections: I worked with PCollections, which are specialized data sets that Apache Beam can process in parallel. I learned that they are immutable; you don't change them, you transform them into new ones.
PTransforms: I applied various transformations to move data through the pipeline:
ReadFromText: To bring data into the system.
FlatMap: To turn one input (a line of text) into many outputs (individual words).
Map: To perform a 1-to-1 transformation on each element.
CombinePerKey: To perform mathematical aggregations efficiently.
DirectRunner: I used the DirectRunner to execute the pipeline locally on my machine, which is essential for testing and debugging before scaling to a cloud-based runner like Google Cloud Dataflow.
Data Normalization: I practiced "cleaning" data within a pipeline by handling case-sensitivity, ensuring that my data science analysis is accurate and consistent.

## How to Run
To replicate this lab, ensure you have Apache Beam installed:

Bash
pip install apache-beam
Then, execute the Python script (Script.py) to see the combined word counts in the /outputs folder.