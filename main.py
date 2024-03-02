from bs4 import BeautifulSoup

with open('home.html','r') as h:
    content=h.read()
    # print(content)

    soup=BeautifulSoup(content,'lxml')
    # tags=soup.find('h5')
    # html_courses=soup.find_all('h5')
    # # print(tags)
    # for cources in html_courses:
    #     print(cources.text)
    couese_cards=soup.find_all('div',class_='card')
    print(couese_cards)
    for course in couese_cards:
        course_name=course.h5.text
        course_price=course.a.text.split()[-1]
        # print(course_name)
        # print(f'{course_name} costs {course_price}')
