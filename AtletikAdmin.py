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
    pass

# Denne funktion returnerer en liste af navne, som har en tilmelding på den valgte disciplin
def generate_team_list(discipline):
    pass

# Denne funktion tilføjer et medlem til tabellen 'Medlemmer'
def add_member(name, birthdate, fee):
    pass

# Denne funktion tilføjer en tilmelding til tabellen 'Tilmeldinger'
def add_participant(member_id, discipline, is_coach):
    pass


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