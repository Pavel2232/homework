from flask import Flask
from test import loud_list, format_candidates, get_candidat, get_candidat_skill

app = Flask(__name__)


@app.route("/")
def home_page():
    """Главная страница"""
    candidats = loud_list()
    result = format_candidates(candidats)
    return result


@app.route('/candidates/<int:uid>')
def candidate_page(uid):
    """Страница студентов по Id"""
    candidat = get_candidat(uid)
    result = f'<img src="{candidat["picture"]}">'
    result += format_candidates([candidat])
    return result


@app.route('/skills/<skill>')
def skills_page(skill):
    """Страница студентов с навыками Skill"""
    candidat = get_candidat_skill(skill.lower())
    result = format_candidates(candidat)
    return result


if __name__ == "__main__":
    app.run(debug=True)



