# 💰 Expense Tracker

A Python terminal app to track daily expenses, view category
breakdowns, and export data to CSV.

## Features
- Add expenses with amount, category, description and date
- View all expenses sorted by date
- Category-wise summary with percentage bar chart
- Monthly summary (total, average, transaction count)
- Delete expenses
- Export all expenses to CSV (open in Excel!)
- Saves data automatically to a JSON file

## Categories
Food · Travel · Shopping · Bills · Entertainment · Other

## How to Run
```bash
python expense_tracker.py
```

## Example
💰 EXPENSE TRACKER

Add expense
View all expenses
Category summary
Monthly summary
Delete expense
Export to CSV
Exit

Choose an option (1-7): 3
CATEGORY SUMMARY
Travel          ₹ 1200.00  ████████████ 60.0%

Bills           ₹  450.00  ████ 22.5%

Food            ₹  350.00  ███ 17.5%
Total           ₹ 2000.00

## What I Learned
- Working with the datetime module
- Grouping and aggregating data (similar to Pandas groupby)
- Exporting data to CSV format
- Sorting data using lambda functions
- Calculating percentages and building text-based charts

## Tech Used
- Python 3
- json module (built-in)
- datetime module (built-in)
- csv format (built-in)
