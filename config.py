def parse_config(cfgfile):
    file = open(cfgfile, 'r')
    lines = file.read().split('\n')     #store the lines in a list
    lines = [x for x in lines if len(x) > 0] #get read of the empty lines 
    lines = [x for x in lines if x[0] != '#']  
    lines = [x.rstrip().lstrip() for x in lines]
    config = []
    count = 0
    for x in lines:
        if x[0] == '[':
            count += 0
            key = x.replace('[','').replace(']','')
            config.append({key:dict()})
        else:
            tmp = x.split('=')
            tmp[1] = tmp[1].rstrip().lstrip()
            vector = []
            for i in tmp[1].split(','):
                try:
                    j = int(i)
                except:
                    try:
                        j = float(i)
                    except:
                        j = i
                vector.append(j)
            if len(vector) > 1:
                config[count-1][key][tmp[0].rstrip().lstrip()] = vector
            else:
                config[count-1][key][tmp[0].rstrip().lstrip()] = vector[0]
    return config
