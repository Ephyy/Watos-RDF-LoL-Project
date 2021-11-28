class Champion:
    
    """
    Class Champion
    
    """

    def __init__(self, name, attack, defense, magic, difficulty,
                 primary_position, info, key, partype,
                 playstyle, region, relation, tags,
                version):
        self.name = name
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.difficulty = difficulty
        self.primary_position = primary_position
        self.info = info
        self.key = key
        self.partype = partype
        self. playstyle = playstyle
        self.region = region
        self.relation = relation
        self.tags = tags
        self.version = version
        
    
    def rdfs_class_type(self):
        return f'ex:{self.name} ex:type ex:Champion'
    
    def rdfs_primary_position(self):
        return f'ex:primaryPosition ex:{self.primary_position}'
    
    def rdfs_region(self):
        return f'ex:region ex:{self.region}'
    
    
    
    def rdf_champ(self):
        
        """
        Create RDF for a Champion
        
        """
        
        print(f'''{self.rdfs_class_type()}
              \t {self.rdfs_primary_position()}
              \t {self.rdfs_region()}
              '''
              
              )
        

def create_champion(dict_info):
    
    """
    create a champion object from a dictionary
    
    :param dict_info: dictionary with the champion information
    
    :return champion: champion object
    
    """
    
    name = dict_info['name']
    attack = dict_info['info']['attack']
    defense = dict_info['info']['defense']
    magic = dict_info['info']['magic']
    difficulty = dict_info['info']['difficulty']
    primary_position = dict_info["PrimaryPosition"]
    info = dict_info['info']
    key = dict_info['key']
    partype = dict_info['partype']
    playstyle = dict_info['playstyle'] if 'playstyle' in dict_info else ""
    region = dict_info['region']
    relation = dict_info['relation']
    tags = dict_info['tags']
    version = dict_info['version']
    
    return Champion(name, attack, defense, magic, difficulty,
                    primary_position, info, key, partype,
                    playstyle, region, relation, tags,
                    version)

def json_to_champion(json_champ):
    
    """
    create a list of champion objects from a json file
    
    :param json_champ: json file with the champions information
    
    :return champions: list of champion objects
    
    """
    
    list_champ = []
    for champ in json_champ:
        list_champ.append(create_champion(json_champ[champ]))
        
    return list_champ