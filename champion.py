class Champion:

    def __init__(self, name, health, damage,
                 primary_position, info, key, partype,
                 playstyle, region, relation, tags,
                 title, version):
        self.name = name
        self.health = health
        self.damage = damage
        self.primary_position = primary_position
        self.info = info
        self.key = key
        self.partype = partype
        self. playstyle = playstyle
        self.region = region
        self.relation = relation
        self.tags = tags
        self.title = title
        self.version = version
        

def create_champion(dict_info):
    
    name = dict_info['name']
    health = dict_info['stats']['hp']
    damage = dict_info['stats']['attackdamage']
    primary_position = dict_info["PrimaryPosition"]
    info = dict_info['info']
    key = dict_info['key']
    partype = dict_info['partype']
    playstyle = dict_info['playstyle'] if 'playstyle' in dict_info else ""
    region = dict_info['region']
    relation = dict_info['relation']
    tags = dict_info['tags']
    title = dict_info['title']
    version = dict_info['version']
    
    return Champion(name, health, damage,
                    primary_position, info, key, partype,
                    playstyle, region, relation, tags,
                    title, version)

def json_to_champion(json_champ):
    
    list_champ = []
    for champ in json_champ:
        print(champ)
        list_champ.append(create_champion(json_champ[champ]))