const chatBox = document.getElementById('chat-box');
const userInput = document.getElementById('user-input');
const chatForm = document.getElementById('chat-form');

function appendMessage(message, type) {
    const msgDiv = document.createElement('div');
    msgDiv.textContent = message;
    msgDiv.className = type === 'user' ? 'user-msg' : 'ai-msg';
    chatBox.appendChild(msgDiv);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// Função para enviar mensagem
async function sendMessage(message) {
    appendMessage(message, 'user');
    userInput.value = '';

    try {
        const response = await fetch('/chat', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ message })
        });

        if (!response.ok) throw new Error('Network response not ok');

        const data = await response.json();
        appendMessage(data.response, 'ai');

    } catch (err) {
        appendMessage('Error: ' + err.message, 'ai');
    }
}

chatForm.addEventListener('submit', function(e) {
    e.preventDefault();

    const message = userInput.value.trim();
    if (!message) return;

    sendMessage(message);
});