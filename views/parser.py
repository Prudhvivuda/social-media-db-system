from views.posts import get_trending_posts
from views.reported_content import get_reported_content
from views.activity import get_activity
from views.followers import get_followers

views_functions = {
    'get_trending_posts': get_trending_posts,
    'get_reported_content': get_reported_content,
    'get_activity': get_activity,
    'get_followers': get_followers,
}
    
    
def parse_views(view_type):
    if view_type == 'get_trending_posts':
        return get_trending_posts()
    elif view_type == 'get_reported_content':
        return get_reported_content()
    elif view_type == 'get_activity':
        return get_activity()
    elif view_type == 'get_followers':
        return get_followers()