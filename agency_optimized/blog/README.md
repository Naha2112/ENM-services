# ENM'S SERVICES Blog Template Guide

This guide explains how to use the blog post template to create new SEO-optimized blog posts for the ENM'S SERVICES website.

## Template File
- **Location**: `blog/blog-post-template.html`
- **Purpose**: Standardized template for creating new blog posts with proper SEO elements

## How to Create a New Blog Post

### 1. Copy the Template
1. Copy `blog-post-template.html` to a new file
2. Name the file using the format: `blog-post-slug.html`
3. Use lowercase letters, hyphens for spaces, no special characters

### 2. Replace Template Placeholders

#### Meta Information
- `[BLOG POST TITLE]` - The main title of your blog post
- `[BLOG POST DESCRIPTION]` - 150-160 character description for search engines
- `[RELEVANT KEYWORDS]` - Comma-separated keywords related to the topic
- `[BLOG-POST-URL]` - The filename without .html extension
- `[CATEGORY]` - The blog post category (e.g., "Property Maintenance", "Security Services")

#### Content Placeholders
- `[BREADCRUMB TITLE]` - Short title for breadcrumb navigation
- `[PUBLICATION DATE]` - Format: "Month DD, YYYY" (e.g., "December 15, 2024")
- `[X] min read` - Estimated reading time
- `[ARTICLE SUBTITLE/SUMMARY]` - Brief summary for the header section
- `[INTRODUCTION PARAGRAPH]` - Opening paragraph that hooks the reader
- `[SECTION HEADING 1]`, `[SECTION HEADING 2]` - Main section headings
- `[SUBSECTION HEADING]` - Subsection headings
- `[CTA HEADING]` - Call-to-action heading
- `[CTA DESCRIPTION]` - Call-to-action description
- `[CTA BUTTON TEXT]` - Text for the action button
- `[SERVICE]` - Relevant service for WhatsApp link

#### Images and Media
- `[RELEVANT-IMAGE]` - Image filename from the images folder
- `[RELATED-ARTICLE-1-URL]`, `[RELATED-ARTICLE-2-URL]` - Links to related articles

#### Schema Data
- `[YYYY-MM-DD]` - Publication date in ISO format (e.g., "2024-12-15")

### 3. Content Guidelines

#### SEO Best Practices
- **Title**: 50-60 characters, include main keyword
- **Meta Description**: 150-160 characters, compelling and descriptive
- **Headings**: Use H1 for title, H2 for main sections, H3 for subsections
- **Keywords**: Include naturally throughout the content
- **Internal Links**: Link to relevant service pages and other blog posts
- **External Links**: Link to authoritative sources when appropriate

#### Content Structure
1. **Introduction** (150-200 words)
   - Hook the reader
   - Introduce the topic
   - Mention ENM'S SERVICES expertise
   - Preview what the article covers

2. **Main Content** (800-1500 words)
   - Use clear headings and subheadings
   - Include bullet points and numbered lists
   - Add practical tips and advice
   - Include professional insights

3. **Call-to-Action**
   - Encourage readers to contact ENM'S SERVICES
   - Customize WhatsApp message for the specific service
   - Use compelling action words

4. **Related Articles**
   - Link to 2 relevant blog posts or service pages
   - Provide brief descriptions

#### Writing Style
- **Tone**: Professional but approachable
- **Expertise**: Demonstrate knowledge and experience
- **Local Focus**: Mention London and surrounding areas when relevant
- **Practical**: Provide actionable advice and tips
- **Length**: Aim for 1000-2000 words for comprehensive coverage

### 4. Technical Requirements

#### File Naming
- Use lowercase letters only
- Replace spaces with hyphens
- No special characters or numbers at the start
- Example: `kitchen-renovation-tips.html`

#### Image Requirements
- Store images in the `../images/` folder
- Use descriptive filenames
- Optimize for web (under 500KB)
- Include alt text for accessibility

#### Links
- Internal links should be relative paths
- External links should open in new tabs
- WhatsApp links should include relevant pre-filled message

### 5. After Creating the Blog Post

#### Update Blog Listing Page
1. Open `blog.html`
2. Add a new blog post card with:
   - Appropriate icon
   - Title and description
   - Publication date and category
   - Link to the new blog post

#### Update Sitemap
1. Open `sitemap.xml`
2. Add a new URL entry for the blog post:
```xml
<url>
  <loc>https://www.enmsservices.co.uk/blog/[BLOG-POST-URL].html</loc>
  <lastmod>[YYYY-MM-DD]</lastmod>
  <changefreq>monthly</changefreq>
  <priority>0.7</priority>
</url>
```

#### Update Blog Schema
1. Open `blog.html`
2. Add the new blog post to the Schema.org structured data

### 6. Content Ideas

#### Property Maintenance Topics
- Seasonal maintenance guides
- DIY vs professional services
- Cost-saving tips
- Common problems and solutions
- Material selection guides

#### Security Topics
- Security system comparisons
- Legal requirements and compliance
- Risk assessment guides
- Industry best practices
- Technology updates

#### Kitchen and Bathroom Topics
- Design trends
- Material selection
- Installation processes
- Maintenance tips
- Cost considerations

### 7. SEO Checklist

Before publishing, ensure:
- [ ] Title is optimized and under 60 characters
- [ ] Meta description is compelling and under 160 characters
- [ ] URL is SEO-friendly
- [ ] Headings use proper hierarchy (H1, H2, H3)
- [ ] Images have alt text
- [ ] Internal links are included
- [ ] Schema markup is properly configured
- [ ] Content is original and valuable
- [ ] Call-to-action is clear and relevant
- [ ] Related articles are linked
- [ ] Sitemap is updated
- [ ] Blog listing page is updated

### 8. Maintenance

#### Regular Updates
- Review and update content quarterly
- Check for broken links
- Update publication dates if content is significantly revised
- Monitor performance and adjust keywords as needed

#### Performance Tracking
- Monitor page views and engagement
- Track conversion from blog to contact
- Analyze search rankings for target keywords
- Use insights to improve future content

This template system ensures consistency, SEO optimization, and professional presentation across all ENM'S SERVICES blog content.
