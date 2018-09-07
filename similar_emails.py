import random

# Given some email ids, and a similarity function which says whether two email ids are similar, determine all the sets of email ids that are similar to each other.

# Given
# in_email_set = list of strings
# email_is_similar(one, another)

class SimilarEmails:    
    def __init__(self, email):
        self.emails = [email]
    
    def __str__(self):
        return ','.join(self.emails)
    
    def is_similar_to(self, other_emails):
        for e in self.emails:
            for other_e in other_emails.emails:
                if email_is_similar(e, other_e):
                    return True
        return False
    
    def join(self, other_emails):
        self.emails += other_emails.emails
       # print(self.emails)
                   
        
# Given stubs
in_emails = ('a', 'b','c', 'b', 'b')
def email_is_similar(e1, e2):
    print('comparing ' + e1 + ' and ' + e2)
    #return random.uniform(0,1) >= 0.5
    return e1==e2

def print_res():
    print('result')
    for line in in_sets:
        print(line)
        

in_sets = []
for e in in_emails:
    in_sets.append(SimilarEmails(e))
    
#out_sets = in_sets[:]

# for index, element in enumerate(in_emails):
for e in in_sets:
    for j, other_e in enumerate(in_sets):
        print('values', e, ' ', other_e)
        if e == other_e:
            continue
        if e.is_similar_to(other_e):
            print(e, '=', other_e)
            e.join(other_e)
            in_sets.pop(j)

print_res()
