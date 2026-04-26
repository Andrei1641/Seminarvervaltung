import json

from collector import Information
import shlex

from managers import ParticipantManager, CourseManager, DocentManager, Manager

curse_manager = CourseManager()
docent_manager = DocentManager(curse_manager.get_db())
participant_manager = ParticipantManager(curse_manager.get_db())

managers: list = [curse_manager, docent_manager, participant_manager]

information = Information(managers)

information.deserialize()

while True:
    try:
        query: str = str(input('write your query: ')).strip()

        query_modules: list[str] = shlex.split(query)

        if not query_modules:
            raise ValueError('query can not be empty')

        t = query_modules[0]

        if t == 'save':
            information.serialize()
            continue
        if t == 'end':
            information.serialize()
            break

        if len(query_modules) < 2:
            raise ValueError('incorrect query')

        args = query_modules[1:]

        information.find_manager(t, *args)
    except ValueError as e:
        print(e)
    except OverflowError as e:         #?
        print(e)
    except Exception:
        print("something gone wrong")