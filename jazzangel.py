import requests
import re

def patchJazzAngelJS(html_content):
    pattern = r'(</body>)'
    script_tag = '<script src="scripts/jazzangel.js"></script>\n'
    patched_html = re.sub(pattern, script_tag + r'\1', html_content, flags=re.DOTALL)
    return patched_html

def cleanHtml(html_content):
    pattern = r'''
        <meta.*?>\s*                    
        .*?                              
        <link.*?>                        
    '''
    cleaned_html = re.sub(pattern, r'<meta />\n<link rel="stylesheet" />', html_content, flags=re.DOTALL | re.VERBOSE)
    return cleaned_html

def downloadDocs():
    url = 'https://docs.jj2.plus/plus-angelscript.html'
    file_path = "plus-angelscript.html"
    response = requests.get(url)
    html_content = response.text
    newhtml = cleanHtml(html_content)
    patched_html = patchJazzAngelJS(newhtml)
    with open(file_path, "w", encoding='utf-8') as file:
        file.write(patched_html)
 
downloadDocs()