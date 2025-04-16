🤖FinBot — Telegram Financial Assistant
FinBot is a lightweight Telegram bot developed using Python. It is designed to help users manage their personal finances through categorization of income and expenses, budget tracking, and financial summaries. The bot utilizes simple command-based interactions and stores user data locally in CSV format for ease of use and transparency.

#Features
1.Configuration of income and budgets by categories

2.Logging of income and expense transactions

3.Generation of financial summaries and balance reports

4.Notification system (turn on/turn out)

5.Persistent data storage using CSV files

#Command | Description✔️
/start | Initiates interaction with the bot
/help | Provides a list of available commands and details
/config | Allows users to configure income and budgets
/log | Records a new income or expense entry
/summary | Displays a summary of financial activity
/notifyon | Enables notifications (feature under development)
/notifyoff | Disables notifications

#Example of using FinBot
![Снимок экрана 2025-04-15 222608](https://github.com/user-attachments/assets/dbc25de9-3065-4e99-9fb9-909f43e6429c) 
![Снимок экрана 2025-04-15 222632](https://github.com/user-attachments/assets/8b43aeab-1ac0-4a04-8617-20058e27b251)
![Снимок экрана 2025-04-15 222647](https://github.com/user-attachments/assets/ba8925c7-f1f7-452c-ab80-31e06ec23c57) 
![Снимок экрана 2025-04-15 222659](https://github.com/user-attachments/assets/0b2d23bb-82aa-46aa-b2d0-8372b023b8c5) 

#Installation:
To run the bot locally, follow the steps below:

Ensure you have Python installed (preferably version 3.8 or later).

Clone this repository or download the source files.

Navigate to the project directory and install dependencies:
📍pip install -r requirements.txt

Launch the bot:
📍python bot.py
❗Make sure to insert your valid Telegram Bot Token in the bot.py file.

#File Structure
finbot/
├── bot.py              # Main bot logic
├── config.py           # Income and budget configuration
├── log.py              # Logging income and expenses
├── notifications.py    # Notification system (upcoming)
├── data/               # Directory for CSV user data
├── screenshots/        # Demonstration images
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation





