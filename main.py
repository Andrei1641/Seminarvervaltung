import json

from collector import Information
import shlex


information = Information()

information.deserialize()


while True:
    try:
        query: str = str(input('write your query: '))

        if query == 'end':
            break

        query_modules: list[str] = shlex.split(query)

        action = query_modules[0]
        target = query_modules[1]
        args = query_modules[2:]

        states: dict = {
                        'create' : {
                                    'docent' : information.docent_create,
                                    'participant' : information.participant_create,
                                    'course' : information.course_create
                                    },
                        'add':     {
                                    'docent' : information.add_docent_to_course,
                                    'participant' : information.add_participant_to_course
                                    },
                        'show':    {
                                    'all' : information.show_all,
                                    'course' : information.show_course
                                   },
                        'delete':   {
                                    'from db' : information.delete_from_db,
                                    'from course' : information.delete_from_course,
                                    'course' : information.delete_course
                                    },
                        'info':     {
                                    'docent' : information.info_docent,
                                    'participant' : information.info_participant,
                                    'course' : information.info_course
                                    }
                        }

        states[action][target](*args)

    except ValueError as e:
        print(e)
    except OverflowError as e:
        print(e)
    except IndexError:
        print('the query is not full')
    except TypeError:
        print('the query is not full')
    except Exception as e:
        print('something gone wrong')

j: dict = information.get_dict()

if j:
    with open('data.json', "w") as f:
        json.dump(j, f, indent=4)