import json

CANDIDATES_PATH = "candidates.json"


def loud_list() -> list[dict]:
    """все кандитаты словарём"""
    with open(CANDIDATES_PATH, "r", encoding="utf-8") as f:
        return json.load(f)


def list_candidates(list) -> str:
    """Форматирование списка кандидатов"""
    result = "<pre>\n"
    for candidat in list:
        result += f'''  {candidat["name"]}\n
  {candidat["position"]}\n
  {candidat["skills"]}\n
\n'''
    result += "</pre>"
    return result


def get_candidat(uid: int) -> dict:
    """Поиск кандидата по id"""
    list_candidats = loud_list()
    for candidat in list_candidats:
        if candidat["id"] == uid:
            return candidat


def get_candidat_skill(skill: str) -> list[dict]:
    """Поиск кандидата по skill"""
    list_candidats= loud_list()
    result = []
    for candidat in list_candidats:
        if skill in candidat["skills"].lower().split(', '):
            result.append(candidat)
    return result
