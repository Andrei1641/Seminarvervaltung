# Commands Test

## Create

### Create "person"

| Testfallbeschreibung    | Testdaten           | Hypothese                                     | Testergebnis    |
|-------------------------|---------------------|-----------------------------------------------|-----------------|
| first/second name enter |                     |                                               |                 |
| not only letter         | A4drei, d$fl, L<dfe | error: name can only consist letter           | correct         |
| empty                   | "", " "             | error: name can not be empty                  | correct         |
| right name enter        | Name, name          | Name, Name                                    | Name, Name      |
| email enter             |                     |                                               |                 |
| there is no @           | asdf                | error: please enter the correct email-address | correct         |
| empty                   | "", " "             | error: email can not be empty                 | correct         |
| right email enter       | aDsfs@gmail.com     | adsfs@gmail.com                               | adsfs@gmail.com |
| theme enter(docent)     |                     |                                               |                 |
| empty                   | "", " "             | error: this dozent can not learn              | correct         |

### Create course

| Testfallbeschreibung                         | Testdaten                                     | Hypothese                                                        | Testergebnis   |
|----------------------------------------------|-----------------------------------------------|------------------------------------------------------------------|----------------|
| title/place enter                            |                                               |                                                                  |                |
| empty                                        | "", " "                                       | error: <title/place> can not be empty                            | correct        |
| right title/place enter                      | "dfsga 205"                                   | dfsga 205                                                        | dfsga 205      |
| duration/max_participant_count enter         |                                               |                                                                  |                |
| out of await range                           | 0, -5                                         | error: <duration/max_participant_count> need to be higher than 0 | correct        |
| empty                                        | " ", ""                                       | error: <duration/max_participant_count> can not be empty         | correct        |
| correct duration/max_participant_count enter | 5, 10                                         | 5, 10 (minutes)                                                  | 5, 10          |
| date enter                                   |                                               |                                                                  |                |
| inappropriate format                         | 2000-5-5-5-5, 2000-5-5-5-5-5-5, "", - - - - - | error: date has inappropriate format (YYYY-MM-DD-HH-MM-SS)       | correct        |
| zero input                                   | 2000-0-4-4-4-4                                | error: date period can not be less than 1                        |                |
| not numeric                                  | 2000-d-5-5-5-a                                | error: date can not consist letter                               | correct        |
| out of await period                          | 200-5-5-5-5-5, 20000-5-5-5-5-5                | error: it is out of observing years                              | correct        |
| input on month is too big                    | 2000-13-5-5-5-5                               | error: months can not be higher then 12                          | correct        |
| input on day is too big                      | 2000-11-31-5-5-5                              | error: days can not be higher then 30 in 11 month                | correct        |
| input on hour is too big                     | 2000-5-5-24-4-4, 2000-5-5-40-4-4              | error: hours can not be higher then 23                           | correct        |
| input on minute/second is too big            | 2000-5-5-5-60-5, 2000-5-5-5-50-100            | error: <minutes/seconds> can not be higher then 59               | correct        |
| correct date enter                           | 2000-5-5-5-5-5                                | 2000-5-5-5-5-5                                                   | 2000-5-5-5-5-5 |

## Add

### Add person

#### (setUp):
global participant_db has a participants: name = Smith James, name = Russell Michael  
global docent_db has a docent: name = James Jon, Harrison Bil, Arnold Daniel 
global course_db has a courses: title = Math, max_participant_count = 1, date = 2000-5-5-5-5-5, duration = 40; title = Bio, date = 2000-5-5-5-15-5

| Testfallbeschreibung    | Testdaten                                                       | Hypothese                                                                      | Testergebnis |
|-------------------------|-----------------------------------------------------------------|--------------------------------------------------------------------------------|--------------|
| docent/person not found | name = Conner Steven, role: docent                              | error: there is no such a <docent/person>: Conner Steven, there are: James Jon | correct      |
| course not found        | title = Deu                                                     | error: there is no such a course: Deu, there are: Math, Bio                    | correct      |
| person overflow         | title = Math -> add Smith James, Russell Michael                | error: the seminar "Math" is already full for participant                      | correct      |
| docent overflow         | title = Math -> add James Jon, Harrison Bil, Arnold Daniel      | error: the seminar "Math" is already full for docents                          | correct      |
| docent/person is busy   | title = Math -> add Smith James; title = Bio -> add Smith James | error: this person is already on course: Math                                  | correct      |

## Show

#### (setUp):
global participant_db has a participants: name = Smith James, Harrison Bil 
global docent_db has a docent: name = Arnold Daniel, James Jon
global course_db has a courses: title = Math
course: title = Math has Smith James(participant), Arnold Daniel(docent)

| Testfallbeschreibung            | Testdaten    | Hypothese                 | Testergebnis              |
|---------------------------------|--------------|---------------------------|---------------------------|
| show all docents                | ^            | Arnold Daniel, James Jon  | Arnold Daniel, James Jon  |
| show all participant            | ^            | Smith James, Harrison Bil | Smith James, Harrison Bil |
| show all course                 | ^            | Math                      | Math                      |
| show participants inside course | title = Math | Smith James               | Smith James               |
| show docents inside course      | title = Math | Arnold Daniel             | Arnold Daniel             |

## Info

#### (setUp):
global participant_db has a participants: name = Smith James  
global docent_db has a docent: name = Arnold Daniel email = arnold@gmail.com, list_of_theme: mat  
global course_db has a courses: title = Math, max_participant_count = 1, date = 2000-5-5-5-5-5, duration = 40  
course: title = Math has Smith James(participant), Arnold Daniel(docent), max_participant_count = 1, date = 2000-5-5-5-5-5, duration = 40, place = room 125  

| Testfallbeschreibung | Testdaten            | Hypothese                                                                                                                      | Testergebnis |
|----------------------|----------------------|--------------------------------------------------------------------------------------------------------------------------------|--------------|
| info person          | name = Arnold Daniel | Name: Arnold Daniel  Email-Adresse: arnold@gmail.com  Rolle: Dozent(Teilnehmer)  'Themen: mat(only for docents)                | correct      |
| info course          | title = Math         | Titel: Math  Dozierend: Arnold Daniel  Datum: 2000-5-5 um 5:5:5 Uhr  Dauer: 40 Minuten  Ort: room 125  Plätze: 1 von 1 bellegt | correct      |

### Delete

#### (setUp):
global participant_db has a participants: name = Smith James   
global course_db has a courses: title = Math   
course: title = Math has Smith James(participant), Arnold Daniel(docent)

| Testfallbeschreibung | Testdaten                        | Hypothese                                        | Testergebnis |
|----------------------|----------------------------------|--------------------------------------------------|--------------|
| delete from db       | name = Smith James               | this person will delete from db and from courses | correct      |
| delete from course   | name = Smith James, title = Math | this person will delete from the course          | correct      |
| delete course        | title = Math                     | this course will delete from db                  | correct      |