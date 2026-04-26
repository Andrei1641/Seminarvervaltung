# Seminarverwaltung

## Commands-Syntax

## Contents

- [Create](#create-syntaxcreate-new-objects)
- [Add](#add-syntaxadd-person-to-course)
- [Show](#show-syntaxshow-object-names-or-person-names-inside-course)
- [Delete](#delete-syntaxdelete-course-person-from-course-person-completely)
- [Info](#info-syntaxshows-detailed-information-about-object)

### Create-Syntax(create new objects)

```
<type> create
type: {participant | docent | couse}
```

### Add-Syntax(add person to course)
```
<person_type> add "Second_name First_name" "Title"
person_type: {participant | docent}
```

### Show-Syntax(show object names or person names inside course)

```
<type> show [arguments]
type: {participant | docent | course}
```

#### [arguments]:
#### show person

```
course show person 
```
 
### Delete-Syntax(delete course, person from course, person completely)

```
<type> delete [arguments]
type: {participant | docent | course}
```

#### [arguments]:
#### delete from_db

```
<person_type> delete from_db "Second_name First_name"
person_type: {participant | docent}
```

#### delete from_course

```
<person_type> delete from_course "Second_name First_name" "Title"
person_type: {participant | docent}
```

#### delete course

```
course delete "Title"
```

### Info-Syntax(shows detailed information about object)

```
<type> info "<name>"
type: {participant | docent | course}
name: {Second_name First_name | Title}
```