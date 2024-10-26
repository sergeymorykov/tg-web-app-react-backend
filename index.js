
const token = '7866617284:AAHDOfPQJdKmufOdRgFza6XA8ZWRHPeA_Yc';
const signUpUrl = 'https://sergeymorykov-tg-web-app-react-72ec.twc1.net/signup';
const webAppUrl = 'https://sergeymorykov-tg-web-app-react-72ec.twc1.net';
const TelegramBot = require('node-telegram-bot-api');

// Create a bot that uses 'polling' to fetch new updates
const bot = new TelegramBot(token, {polling: true});

function checkUsersPresence(chatId) {
  let presence = false;

  // Check if user is already registered

  return presence;
}

bot.on('message', (msg) => {
  const chatId = msg.chat.id;
  if (checkUsersPresence(chatId)) {
    const opts = {
      reply_markup: {
        // keyboard: [
        inline_keyboard: [
          [{ text: 'Open profile', web_app: {url: webAppUrl} }, // change the url
            { text: 'Open events', web_app: {url: webAppUrl} } // change the url
          ]
        ]
      }
    };
    bot.sendMessage(chatId, 'It seems, that You are already registered', opts);
  } else {
    bot.sendMessage(chatId, 'We don\'t know you. Please, use /start');
  }
});


bot.onText(/\/start/, (msg) => {
  const opts = {
    reply_markup: {
      // keyboard: [
      inline_keyboard: [
        [{ text: 'Sign up', web_app: {url: signUpUrl} }]
      ]
    }
  };

  console.log(`User's id is ${msg.from.id}`);
  bot.sendMessage(msg.chat.id, 'Please, sign up', opts);
});
