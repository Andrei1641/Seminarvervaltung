from classes.person_classen import Docent, Participant


class PersonFactory:

    @staticmethod
    def __name_check(name: str) -> str:
        if not name.strip():
            raise ValueError('name can not be empty')

        for i in name:
            if i.isdigit():
                raise ValueError('name can not consist digit')

        name = name.strip()
        name = name.capitalize()
        return name

    @staticmethod
    def __email_check(email: str) -> str:

        if not email.strip():
            raise ValueError('email can not be empty')

        if '@' not in email:
            raise ValueError('please enter the correct email-address')
        return email.lower()

    @staticmethod
    def __theme_check(theme: list[str]):
        if not theme:
            raise ValueError('this dozent can not learn')
        return theme

    @staticmethod
    def __persons_adjustments(first_name: str, second_name: str, email_address: str):
        first_name = PersonFactory.__name_check(first_name)
        second_name = PersonFactory.__name_check(second_name)
        email_address = PersonFactory.__email_check(email_address)

        return first_name, second_name, email_address


    @staticmethod
    def create_docent(first_name: str, second_name: str, email_address: str, list_an_themes: list[str]) -> Docent:

        first_name, second_name, email_address = PersonFactory.__persons_adjustments(first_name, second_name, email_address)
        list_an_themes = PersonFactory.__theme_check(list_an_themes)

        return Docent(first_name, second_name, email_address, list_an_themes)

    @staticmethod
    def create_participant(first_name: str, second_name: str, email_address: str) -> Participant:

        first_name, second_name, email_address = PersonFactory.__persons_adjustments(first_name, second_name, email_address)

        return Participant(first_name, second_name, email_address)


