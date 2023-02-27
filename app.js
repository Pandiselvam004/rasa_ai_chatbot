const socket = io.connect('http://localhost:5005', { transports: ['websocket'] });

socket.on('bot_uttered', (message) => {
    // Handle the bot's response
    // ...
});

socket.emit('user_uttered', { text: 'Hello, World!' });
