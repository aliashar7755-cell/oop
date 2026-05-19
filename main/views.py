from django.shortcuts import render


def home(request):
    context = {
        'name': 'Your Name',
        'title': 'Python Django Developer',
        'description': 'I build clean, responsive web experiences with Django, HTML, CSS, and JavaScript.',
        'about': 'I am a developer who enjoys turning simple ideas into fast, useful websites that work smoothly on desktop and mobile.',
        'skills': ['Python', 'Django', 'HTML', 'CSS', 'JavaScript', 'SQLite', 'Responsive Design'],
        'projects': [
            {
                'name': 'Personal Portfolio',
                'description': 'A clean Django portfolio site with reusable templates and static front-end assets.',
                'link': '#projects',
            },
            {
                'name': 'Task Dashboard',
                'description': 'A simple dashboard concept for tracking project progress and daily priorities.',
                'link': '#projects',
            },
            {
                'name': 'Business Landing Page',
                'description': 'A responsive landing page layout with clear sections and smooth navigation.',
                'link': '#projects',
            },
        ],
        'contact_email': 'your.email@example.com',
        'contact_message': "Let's build something great together.",
    }
    return render(request, 'main/index.html', context)
