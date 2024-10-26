
const token = '7866617284:AAHDOfPQJdKmufOdRgFza6XA8ZWRHPeA_Yc';
const webAppUrl = 'https://sergeymorykov-tg-web-app-react-72ec.twc1.net/signup';
const TelegramBot = require('node-telegram-bot-api');

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'Received your message');
});

bot.onText(/\/change/, (msg) => {
  const opts = {
    reply_markup: {
      inline_keyboard: [
        [{ text: 'Change user info', callback_data: 'change_user_info' }]
      ]
    }
  };

  bot.sendMessage(msg.chat.id, 'Please, change your user info', opts);
});

bot.onText(/\/start/, (msg) => {
  const opts = {
    reply_markup: {
      // keyboard: [
      inline_keyboard: [
        [{ text: 'Sign up', web_app: {url: webAppUrl} }]
      ]
    }
  };

  console.log(`User's id is ${msg.from.id}`);
  bot.sendMessage(msg.chat.id, 'Please, sign up', opts);
});
