# Importing specific functions for handling queries from respective modules
from queries.followers import get_followers_count
from queries.likes import get_likes_count

# Dictionary mapping query types to their corresponding functions
query_functions = {
    'get_followers': get_followers_count,
    'get_likes': get_likes_count,
}
    
def parse_query(query_type):
    """
    Parses the query type and calls the corresponding function.

    Parameters:
    - query_type (str): The type of query to be parsed.

    Returns:
    - result: The result of the executed query function.
    """
    # Checking the query type and calling the appropriate function
    if query_type == 'get_likes_count':
        return get_likes_count()
    elif query_type == 'get_followers_count':
        return get_followers_count()
