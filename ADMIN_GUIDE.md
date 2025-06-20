# ENM'S SERVICES - Admin Dashboard Guide

## 🔒 Secret Admin Access

The admin dashboard provides an easy way to manage images and update your portfolio without touching code.

## 🚀 Quick Start

### 1. Start the Admin Server
```bash
python3 admin_server.py
```

### 2. Access the Dashboard
Open your browser and go to:
**http://localhost:8444/admin.html**

⚠️ **Keep this URL secret!** This is your private admin panel.

## 📸 Managing Images

### Upload New Images
1. Click the **Upload Images** section
2. Select your category (Bathroom, Kitchen, etc.)
3. Click the upload zone or drag & drop images
4. Click **Process Selected Images**

### Add Images to Carousel
1. In the **Current Images** section, find your image
2. Click **Add to Carousel** button
3. The image will appear in the carousel preview

### Remove from Carousel
1. In the **Portfolio Manager** section
2. Click the **×** button on any carousel image to remove it

## 🎨 Portfolio Management

### Update Portfolio Title
1. Go to **Portfolio Manager** section
2. Edit the **Portfolio Title** field
3. Changes are saved automatically

### Reorder Carousel Images
- Click on any thumbnail in the carousel preview to set it as the main image
- The first image is always the one shown initially

## 🛠 Quick Actions

- **View Website**: Opens your live website in a new tab
- **Clear Browser Cache**: Refreshes the page to show latest changes

## 📁 File Management

### Supported Formats
- JPG, JPEG, PNG, WebP, GIF
- Automatic file renaming for safety
- Duplicate files get timestamp suffixes

### File Organization
- All images are stored in the `images/` folder
- Files are automatically renamed to be web-safe
- Original filenames are preserved when possible

## 🔧 Technical Notes

### Two Servers
- **Main Website**: http://localhost:8443 (public)
- **Admin Dashboard**: http://localhost:8444 (private)

### Security
- Admin dashboard runs on a different port
- No authentication (keep URL private)
- Only serves to localhost

### Backup
- Images are stored in the `images/` folder
- Carousel configuration saved in `carousel_config.json`
- Regular backups recommended

## 🆘 Troubleshooting

### Images Not Showing
1. Check if files are in the `images/` folder
2. Refresh the gallery using the **Refresh Gallery** button
3. Clear browser cache

### Upload Issues
1. Check file format (JPG, PNG, WebP only)
2. Ensure files aren't too large
3. Check console for error messages

### Server Issues
1. Make sure port 8444 is available
2. Check if Python 3 is installed
3. Restart the admin server

## 💡 Tips

1. **Organize by Category**: Use the category dropdown when uploading
2. **Optimal Image Size**: 1200x800px works well for carousel
3. **File Names**: Use descriptive names (bathroom-renovation-1.jpg)
4. **Regular Updates**: Keep your portfolio fresh with new projects
5. **Test Changes**: Always check the live website after updates

---

**Remember**: Keep the admin URL private and only share with trusted team members! 