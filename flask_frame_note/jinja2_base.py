from flask import Flask, render_template

app = Flask(__name__,
            # the folder that contains the templates that should be used by the application.
            # Defaults to ``'templates'`` folder in the root path of the application.
            template_folder='templates'
            )


class Play:
    play_min = 34

    def play_info(self, describe):
        return "玩的" + describe + "开心"


@app.route('/index', methods=['GET'])
def index():
    name = "dcdmm"
    age = 3
    like = ['football', 'game', 'music']
    other = {"countery": "china", "grade": "A"}
    p = Play()
    return render_template('jinja2_base.html',
                           **{
                               # `user_name`: jinja2中的变量名
                               "user_name": name,
                               "user_age": age,
                               "user_like": like,
                               "user_other": other,
                               "user_play": p
                           }
                           )


if __name__ == '__main__':
    app.run()
