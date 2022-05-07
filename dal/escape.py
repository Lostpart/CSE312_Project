def html_escape(msg):
    msg = msg.replace("&", "&amp;")
    msg = msg.replace("<", "&lt;")
    msg = msg.replace(">", "&gt;")
    msg = msg.replace('"', "&quot;")
    msg = msg.replace("'", "&apos;")
    return msg
