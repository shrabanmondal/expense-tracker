# 💰 CLI Expense & Budget Tracker

A lightweight, robust command-line utility built in Python to help individuals track their daily expenses, monitor category breakdowns, and stay within a set monthly budget without the bloat of heavy commercial apps.

## 🚀 Features

- **Budget Management:** Set a monthly spending limit with automatic warnings when exceeded.
- **Categorized Tracking:** Log expenses under custom categories (e.g., Food, Transport, Studies).
- **Instant Summaries:** View a clean text-based breakdown of total spending and category proportions.
- **CSV Export:** Export your entire expense log into a CSV file for spreadsheet analysis.
- **Local Persistence:** Automatically saves your data locally using JSON.

## 🛠️ Project Structure

```text
expense-tracker/
│
├── main.py         # Handles the command-line user interface
├── tracker.py      # Core logic and file handling functions
├── expenses.json   # Local database (auto-generated)
└── README.md       # Project documentation


