def validate_input(text):
    """
    Retorna: 'youtube', 'spotify', ou 'query'
    Raises Exception se for URL inválida
    """
    # Se não parece com URL, é texto (query)
    if not text.startswith(('http://', 'https://', 'www.')):
        return 'query'
    
    # Se é URL, verifica se é YouTube ou Spotify
    if any(domain in text.lower() for domain in ['youtube.com', 'youtu.be']):
        return 'youtube'
    elif 'open.spotify.com' in text.lower():
        return 'spotify'
    else:
        # URL inválida
        raise Exception("URL inválida. Use apenas YouTube ou Spotify")