from django.shortcuts import render

def get_blog(request):
    blogs = [
        {'title': 'First Blog', 'text': 'This is the text of the first blog post.', 'author' : 'Jane Smith'},
        {'title': 'Second Blog', 'text': 'This is the text of the second blog post.', 'author' : 'John Doe'},
        {'title': 'Third Blog', 'text': 'This is the text of the third blog post.', 'author' : 'Alex Smith'},
    ]
    return render(request, 'get_b/blog.html', {'blogs': blogs})
