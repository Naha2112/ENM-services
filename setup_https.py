#!/usr/bin/env python3
import http.server
import ssl
import socketserver
import os
import subprocess

def setup_https_server():
    # Generate self-signed certificate if it doesn't exist
    if not os.path.exists('cert.pem') or not os.path.exists('key.pem'):
        print("Generating self-signed certificate...")
        subprocess.run([
            'openssl', 'req', '-x509', '-newkey', 'rsa:4096', 
            '-keyout', 'key.pem', '-out', 'cert.pem', '-days', '365', '-nodes',
            '-subj', '/C=US/ST=State/L=City/O=ENM\'S SERVICES/CN=localhost'
        ], check=True)
    
    # Create HTTPS server
    PORT = 8443
    Handler = http.server.SimpleHTTPRequestHandler
    
    with socketserver.TCPServer(('', PORT), Handler) as httpd:
        context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        context.load_cert_chain('cert.pem', 'key.pem')
        httpd.socket = context.wrap_socket(httpd.socket, server_side=True)
        
        print(f"🔒 HTTPS Server running on port {PORT}")
        print(f"🌐 Visit: https://localhost:{PORT}")
        print("⚠️  You'll need to accept the security warning for the self-signed certificate")
        print("🛑 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n👋 Server stopped")

if __name__ == "__main__":
    setup_https_server() 