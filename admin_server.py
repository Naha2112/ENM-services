#!/usr/bin/env python3
import os
import shutil
import json
from datetime import datetime
import socketserver
import http.server
from urllib.parse import parse_qs, urlparse
import cgi

PORT = 8444  # Different port for admin
UPLOAD_DIR = "images"
ALLOWED_EXTENSIONS = {'.jpg', '.jpeg', '.png', '.webp', '.gif'}

class AdminHandler(http.server.SimpleHTTPRequestHandler):
    def do_POST(self):
        """Handle POST requests for file uploads"""
        if self.path == '/upload':
            self.handle_upload()
        elif self.path == '/update_carousel':
            self.handle_carousel_update()
        elif self.path == '/update_portfolio':
            self.handle_portfolio_update()
        else:
            self.send_error(404)
    
    def do_OPTIONS(self):
        """Handle CORS preflight requests"""
        self.send_response(200)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
    
    def do_GET(self):
        """Handle GET requests"""
        if self.path == '/api/images':
            self.send_image_list()
        elif self.path == '/api/carousel':
            self.send_carousel_config()
        else:
            # Serve files normally
            super().do_GET()
    
    def handle_upload(self):
        """Handle file upload"""
        try:
            # Parse the multipart form data
            form = cgi.FieldStorage(
                fp=self.rfile,
                headers=self.headers,
                environ={'REQUEST_METHOD': 'POST'}
            )
            
            uploaded_files = []
            
            # Get category
            category = form.getvalue('category', 'general')
            
            # Process uploaded files
            if 'files' in form:
                files = form['files']
                if not isinstance(files, list):
                    files = [files]
                
                for file_item in files:
                    if file_item.filename:
                        # Check file extension
                        filename = file_item.filename
                        file_ext = os.path.splitext(filename)[1].lower()
                        
                        if file_ext in ALLOWED_EXTENSIONS:
                            # Create safe filename with category prefix
                            base_name = os.path.splitext(filename)[0]
                            safe_filename = self.make_safe_filename(f"{category}-{base_name}{file_ext}")
                            file_path = os.path.join(UPLOAD_DIR, safe_filename)
                            
                            # Save file
                            with open(file_path, 'wb') as f:
                                f.write(file_item.file.read())
                            
                            uploaded_files.append(safe_filename)
                            print(f"✅ Uploaded: {safe_filename} (category: {category})")
            
            # Send response
            response = {
                'success': True,
                'uploaded_files': uploaded_files,
                'message': f'Successfully uploaded {len(uploaded_files)} files'
            }
            
            self.send_json_response(response)
            
        except Exception as e:
            print(f"❌ Upload error: {e}")
            self.send_json_response({
                'success': False,
                'error': str(e)
            }, status=500)
    
    def handle_carousel_update(self):
        """Handle carousel configuration update"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            # Save carousel configuration
            config = {
                'images': data.get('images', []),
                'title': data.get('title', 'Complete Home Renovation Projects'),
                'description': data.get('description', ''),
                'updated': datetime.now().isoformat()
            }
            
            with open('carousel_config.json', 'w') as f:
                json.dump(config, f, indent=2)
            
            print(f"✅ Carousel updated with {len(config['images'])} images")
            
            self.send_json_response({
                'success': True,
                'message': 'Carousel configuration updated successfully'
            })
            
        except Exception as e:
            print(f"❌ Carousel update error: {e}")
            self.send_json_response({
                'success': False,
                'error': str(e)
            }, status=500)
    
    def handle_portfolio_update(self):
        """Handle portfolio section updates"""
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length)
            data = json.loads(post_data.decode('utf-8'))
            
            category = data.get('category', 'general')
            images = data.get('images', [])
            action = data.get('action', 'add_to_category')
            
            # Update the main website's HTML file
            self.update_website_portfolio(category, images, action)
            
            # Update the JavaScript carousel collections
            self.update_carousel_collections(category, images)
            
            print(f"✅ Portfolio updated: {category} category with {len(images)} images")
            
            self.send_json_response({
                'success': True,
                'message': f'Portfolio updated for {category} category'
            })
            
        except Exception as e:
            print(f"❌ Portfolio update error: {e}")
            self.send_json_response({
                'success': False,
                'error': str(e)
            }, status=500)
    
    def update_website_portfolio(self, category, images, action):
        """Update the main website's portfolio section"""
        try:
            # Read the current index.html
            with open('index.html', 'r', encoding='utf-8') as f:
                html_content = f.read()
            
            # Create portfolio items for the new images
            portfolio_items = []
            for image in images:
                # Determine the display category name
                category_display = {
                    'bathroom': 'Bathroom Renovation',
                    'kitchen': 'Kitchen Renovation', 
                    'painting': 'Professional Painting',
                    'tiling': 'Tiling & Flooring',
                    'flooring': 'Flooring Installation',
                    'handyman': 'Handyman Services',
                    'carpentry': 'Carpentry Work'
                }.get(category, category.title())
                
                portfolio_item = f'''
                    <div class="portfolio-item" data-category="{category}">
                        <div class="portfolio-image">
                            <img src="images/{image}" alt="{category_display}" loading="lazy">
                        </div>
                        <div class="portfolio-info">
                            <h3>{category_display}</h3>
                            <p>Professional {category_display.lower()} completed to the highest standards</p>
                            <span class="portfolio-category">{category_display}</span>
                        </div>
                    </div>'''
                portfolio_items.append(portfolio_item)
            
            # Find the portfolio items grid section and add new items
            portfolio_items_grid = html_content.find('<div class="portfolio-items-grid">')
            if portfolio_items_grid != -1:
                # Find the comment inside the grid
                comment_start = html_content.find('<!-- Portfolio items will be added here by admin uploads -->', portfolio_items_grid)
                if comment_start != -1:
                    # Insert new portfolio items after the comment
                    comment_end = html_content.find('-->', comment_start) + 3
                    new_content = (html_content[:comment_end] + 
                                 '\n                        ' + 
                                 '\n                        '.join(portfolio_items) +
                                 html_content[comment_end:])
                    
                    # Write the updated HTML back
                    with open('index.html', 'w', encoding='utf-8') as f:
                        f.write(new_content)
                    
                    print(f"✅ Added {len(images)} portfolio items to website")
                    return True
            
            print("⚠️ Could not find portfolio items grid section in HTML")
            return False
            
        except Exception as e:
            print(f"❌ Error updating website portfolio: {e}")
            return False
    
    def update_carousel_collections(self, category, images):
        """Update the JavaScript carousel collections with new images"""
        try:
            # Read the current script.js
            with open('script.js', 'r', encoding='utf-8') as f:
                js_content = f.read()
            
            # Find the category in the categoryImages object
            category_key = f"'{category}': ["
            category_start = js_content.find(category_key)
            
            if category_start != -1:
                # Find the end of this category's array
                bracket_count = 0
                array_start = js_content.find('[', category_start)
                i = array_start
                
                while i < len(js_content):
                    if js_content[i] == '[':
                        bracket_count += 1
                    elif js_content[i] == ']':
                        bracket_count -= 1
                        if bracket_count == 0:
                            array_end = i
                            break
                    i += 1
                
                # Create new image objects for the carousel
                new_images = []
                for image in images:
                    category_display = {
                        'bathroom': 'Luxury Bathroom Renovation',
                        'kitchen': 'Professional Kitchen Refit',
                        'painting': 'Professional Painting',
                        'tiling': 'Expert Tiling Work',
                        'flooring': 'Quality Flooring Installation',
                        'handyman': 'Professional Handyman Services',
                        'carpentry': 'Expert Carpentry Work'
                    }.get(category, 'Professional Work')
                    
                    new_images.append(f"{{ src: 'images/{image}', alt: '{category_display}' }}")
                
                # Get existing array content
                existing_array = js_content[array_start+1:array_end]
                
                # Add new images to existing array
                if existing_array.strip():
                    updated_array = existing_array.rstrip() + ',\n            ' + ',\n            '.join(new_images)
                else:
                    updated_array = '\n            ' + ',\n            '.join(new_images) + '\n        '
                
                # Update the JavaScript content
                new_js_content = (js_content[:array_start+1] + 
                                updated_array + 
                                js_content[array_end:])
                
                # Write the updated JavaScript back
                with open('script.js', 'w', encoding='utf-8') as f:
                    f.write(new_js_content)
                
                print(f"✅ Updated carousel collections for {category}")
                return True
            
            print(f"⚠️ Could not find {category} category in carousel collections")
            return False
            
        except Exception as e:
            print(f"❌ Error updating carousel collections: {e}")
            return False
    
    def send_image_list(self):
        """Send list of available images"""
        try:
            if not os.path.exists(UPLOAD_DIR):
                os.makedirs(UPLOAD_DIR)
                print(f"📁 Created upload directory: {UPLOAD_DIR}")
            
            images = []
            try:
                for filename in os.listdir(UPLOAD_DIR):
                    file_path = os.path.join(UPLOAD_DIR, filename)
                    if os.path.isfile(file_path):
                        file_ext = os.path.splitext(filename)[1].lower()
                        if file_ext in ALLOWED_EXTENSIONS:
                            try:
                                stat = os.stat(file_path)
                                images.append({
                                    'filename': filename,
                                    'size': stat.st_size,
                                    'modified': datetime.fromtimestamp(stat.st_mtime).isoformat()
                                })
                            except OSError as e:
                                print(f"⚠️ Could not get stats for {filename}: {e}")
                                continue
            except OSError as e:
                print(f"⚠️ Could not list directory {UPLOAD_DIR}: {e}")
            
            self.send_json_response({
                'success': True,
                'images': images,
                'total_count': len(images)
            })
            
        except Exception as e:
            print(f"❌ Image list error: {e}")
            self.send_json_response({
                'success': False,
                'error': str(e),
                'images': []
            }, status=500)
    
    def send_carousel_config(self):
        """Send current carousel configuration"""
        try:
            if os.path.exists('carousel_config.json'):
                with open('carousel_config.json', 'r') as f:
                    config = json.load(f)
            else:
                # Default configuration (empty until images are uploaded)
                config = {
                    'images': [],
                    'title': 'Complete Home Renovation Projects',
                    'description': 'Upload your best work through the admin panel to showcase here'
                }
            
            self.send_json_response({
                'success': True,
                'config': config
            })
            
        except Exception as e:
            print(f"❌ Carousel config error: {e}")
            self.send_json_response({
                'success': False,
                'error': str(e)
            }, status=500)
    
    def send_json_response(self, data, status=200):
        """Send JSON response"""
        self.send_response(status)
        self.send_header('Content-type', 'application/json')
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.end_headers()
        
        response_json = json.dumps(data)
        self.wfile.write(response_json.encode('utf-8'))
    
    def make_safe_filename(self, filename):
        """Create a safe filename"""
        # Remove path components
        filename = os.path.basename(filename)
        
        # Replace spaces and special characters
        safe_chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789-_."
        safe_filename = ''.join(c if c in safe_chars else '_' for c in filename)
        
        # Add timestamp if file exists
        if os.path.exists(os.path.join(UPLOAD_DIR, safe_filename)):
            name, ext = os.path.splitext(safe_filename)
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            safe_filename = f"{name}_{timestamp}{ext}"
        
        return safe_filename

def setup_admin_server():
    """Setup and run the admin server"""
    print("🔧 Setting up Admin Server...")
    
    # Create upload directory if it doesn't exist
    if not os.path.exists(UPLOAD_DIR):
        os.makedirs(UPLOAD_DIR)
        print(f"📁 Created upload directory: {UPLOAD_DIR}")
    
    # Start server
    with socketserver.TCPServer(('', PORT), AdminHandler) as httpd:
        print(f"🔒 Admin Server running on port {PORT}")
        print(f"🌐 Admin Dashboard: http://localhost:{PORT}/admin.html")
        print(f"⚠️  Keep this URL secret!")
        print(f"🛑 Press Ctrl+C to stop the server")
        
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\n🛑 Admin server stopped")

if __name__ == "__main__":
    setup_admin_server() 