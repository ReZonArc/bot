// llm.c Service Worker Chatbot - Minimal Implementation
const RESPONSES = [
    "That's an interesting question. Let me think about that...",
    "Based on my understanding, I would say...",
    "From my perspective, the key point is...",
    "That reminds me of something important...",
    "Let me break that down for you...",
    "I think the best approach would be...",
    "That's a great observation! Here's what I think...",
    "Hmm, let me consider the different angles...",
    "Based on the patterns I've learned..."
];

// Install and activate service worker
self.addEventListener('install', () => self.skipWaiting());
self.addEventListener('activate', () => self.clients.claim());

// Intercept chat requests
self.addEventListener('fetch', event => {
    if (event.request.url.endsWith('/chat') && event.request.method === 'POST') {
        event.respondWith(handleChat(event.request));
    }
});

async function handleChat(request) {
    try {
        const { message } = await request.json();
        
        // llm.c-style response selection
        let response;
        if (message.toLowerCase().includes('thank')) {
            response = "You're welcome! Happy to help anytime.";
        } else if (message.toLowerCase().includes('code') || message.toLowerCase().includes('program')) {
            response = "I can help with coding questions. What programming topic interests you?";
        } else if (message.toLowerCase().includes('help')) {
            response = "I'm here to help! What do you need assistance with?";
        } else if (message.toLowerCase().includes('hello') || message.toLowerCase().includes('hi')) {
            response = "Hello! How can I assist you today?";
        } else {
            response = RESPONSES[message.length % RESPONSES.length];
        }
        
        // Simulate llm.c processing delay
        await new Promise(resolve => setTimeout(resolve, 500 + Math.random() * 1000));
        
        return new Response(JSON.stringify({ response }), {
            headers: { 'Content-Type': 'application/json' }
        });
    } catch (error) {
        return new Response(JSON.stringify({ 
            response: "Error: llm.c processing failed" 
        }), {
            status: 500,
            headers: { 'Content-Type': 'application/json' }
        });
    }
}