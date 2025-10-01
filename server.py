#!/usr/bin/env python3
import http.server
import socketserver
import os
import json
import random
import time

PORT = 8000

class Handler(http.server.SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=os.path.dirname(os.path.realpath(__file__)), **kwargs)
    
    def do_POST(self):
        if self.path == '/chat':
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            
            try:
                data = json.loads(post_data.decode('utf-8'))
                message = data.get('message', '')
                
                # Simple llm.c-like responses
                responses = [
                    "That's an interesting question. Let me think about that...",
                    "Based on my understanding, I would say...",
                    "From my perspective, the key point is...",
                    "That reminds me of something important...",
                    "Let me break that down for you...",
                    "I think the best approach would be...",
                    "That's a great observation! Here's what I think...",
                    "Hmm, let me consider the different angles...",
                    "Based on the patterns I've learned..."
                ]
                
                # Context-aware responses (order matters - most specific first)
                if 'thank' in message.lower():
                    response = "You're welcome! Happy to help anytime."
                elif 'code' in message.lower() or 'program' in message.lower():
                    response = "I can help with coding questions. What programming topic interests you?"
                elif 'help' in message.lower():
                    response = "I'm here to help! What do you need assistance with?" 
                elif 'hello' in message.lower() or 'hi' in message.lower():
                    response = "Hello! How can I assist you today?"
                else:
                    response = responses[len(message) % len(responses)]
                
                # Simulate processing delay
                time.sleep(0.5 + random.random())
                
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.send_header('Access-Control-Allow-Origin', '*')
                self.end_headers()
                self.wfile.write(json.dumps({'response': response}).encode())
                
            except Exception as e:
                self.send_response(500)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                self.wfile.write(json.dumps({'response': 'Error processing message'}).encode())
        else:
            self.send_response(404)
            self.end_headers()

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Serving llm.c chatbot at http://localhost:{PORT}")
    httpd.serve_forever()