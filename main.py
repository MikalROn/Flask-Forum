from flask import Flask, render_template, request, redirect


forum = Flask(__name__, static_folder='static')


mensagens: list[dict] = [{}]
value = ''

def render_value(value: str) -> str:
    return ''.join([x if i != 90  else f'{x}\n' for i, x in enumerate(value)])

@forum.route('/')
def index():
    return render_template('index.html', 
                           menssagens=mensagens, 
                           render_value=render_value,
                           value=value)

@forum.route('/send_message', methods=['POST'])
def send_message():
        if request.method == 'POST' and request.form["user"] and request.form["msg"]:
            value = request.form["user"] 
            mensagens.append(
                {
                    request.form["user"]: request.form["msg"]
                    }
                )
            print(mensagens)
        return redirect('/')
    

if __name__ == '__main__':
    forum.run(debug=True, host="0.0.0.0")
    