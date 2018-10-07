from bs4 import BeautifulSoup


def load_sample_result_html():

    with open('result_query_sample_html.txt', 'r') as myfile:
        html = myfile.read().replace('\n', '')

    parsed_html = BeautifulSoup(html, 'lxml')
    return parsed_html
