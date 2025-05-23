document.addEventListener('DOMContentLoaded', function() {
    const readMoreButtons = document.querySelectorAll('.read-more-btn');
    
    readMoreButtons.forEach(button => {
        button.addEventListener('click', function() {
            const projectDiv = this.closest('.project');
            const isExpanded = projectDiv.classList.contains('expanded');
            
            projectDiv.classList.toggle('expanded');
            this.textContent = isExpanded ? 'Read More' : 'Read Less';
        });
    });
});

function formatResponse(text) {
    // Add line breaks
    text = text.replace(/\n/g, '<br>');
    
    // Format lists
    if (text.includes('•')) {
        const items = text.split('•').filter(item => item.trim());
        text = '<ul>' + items.map(item => `<li>${item.trim()}</li>`).join('') + '</ul>';
    }
    
    // Wrap paragraphs
    if (!text.includes('<ul>')) {
        const paragraphs = text.split('<br><br>');
        text = paragraphs.map(p => `<p>${p}</p>`).join('');
    }
    
    return text;
}

async function sendMessage(event) {
    event.preventDefault();
    const input = document.getElementById('message');
    const messages = document.getElementById('messages');
    
    if (!input.value.trim()) return;
    
    messages.innerHTML += `
        <div class="message user-message">
            ${input.value}
        </div>`;
    
    try {
        const response = await fetch('/api/chat', {
            method: 'POST',
            headers: { 
                'Content-Type': 'application/json',
                'Accept': 'application/json'
            },
            body: JSON.stringify({ question: input.value })
        });
        
        if (!response.ok) {
            throw new Error(`HTTP error! status: ${response.status}`);
        }
        
        const data = await response.json();
        messages.innerHTML += `
            <div class="message bot-message">
                ${formatResponse(data.response)}
            </div>`;
    } catch (error) {
        console.error('Error:', error);
        messages.innerHTML += `
            <div class="message bot-message error">
                Sorry, I couldn't process your request. Error: ${error.message}
            </div>`;
    }
    
    messages.scrollTop = messages.scrollHeight;
    input.value = '';
}

function toggleChat() {
    const chatWindow = document.getElementById('chatWindow');
    const chatToggle = document.querySelector('.chat-toggle');
    
    if (chatWindow.style.display === 'flex') {
        chatWindow.style.display = 'none';
        chatToggle.style.display = 'flex';
    } else {
        chatWindow.style.display = 'flex';
        chatToggle.style.display = 'none';
    }
}