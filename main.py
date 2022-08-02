# Marvish Chandra

'''Through web scraping, this program is intended to help students find the rating information of a college from the Rate My Professor database.'''

from bs4 import BeautifulSoup

with open('ratemyprofessors.com/campusRatings.jsp?sid=1072','r') as html_file:
    content = html_file.read()

    soup = BeautifulSoup(content, 'lxml')
    professor_name = soup.find_all('div',class_='professor-name')
    for pron in professor_name:
        print(pron)
    professor_rating = soup.find_all('div',class='professor-name-rating')
    for pror in professor_rating:
        print(pror)
    professor_rcount = soup.find_all('div',class='professor-rating-count')
    for prorc in professor_rcount:
        print(prorc)
    schoolrate = soup.find('table',class='school-ratings')
    for schoolr in schoolrate:
        print(schoolr)




