# llm.c Service Worker Chatbot

A minimal implementation of an llm.c-inspired chatbot using service workers with the least amount of code possible.

## Features

- **Minimal Code**: Complete chatbot in just 3 files (~8KB total)
- **Service Worker**: Background processing for chat responses  
- **Retro Terminal UI**: Matrix-style green-on-black interface
- **Context Awareness**: Keyword-based response selection
- **No Dependencies**: Pure HTML, CSS, and JavaScript

## Usage

1. Start the server:
   ```bash
   python3 server.py
   ```

2. Open http://localhost:8000 in your browser

3. Chat with the llm.c-inspired bot!

## Files

- `index.html` - Chat interface with service worker registration (2.6KB)
- `sw.js` - Service worker with llm.c-style response logic (2.3KB)
- `server.py` - HTTP server with POST endpoint support (3.0KB)

**Total: 7.9KB** for a complete chatbot with service worker architecture.

## Architecture

The chatbot uses a hybrid approach:
1. **Service Worker** registers for background processing
2. **Server fallback** handles chat requests when SW isn't available
3. **Minimal UI** provides immediate feedback
4. **Context detection** for intelligent responses

![Chatbot Demo](https://github.com/user-attachments/assets/6666799c-d1dd-4e7c-a750-8c95f1b3ab37)