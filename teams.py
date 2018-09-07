def differentTeams(skills):
    skills = skills.strip()
        
    skills_count = {
        'p': 0,
        'c': 0,
        'm': 0,
        'b': 0,
        'z': 0,
    }
    
    for skill in skills_count.keys():
        skills_count[skill] = skills.count(skill)
    return min(skills_count.values())
