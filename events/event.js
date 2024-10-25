
module.exports = {
  reply_markup: {
    inline_keyboard: [
      [
        { text: 'View Events', callback_data: 'view_events' }
      ],
      [
        { text: 'Register for Event', callback_data: 'register_event' }
      ],
      [
        { text: 'Add New Event', callback_data: 'add_event' }
      ]
    ]
  }
};
