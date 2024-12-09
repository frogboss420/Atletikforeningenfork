from operator import truediv

from pysondb import db

medlemmer = db.getDb('medlemmer.json')
tilmeldinger = db.getDb('tilmeldinger.json')

# Denne funktion genererer en string ud fra en tabel i pysonDB-format i mere læsbart format
def table_to_text(table):
    out = ''
    for row in table:
        for field in row.values():
            out += str(field) + '\t'
        out += '\n'
    return out

# Denne funktion returnerer en liste af hold fra tabellen 'Tilmeldinger' uden dubletter
def find_unique_teams():
    data = tilmeldinger.getAll()
    disc = []
    for row in data:
        if row['Disciplin'] not in disc:
            disc.append(row['Disciplin'])
    return disc

# Denne funktion returnerer en liste af navne, som har en tilmelding på den valgte disciplin
def generate_team_list(discipline):
    #dataTilmeldinger = tilmeldinger.getAll()
    #dataMedlemmer = medlemmer.getAll()
    #medlemmerId = []
    #out = []
    #for i in dataTilmeldinger:
    #    if i['Disciplin'] == discipline:
    #        medlemmerId.append(i['Medlem'])
    #for i in dataMedlemmer:
    #    if i['Medlemsnummer'] in medlemmerId:
    #        out.append(i['Navn'])
    #return out
    t=tilmeldinger.getBy({'Disciplin':discipline})
    team_list=[]
    for row in t:
        m=medlemmer.getBy({'Medlemsnummer':row['Medlem']})
        team_list.append(m[0]['Navn'])
    return team_list

# Denne funktion tilføjer et medlem til tabellen 'Medlemmer'
def add_member(name, birthdate, fee):
    nummer=len(medlemmer.getAll())+1
    found = False
    for medlem in medlemmer.getAll():
        if medlem['Navn'] == name and medlem['Fødselsdag']==birthdate and medlem['Kontingent']==fee:
            found = True
            break
    if not found:
        medlemmer.add({'Medlemsnummer':nummer, 'Navn':name, 'Fødselsdag':birthdate, 'Kontingent': fee})

# Denne funktion tilføjer en tilmelding til tabellen 'Tilmeldinger'
def add_participant(member_id, discipline, is_coach):
    found = False
    for entry in tilmeldinger.getAll():
        if entry['Medlem']==member_id and entry['Disciplin']==discipline:
            found = True
            break
    if not found:
        tilmeldinger.add({'Medlem':member_id,'Disciplin':discipline,'Træner':is_coach})

# Denne funktion skifter et medlems "Coach" status
def modifyMember(member_id):
    for entry in tilmeldinger.getAll()
        if entry['id'] == member_id:
            tilmeldinger.update({'Træner':false,'Disciplin':''}, {})



if __name__ == '__main__':
    print(table_to_text(medlemmer.getAll()))
    print(table_to_text(tilmeldinger.getAll()))

    ## Test af løsning på opgaver ##

    # Find og print discipliner
    hold = find_unique_teams()
    print(hold)

    # Print holdlister
    for h in hold:
        print(h)
        print(generate_team_list(h))

    # Tilføj medlemmer
    add_member('Alidia McGoon', '1950-10-17', 150)
    add_member('Osgood Tollet', '1979-09-30', 200)

    # Meld medlemmer på disciplin
    add_participant(9, 'Kapgang', True)
    add_participant(10, 'Kapgang', False)