# Commands Test

## Create "person"

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

