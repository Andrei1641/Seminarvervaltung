# Seminarverwaltung

## Commands-Syntax

## Contents

- [Create](#create)
- [Add](#add)
- [Show](#show)
- [Delete](#delete)
- [Info](#info)

### Create-Syntax(create new objects) {#create}

```
create <type>
type: {participant | docent | couse}
```

### Add-Syntax(add person to course) {#add}
```
add <person_type> "Second_name First_name" "Title"
person_type: {participant | docent}
```

### Show-Syntax(show object names or person names inside course) {#show}

```
show <scope> [arguments]
scope: {all | course}
```

#### [arguments]:
#### show all

```
show all <type>
type: {participant | docent | course}
```

#### show course

```
show course <person_type> "Title"
person_type: {participant | docent}
```
 
### Delete-Syntax(delete course, person from course, person completely) {#delete}

```
delete <scope> [arguments]
scope: {from_db | from_course | course}
```

#### [arguments]:
#### delete from_db

```
delete from_db <person_type> "Second_name First_name"
person_type: {participant | docent}
```

#### delete from_course

```
delete from_course <person_type> "Second_name First_name" "Title"
person_type: {participant | docent}
```

#### delete course

```
delete course "Title"
```

### Info-Syntax(shows detailed information about object) {#info}

```
info <type> "<name>"
type: {participant | docent | course}
name: {Second_name First_name | Title}
```