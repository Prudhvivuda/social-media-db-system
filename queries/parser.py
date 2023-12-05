from queries.followers import get_followers_count
from queries.likes import get_likes_count


query_functions = {
    'get_followers': get_followers_count,
    'get_likes': get_likes_count,
}
    
    
def parse_query(query_type):
    if query_type == 'get_likes_count':
        return get_likes_count()
    elif query_type == 'get_followers_count':
        return get_followers_count()
