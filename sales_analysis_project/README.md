Simple Sales Visualizer

This is a simple project to analyze sales data using Python.

Everything is written manually with short variable names, lots of spacing for clarity, and no functions used.  
The code focuses on being easy to read and understand.

------------------------------------------

How I Made It

- I used Python with pandas, matplotlib, and seaborn libraries.
- I wrote the code by hand, line by line, in a personal style.
- No shortcuts, no functions, no auto-formatting.
- Variable names are kept short (like df, avg, grp).
- Brackets are used everywhere for consistency.
- Each logical part of the code is spaced out to make it more readable.

------------------------------------------

Files Included

1. sales_data.csv — the sample dataset containing product, category, sales, and profit
2. sales_analysis.py — the main Python file that runs all the logic and visuals
3. processed_sales_data.csv — output file generated after running the script
4. README.md — this file

------------------------------------------

Requirements

You need to have Python 3 installed.

You also need these Python libraries:
- pandas
- matplotlib
- seaborn

You can install them by running this:

pip install pandas matplotlib seaborn

------------------------------------------

How To Run The Project

1. Make sure Python 3 is installed on your system
2. Download all the files and place them in one folder
3. Open a terminal or command prompt in that folder
4. Run the following command:

   python sales_analysis.py

5. The script will:
   - Print the first few rows of data
   - Calculate and print the average sales
   - Show a bar chart (average sales per category)
   - Show a scatter plot (sales vs profit)
   - Show a heatmap (correlation between numeric values)
   - Save a new CSV file with processed data

------------------------------------------

What This Project Does

- Reads and displays sample sales data
- Calculates the average sales
- Shows visual insights using basic graphs
- Saves the data to a new file for further use

------------------------------------------

Created by Vignesh Durishetty
Free to use, share, or change.
