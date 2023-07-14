"""
Generate HTML
"""

from generating_responses import GenerateResponse

def generate_html():
    """
    Generating HTML
    """
    response = GenerateResponse()
    
    start = '''
<!DOCTYPE html>
<html>
    <head>
    </head>
    <body>
'''
    
    end = '''
    </body>
</html>
'''
    
    responses = [response.total_likes_response(), 
                response.total_login_history_response(),
                response.total_share_history_response(),
                response.total_comments_response(),
                response.total_vidoes_you_made_response()]
                
    for response in responses:
        start += f'''
        <p>{response}<p>\n
'''
    
    html = start + end
    
    return html
    
def write_html_file():
    """
    Writing the generated HTML to a file
    """
    
    html = generate_html()
    
    with open("tiktok_wrapped.html", "w") as f:
        f.write(html) 
   
write_html_file()
  
