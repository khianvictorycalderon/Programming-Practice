sample_data = [
    {"id": 1, "title": "Learn JavaScript", "desc": "Master the basics of JavaScript."},
    {"id": 2, "title": "Learn HTML", "desc": "Master the basics of HTML."},
    {"id": 3, "title": "Learn CSS", "desc": "Master the basics of CSS."},
    {"id": 4, "title": "Learn JavaScript", "desc": "Master the basics of JavaScript."},
    {"id": 5, "title": "Responsive Design", "desc": "Create designs that adapt to any screen."},
    {"id": 6, "title": "Flexbox Guide", "desc": "Learn how to use Flexbox for layouts."},
    {"id": 7, "title": "Grid Layout", "desc": "Learn CSS Grid for advanced layouts."},
    {"id": 8, "title": "Responsive Design", "desc": "Create designs that adapt to any screen."},
    {"id": 9, "title": "Web Accessibility", "desc": "Make your websites accessible to everyone."},
    {"id": 10, "title": "SEO Basics", "desc": "Improve your website's search engine ranking."},
    {"id": 11, "title": "Learn JavaScript", "desc": "Master the basics of JavaScript."},
    {"id": 12, "title": "Git & GitHub", "desc": "Version control and collaboration tools."},
    {"id": 13, "title": "React Basics", "desc": "Build interactive UIs with React."},
    {"id": 14, "title": "Node.js Intro", "desc": "Learn server-side JavaScript with Node.js."},
    {"id": 15, "title": "CSS Animations", "desc": "Bring your website to life with animations."},
    {"id": 16, "title": "Flexbox Guide", "desc": "Learn how to use Flexbox for layouts."},
    {"id": 17, "title": "Web Accessibility", "desc": "Make your websites accessible to everyone."},
    {"id": 18, "title": "React Basics", "desc": "Build interactive UIs with React."},
    {"id": 19, "title": "API Integration", "desc": "Connect your app to external services."},
    {"id": 20, "title": "Learn HTML", "desc": "Master the basics of HTML."},
    {"id": 21, "title": "Node.js Intro", "desc": "Learn server-side JavaScript with Node.js."},
    {"id": 22, "title": "SEO Basics", "desc": "Improve your website's search engine ranking."}
]

def remove_duplicate_titles(array):
    seen = set()
    result = []
    
    for item in array:
        if item["title"] not in seen:
            seen.add(item["title"])
            result.append(item)
    
    return result

print(remove_duplicate_titles(sample_data))