import os

class Champion:
    
    """
    Class Champion
    
    """

    def __init__(self, key_name, attack, defense, magic, difficulty,
                 primary_position, secondary_position, third_position, 
                 info, key, partype, playstyle, region, relation, tags,
                 releaseDate
                ):
        
        self.key_name = key_name
        self.attack = attack
        self.defense = defense
        self.magic = magic
        self.difficulty = difficulty
        self.primary_position = primary_position
        self.secondary_position = secondary_position
        self.third_position = third_position
        self.info = info
        self.key = key
        self.partype = partype
        self.playstyle = playstyle
        self.region = region
        self.relation = relation
        self.tags = tags
        self.releaseDate = releaseDate
        
    
    def rdfs_class_type(self):
        return f'ex:{self.key_name} a ex:Champion ;'
    
    def rdfs_primary_position(self):
        return f'ex:primaryPosition ex:{self.primary_position} ;'
    
    def rdfs_secondary_position(self):
        return f'ex:secondaryPosition ex:{self.secondary_position} ;'
    
    def rdfs_third_position(self):
        return f'ex:thirdPosition ex:{self.third_position} ;'
    
    def rdfs_region(self):
        return f'ex:region ex:{self.region} ;'
    
    def rdfs_key(self):
        return f'ex:key ex:{self.key} ;'
    
    def rdfs_info(self):
        
        text = ''
        for info in self.info:
            text += f'ex:{info} \"{self.info[info]}\"^^xsd:int ;'
            
        return f'ex:info [ {text} ] ;'
    
    def rdfs_tags(self):
        
        tags = ''
        for tag in self.tags:
            tags += f'ex:{tag} , '
        
        return f'ex:tags {tags[:-2]} ;'
    
    def rdfs_relation(self):
        
        if self.relation != []:
            relations = ''
            for relation in self.relation:
                relations += f'ex:{relation} , '
            
            return f'ex:relation {relations[:-2]} ;'
    
    def rdfs_name(self):
        return f'ex:name ex:{self.name}'

    def rdfs_partype(self):
        return f'ex:partype ex:{self.partype} ;'
    
    def rdfs_playstyle(self):
        return f'ex:playStyle ex:{self.playstyle} ;'

    def rdfs_partype(self):
        return f'ex:partype ex:{self.partype} ;'
    
    def rdfs_realeaseDate(self):
        return f'ex:releaseDate \"{self.releaseDate}\"^^xsd:date .'
    
    def rdf_champ(self):
        
        """
        Create RDF for a Champion
        
        """
        
        text = f'''{self.rdfs_class_type()}
        {self.rdfs_primary_position()}
        {self.rdfs_secondary_position() if self.secondary_position != '' else ''}
        {self.rdfs_third_position() if self.rdfs_third_position != '' else ''}
        {self.rdfs_region()}
        {self.rdfs_partype()}
        {self.rdfs_playstyle()}
        {self.rdfs_relation() if self.relation != [] else ''}
        {self.rdfs_tags()}
        {self.rdfs_realeaseDate()}
              '''
              
        lines = text.split("\n")
        text = [line for line in lines if line.strip() != ""]
        final_text = ""

        for line in text:
            final_text += line + "\n"
            
        print(final_text)
        

def create_champion(champ, dict_info):
    
    """
    create a champion object from a dictionary
    
    :param dict_info: dictionary with the champion information
    
    :return champion: champion object
    
    """
    
    key_name = champ
    attack = dict_info['info']['attack']
    defense = dict_info['info']['defense']
    magic = dict_info['info']['magic']
    difficulty = dict_info['info']['difficulty']
    primary_position = dict_info["PrimaryPosition"]
    secondary_position = dict_info["SecondaryPosition"] if 'SecondaryPosition' in dict_info else ''
    third_position = dict_info["ThirdPosition"] if 'ThirdPosition' in dict_info else ''
    info = dict_info['info']
    key = dict_info['key']
    partype = dict_info['partype']
    playstyle = dict_info['playstyle'] if 'playstyle' in dict_info else ""
    region = dict_info['region']
    relation = dict_info['relation']
    tags = dict_info['tags']
    releaseDate = dict_info['releaseDate']
    
    return Champion(key_name, attack, defense, magic, difficulty,
                    primary_position, secondary_position, third_position,
                    info, key, partype,playstyle, region,
                    relation, tags, releaseDate
                    )

def json_to_champion(json_champ):
    
    """
    create a list of champion objects from a json file
    
    :param json_champ: json file with the champions information
    
    :return champions: list of champion objects
    
    """
    
    list_champ = []
    for champ in json_champ:
        list_champ.append(create_champion(champ, json_champ[champ]))
        
    return list_champ