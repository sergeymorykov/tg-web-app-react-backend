
const token = '7866617284:AAHDOfPQJdKmufOdRgFza6XA8ZWRHPeA_Yc';
const webAppUrl = 'https://sergeymorykov-tg-web-app-react-72ec.twc1.net/signup';
const TelegramBot = require('node-telegram-bot-api');
const { onWebAppEvent } = require('./events/event');

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, {polling: true});

bot.on('message', (msg) => {
  const chatId = msg.chat.id;

  bot.sendMessage(chatId, 'Received your message');
});

bot.onText(/\/start/, (msg) => {
  const opts = {
    reply_markup: {
      inline_keyboard: [
        [{ text: 'Sign up', web_app: {url: webAppUrl} }]
      ]
    }
  };
  bot.sendMessage(msg.chat.id, 'Please, sign up', opts);
});



// bot.onText(/\/start/, (msg) => {
//   const opts = {
//     reply_markup: {
//       keyboard: [
//         [
//           { text: 'Sign up', web_app: {url: webAppUrl} }
//         ]
//       ]
//     }
//   };
//   bot.sendMessage(msg.chat.id, 'Select from menu', opts);
// });
