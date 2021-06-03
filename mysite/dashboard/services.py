from django.db import connection
from contextlib import closing

def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_courses""")
        courses=dict_fetchall(cursor)
        return courses

def get_courses_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from mentor_courses""")
        courses=dict_fetchall(cursor)
        return courses

def get_categories_news_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT  count(dashboard_news.id),dashboard_category.name ,dashboard_news.category_id 
        FROM dashboard_category LEFT JOIN dashboard_news
		ON dashboard_news.category_id=dashboard_category.id
		GROUP BY dashboard_news.category_id,dashboard_category.name 
        ORDER BY COUNT(dashboard_news.id) DESC""")
        categories=dict_fetchall(cursor)
        return categories


def count_authors():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""SELECT COUNT(id), author_id  
        FROM dashboard_news
        GROUP BY author_id
        ORDER BY COUNT(id) DESC;""")
        categories=dict_fetchall(cursor)
        return categories

def get_trainers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_trainer""")
        trainers=dict_fetchall(cursor)
        return trainers

def get_trainers_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(name) from mentor_trainer""")
        trainers=dict_fetchall(cursor)
        return trainers

def get_events():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_events""")
        events=dict_fetchall(cursor)
        return events

def get_events_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(title) from mentor_events""")
        events=dict_fetchall(cursor)
        return events

def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_students""")
        students=dict_fetchall(cursor)
        return students

def get_students_count():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(full_name) from mentor_students""")
        students=dict_fetchall(cursor)
        return students

# def get_views():
#     with closing(connection.cursor()) as cursor:
#         cursor.execute("""select name, sum(views) as count from dashboard_category
#         left join dashboard_news on dashboard_category.id=dashboard_news.category_id
#         group by name""")
#         views=dict_fetchall(cursor)
#         return views



def get_subjects_all():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select count(subject) from mentor_students """)
        subjects = dict_fetchall(cursor)
    return subjects


def get_frontend():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select count(subject) from mentor_students where subject = 'frontend' """)
        front = dict_fetchall(cursor)
    return front

def get_backend():
    with closing(connection.cursor()) as cursor:
        cursor.execute(""" select count(subject) from mentor_students where subject = 'backend' """)
        front = dict_fetchall(cursor)
    return front

def dict_fetchall(cursor):
    columns = [col[0] for col in cursor.description]
    return [
        dict(zip(columns, row))
        for row in cursor.fetchall()
    ]


def dict_fetchone(cursor):
    row = cursor.fetchone()
    if row is None:
        return False
    columns = [col[0] for col in cursor.description]
    return dict(zip(columns, row))