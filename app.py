from flask import Flask,render_template
from func import loud_list, list_candidates, get_candidat, get_candidat_skill, get_candidates_by_name

app = Flask(__name__)


@app.route("/")
def home_page():
    """Главная страница"""
    candidates = loud_list()
    return render_template('list.html', candidates = candidates)


@app.route('/candidates/<int:uid>')
def candidate_page(uid):
    """Страница студентов по Id"""
    candidat = get_candidat(uid)
    if not candidat:
        return "Кандидат не найден"
    return render_template('card.html', candidat = candidat)


@app.route('/skills/<skill>')
def skills_page(skill):
    """Страница студентов с навыками Skill"""
    candidat = get_candidat_skill(skill.lower())
    return render_template('skill.html', candidates = candidat)


@app.route('/search/<candidate_name>')
def candidate_name_page(candidate_name):
    candidates = get_candidates_by_name(candidate_name)
    return render_template('search.html', candidates = candidates)



if __name__ == "__main__":
    app.run(debug=True)



