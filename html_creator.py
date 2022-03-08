from protocol_handler import ProtocolHandler


def create_content(lines):
    list = [f"<li></li>"]
    content = '\n'.join(lines)
    return f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Custom protocol handlers</title>
        <style>
            a {{display:block;text-decoration: none;color:black;}}
            a:hover {{background-color:black; color:white;}}
            .command {{color:slategrey}}
        </style>
    </head>
    <body>
        <ol>
            {content}
        </ol>
    </body>
    </html>
    """
     
def create_html(filename, custom_protocol_handlers : list[ProtocolHandler]):
    lines = [f"<li><a href='{soc.protocol}://any'><div class='protocol'>{soc.protocol}</div><div class='command'>{soc.command}</div></a></li>" for soc in custom_protocol_handlers]
    file = open(filename, 'w')
    content = create_content(lines)
    file.write(content)
    file.close()