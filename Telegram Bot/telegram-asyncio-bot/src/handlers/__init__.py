def handle_start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome! Use /help to see available commands.")

def handle_message(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="You said: " + update.message.text)

def handle_callback_query(update, context):
    query = update.callback_query
    context.bot.answer_callback_query(callback_query_id=query.id, text="You clicked: " + query.data)