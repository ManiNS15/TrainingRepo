__author__ = 'Manitra.Rakotozafy'


def all_attributes_value(sampleBase):
    attributes ={}
    for item in sampleBase:
        for att in item:
            if not(attributes.__contains__(att)):
                attributes[att] = {}
            if not(attributes[att].__contains__(item[att])):
                attributes[att][item[att]] = 0
    return attributes

def all_attributes_value_except_t_att(sampleBase,t_att):
    attributes ={}
    for item in sampleBase:
        for att in item:
            if att != t_att :
                if not(attributes.__contains__(att)):
                    attributes[att] = {}
                if not(attributes[att].__contains__(item[att])):
                    attributes[att][item[att]] = 0
    return attributes

def collect_all_attribute(sampleBase):
    attributes =[]
    for item in sampleBase:
        for att in item:
            if not(attributes.__contains__(att)):
                attributes.append(att)
    return attributes

def regroup_by_t_att_value(sampleBase,t_att):
    attributes_value = all_attributes_value_except_t_att(sampleBase,t_att)
    t_att_r = {}
    for item in sampleBase:
        for att in item:
            if (att == t_att and not(t_att_r.__contains__(item[att]))):
                t_att_r[item[att]] = {}
    for key in t_att_r:
        for att in attributes_value:
            t_att_r[key][att] =  attributes_value[att]

    return t_att_r


def regroup_by_t_att_value_and_count(sampleBase,t_att):

    attributes_value = all_attributes_value_except_t_att(sampleBase,t_att)
    t_att_r = {}
    for item in sampleBase:
        for att in item:
            if (att == t_att and not(t_att_r.__contains__(item[att]))):
                t_att_r[item[att]] = {}
    for key in t_att_r:
        for att in attributes_value:
            t_att_r[key][att] =  attributes_value[att]
    i=-1
    for row in sampleBase:
        i+=1
        for att in row:
            if att != t_att:
                t_att_r[row[t_att]][att][sampleBase[i][att]] += 1

    return t_att_r
