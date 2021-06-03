from django.db import connection
from contextlib import closing


def get_abouts():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_about""")
        abouts = dict_fetchall(cursor)
        return abouts


def get_resources():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_resources""")
        resources = dict_fetchall(cursor)
        return resources

def get_trainers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_trainer""")
        trainers = dict_fetchall(cursor)
        return trainers

def get_comment_writers():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_comment_writers""")
        writers_name = dict_fetchall(cursor)
        return writers_name

def get_events():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_events""")
        writers_name = dict_fetchall(cursor)
        return writers_name

def get_students():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select * from mentor_students""")
        students = dict_fetchall(cursor)
        return students


def get_courses():
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mentor_courses.*, mentor_trainer.name as t_name, mentor_trainer.image as t_image from mentor_courses
            inner join mentor_trainer on mentor_courses.trainer_id =mentor_trainer.id""")
        courses = dict_fetchall(cursor)
        return courses

# """select * from mentor_courses where id = %s """, [courses_id]


def get_courses_details(courses_id):
    with closing(connection.cursor()) as cursor:
        cursor.execute("""select mentor_courses.*, mentor_trainer.name as t_name, mentor_trainer.image as t_image from mentor_courses
            inner join mentor_trainer on mentor_courses.trainer_id =mentor_trainer.id where mentor_courses.id = %s """, [courses_id])
        courses = dict_fetchone(cursor)
        return courses



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
