# Telegram Asyncio Bot

This project is a simple Telegram bot built using Python's `asyncio` library and the `aiogram` framework. It serves as an example of how to create a bot that can handle various commands and messages asynchronously.

## Project Structure

```
telegram-asyncio-bot
├── src
│   ├── bot.py          # Entry point for the bot
│   ├── handlers        # Contains message and command handlers
│   │   └── __init__.py
│   └── utils           # Utility functions for the bot
│       └── __init__.py
├── requirements.txt    # Project dependencies
├── README.md           # Project documentation
└── pyproject.toml      # Project configuration
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd telegram-asyncio-bot
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Set up your Telegram bot by talking to [BotFather](https://t.me/botfather) and obtaining your bot token.

4. Update the bot token in `src/bot.py`.

## Usage

To run the bot, execute the following command:
```
python src/bot.py
```

## Features

- Handles `/start` command to welcome users.
- Processes incoming messages and replies accordingly.
- Supports callback queries for inline buttons.

## Contributing

Feel free to submit issues or pull requests for improvements or bug fixes.