import random

# Given some email ids, and a similarity function which says whether two email ids are similar, determine all the sets of email ids that are similar to each other.

# Given
# in_email_set = list of strings
# email_is_similar(one, another)

class StringTrees:
    def __init__(self, str_list):
        self.treedict={}
        for s in str_list:
            self.treedict[ s ] = s

    def printme(self):
        roots = []
        for parent in self.treedict:
            roots.append(self.root(parent))
        for i, r in enumerate(roots):
            print('tree #', i, 'root:', r)
            self.print_subtree(r)

    def return_childs(self, parent):
        r=[]
        for child, p in self.treedict.items():
            if parent == p:
                r.append(child)
        return r

    def print_subtree(self, root):
        childs_list=self.return_childs(root)
        if len(childs_list)==1:
            print(root)
            return
        for child in childs_list:
            self.print_subtree(child)

    def root(self, child):
        while self.treedict[child] != child:
            child = self.treedict[child]
        return child

    def is_connected(self, one, another):
        return self.treedict.root(one) == self.treedict.root(another)

    def union(self, one, another):
        self.treedict[self.root(one)] = self.treedict[self.root(another)]
       # print(self.emails)

# Given stubs
in_emails = ('a', 'b','c', 'b', 'b')
def email_is_similar(e1, e2):
    print('comparing ' + e1 + ' and ' + e2)
    #return random.uniform(0,1) >= 0.5
    #return e1==e2
    return e1==e2

st = StringTrees(in_emails)

#out_sets = in_sets[:]

for i, e in enumerate(in_emails[:-2]):
    for j, other_e in enumerate(in_emails[ i+1 : ]):
        if email_is_similar(e, other_e):
            print(e, '=', other_e)
            st.union(e, other_e)

st.printme()

print(st.treedict)