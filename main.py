from factories.persons_factory import PersonFactory
from factories.seminar_factory import SeminarFactory
from classes.db import DataBase


dozent_db = DataBase()
teilnehmer_db = DataBase()

a = PersonFactory.create_docent('And', 'Sor', 'fsf@gmail.com', ['bio', 'mat'])
c = PersonFactory.create_docent('Tnd', 'Nor', 'fsf@gmail.com', ['bio', 'mat'])
b = PersonFactory.create_participant('And', 'Sor', 'fsf@gmail.com')
t = PersonFactory.create_participant('Qnd', 'Lor', 'fsf@gmail.com')

dozent_db.insert_in_db(a)
dozent_db.insert_in_db(c)

teilnehmer_db.insert_in_db(b)
teilnehmer_db.insert_in_db(t)

mat_sem = SeminarFactory.create_seminar('Math', '2005-10-30-20-43-43', 30, 10, 'klass 25')

mat_sem.add_participant('Sor And', teilnehmer_db)
mat_sem.add_docent('Nor Tnd', dozent_db)
mat_sem.add_docent('Sor And', dozent_db)

print(a)
