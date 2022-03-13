import json
from protocol_handler import ProtocolHandler

def create_html(lines):
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
     
def write_files(protocol_handlers : 'list[ProtocolHandler]'):
    filename = 'public/handlers'
    json_file = open(filename + '.json', 'w')
    json_content = json.dumps(list(map(lambda x: x.__dict__, protocol_handlers)))
    json_file.write(json_content)
    json_file.close()

    lines = [f"<li><a href='{ph.protocol}://any'><div class='protocol'>{ph.protocol}</div><div class='command'>{ph.command}</div></a></li>" for ph in protocol_handlers]
    html_file = open(filename + ".html", 'w')
    content = create_html(lines)
    html_file.write(content)
    html_file.close()