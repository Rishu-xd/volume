{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9gGITX51c1gXg9Vf9QnGU",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/Rishu-xd/volume/blob/main/Untitled17.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "aJS5AD5AHpps",
        "outputId": "bd33f68f-7def-4841-cc75-9987a9f12269"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting pyTelegramBotAPI\n",
            "  Downloading pytelegrambotapi-4.25.0-py3-none-any.whl.metadata (48 kB)\n",
            "\u001b[?25l     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/48.1 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K     \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m48.1/48.1 kB\u001b[0m \u001b[31m2.1 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hRequirement already satisfied: requests in /usr/local/lib/python3.10/dist-packages (from pyTelegramBotAPI) (2.32.3)\n",
            "Requirement already satisfied: charset-normalizer<4,>=2 in /usr/local/lib/python3.10/dist-packages (from requests->pyTelegramBotAPI) (3.4.0)\n",
            "Requirement already satisfied: idna<4,>=2.5 in /usr/local/lib/python3.10/dist-packages (from requests->pyTelegramBotAPI) (3.10)\n",
            "Requirement already satisfied: urllib3<3,>=1.21.1 in /usr/local/lib/python3.10/dist-packages (from requests->pyTelegramBotAPI) (2.2.3)\n",
            "Requirement already satisfied: certifi>=2017.4.17 in /usr/local/lib/python3.10/dist-packages (from requests->pyTelegramBotAPI) (2024.8.30)\n",
            "Downloading pytelegrambotapi-4.25.0-py3-none-any.whl (269 kB)\n",
            "\u001b[?25l   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m0.0/269.2 kB\u001b[0m \u001b[31m?\u001b[0m eta \u001b[36m-:--:--\u001b[0m\r\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m269.2/269.2 kB\u001b[0m \u001b[31m8.9 MB/s\u001b[0m eta \u001b[36m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: pyTelegramBotAPI\n",
            "Successfully installed pyTelegramBotAPI-4.25.0\n"
          ]
        }
      ],
      "source": [
        "!pip install pyTelegramBotAPI"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import telebot\n",
        "from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton\n",
        "\n",
        "# Replace 'YOUR_BOT_API_TOKEN' with your bot's API token\n",
        "API_TOKEN = '7160413938:AAGT0KjtuV9727c0sdBgFxCwE2cdELJsBVs'\n",
        "bot = telebot.TeleBot(API_TOKEN)\n",
        "\n",
        "# To store user data\n",
        "user_data = {}\n",
        "\n",
        "# To track user actions\n",
        "user_states = {}\n",
        "\n",
        "# Start command handler\n",
        "@bot.message_handler(commands=['start'])\n",
        "def send_welcome(message):\n",
        "    chat_id = message.chat.id\n",
        "    user_states[chat_id] = {\"action\": None}  # Reset user action\n",
        "\n",
        "    # Create inline buttons for Login and Register\n",
        "    markup = InlineKeyboardMarkup()\n",
        "    markup.row_width = 2\n",
        "    markup.add(\n",
        "        InlineKeyboardButton(\"Login\", callback_data=\"login\"),\n",
        "        InlineKeyboardButton(\"Register\", callback_data=\"register\")\n",
        "    )\n",
        "\n",
        "    bot.send_message(\n",
        "        chat_id,\n",
        "        \"Welcome! Please choose an option:\",\n",
        "        reply_markup=markup\n",
        "    )\n",
        "\n",
        "# Callback handler for button clicks\n",
        "@bot.callback_query_handler(func=lambda call: True)\n",
        "def handle_callback_query(call):\n",
        "    chat_id = call.message.chat.id\n",
        "    if call.data == \"register\":\n",
        "        user_states[chat_id][\"action\"] = \"register_username\"\n",
        "        bot.send_message(chat_id, \"Enter a username to register:\")\n",
        "    elif call.data == \"login\":\n",
        "        user_states[chat_id][\"action\"] = \"login_username\"\n",
        "        bot.send_message(chat_id, \"Enter your username to login:\")\n",
        "\n",
        "# Handle user input for login and registration\n",
        "@bot.message_handler(func=lambda message: user_states.get(message.chat.id, {}).get(\"action\") is not None)\n",
        "def handle_user_input(message):\n",
        "    chat_id = message.chat.id\n",
        "    action = user_states[chat_id][\"action\"]\n",
        "\n",
        "    if action == \"register_username\":\n",
        "        username = message.text\n",
        "        if username in user_data:\n",
        "            bot.send_message(chat_id, \"Username already registered. Try a different one.\")\n",
        "        else:\n",
        "            user_states[chat_id][\"temp_username\"] = username\n",
        "            user_states[chat_id][\"action\"] = \"register_password\"\n",
        "            bot.send_message(chat_id, \"Username is available! Now enter a password:\")\n",
        "\n",
        "    elif action == \"register_password\":\n",
        "        password = message.text\n",
        "        username = user_states[chat_id].pop(\"temp_username\")\n",
        "        user_data[username] = {\"password\": password}\n",
        "        user_states[chat_id][\"action\"] = None\n",
        "        bot.send_message(chat_id, \"Registration successful! You can now login.\")\n",
        "\n",
        "    elif action == \"login_username\":\n",
        "        username = message.text\n",
        "        if username in user_data:\n",
        "            user_states[chat_id][\"temp_username\"] = username\n",
        "            user_states[chat_id][\"action\"] = \"login_password\"\n",
        "            bot.send_message(chat_id, \"Username found! Enter your password:\")\n",
        "        else:\n",
        "            bot.send_message(chat_id, \"Username not registered. Please register first.\")\n",
        "            user_states[chat_id][\"action\"] = None\n",
        "\n",
        "    elif action == \"login_password\":\n",
        "        password = message.text\n",
        "        username = user_states[chat_id].pop(\"temp_username\")\n",
        "        if user_data[username][\"password\"] == password:\n",
        "            user_states[chat_id][\"action\"] = None\n",
        "            bot.send_message(chat_id, \"Login successful! Here are your links:\")\n",
        "            send_links(chat_id)\n",
        "        else:\n",
        "            bot.send_message(chat_id, \"Incorrect password. Please try again.\")\n",
        "            user_states[chat_id][\"action\"] = None\n",
        "\n",
        "# Function to send links after successful login\n",
        "def send_links(chat_id):\n",
        "    markup = InlineKeyboardMarkup()\n",
        "    markup.row_width = 2  # Number of buttons per row\n",
        "    markup.add(\n",
        "        InlineKeyboardButton(\"Google\", url=\"https://www.google.com\"),\n",
        "        InlineKeyboardButton(\"YouTube\", url=\"https://www.youtube.com\"),\n",
        "        InlineKeyboardButton(\"GitHub\", url=\"https://github.com\"),\n",
        "        InlineKeyboardButton(\"Telegram\", url=\"https://telegram.org\")\n",
        "    )\n",
        "    bot.send_message(\n",
        "        chat_id,\n",
        "        \"Click any of the links below:\",\n",
        "        reply_markup=markup\n",
        "    )\n",
        "\n",
        "# Polling to keep the bot running\n",
        "print(\"Bot is running...\")\n",
        "bot.infinity_polling()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "iM2Y7cWIKyHB",
        "outputId": "13285a04-77e8-4ae8-df24-e86743561af8"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Bot is running...\n"
          ]
        },
        {
          "output_type": "stream",
          "name": "stderr",
          "text": [
            "2024-12-13 18:04:33,504 (__init__.py:1121 MainThread) ERROR - TeleBot: \"Infinity polling: polling exited\"\n",
            "ERROR:TeleBot:Infinity polling: polling exited\n",
            "2024-12-13 18:04:33,508 (__init__.py:1123 MainThread) ERROR - TeleBot: \"Break infinity polling\"\n",
            "ERROR:TeleBot:Break infinity polling\n"
          ]
        }
      ]
    }
  ]
}