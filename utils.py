def safe_html(data: str):
    return data.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
