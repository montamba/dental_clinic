import os
from flask import Flask
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

supabase: Client = create_client(
    os.getenv("SUPABASE_URL"),
    os.getenv("SUPABASE_KEY")
)

@app.route('/')
def index():
    html = '<h1>Todos</h1><ul>'
    res = supabase.table('user').insert([{"first_name":"moana","last_name":"stone"}]).select("id").execute()
    dat = res.data
    html +="<h2>" + str(dat) + "</h2>"
    
    response = supabase.table('user').select("*").execute()
    todos = response.data

    html = '<h1>Todos</h1><ul>'
    for todo in todos:
        html += f'<li>{todo}</li>'
    html += '</ul>'

    return html

if __name__ == '__main__':
    app.run(debug=True)