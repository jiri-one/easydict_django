from .models import Record
import difflib

def db_search(language, text, fulltext):
    if fulltext == "whole_word":
        text_for_pqsql = rf'\y{text}\y'
    else:
        text_for_pqsql = text
    
    if language == "Anglicky" or language == "English":
        language = "eng"
        results = Record.objects.filter(eng__search=text_for_pqsql).values()
    elif language == "Česky" or language == "Czech":
        language = "cze"
        results = Record.objects.filter(cze__search=text_for_pqsql).values()

    results_with_matchratio = []
    for result in results:
        ratio = difflib.SequenceMatcher(None, result[language], text).ratio()
        results_with_matchratio.append([result, ratio])
    sorted_results = sorted(results_with_matchratio, key=lambda x: x[1], reverse=True)
    html = CreateHtml(sorted_results, language)
    return html()

class CreateHtml:
    def __init__(self, results, language):
        self.language = language
        self.second_language = [lang for lang in [
            "cze", "eng"] if lang != language][0]
        self.html_string = ""
        for row in results:
            self.html_string = self.html_string + self.create_html(row[0])
    
    def __call__(self):
        return self.html_string
            
    def create_html(self, row):
        if "notes" in row.keys():
            self.notes =  ", " + row["notes"]
        else:
            self.notes = ""
        if "special" in row.keys():
            self.special = ", "  + row["special"]
        else:
            self.special = ""        
    
        html = f"""
        <p>{row[self.language]}</b>
        <br>&emsp;{row[self.second_language]}{self.notes}{self.special}<hr />
        </p>
        """
        return html
