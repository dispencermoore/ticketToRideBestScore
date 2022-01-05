import networkx as nx
import matplotlib.pyplot as plt

# python program to determine the best possible score, considering 45 max trains
trainsLeft = 45
trainPoints = 0
weightToPointConversion = [0,1,2,4,7,10,15]
destinationPoints = 0
destinationsMade = []
cities = ['VA', 'CA', 'WI', 'SSM', 'MO', 'SE', 'HE', 'DU', 'TO', 'BO', 'PO', 'SLC', 'DE', 'OM', 'CH', 'PI', 'NY', 'SF',
          'LV', 'SFE', 'OC', 'KC', 'SL', 'NA', 'RA', 'WA', 'LA', 'PH', 'EP', 'DA', 'LR', 'AT', 'CHA', 'HO', 'NO', 'MI']
connectionsWithCost = [('VA', 'CA', {"weight": 3}), ('VA', 'SE', {"weight": 1}), ('CA', 'WI', {"weight": 6}),
                       ('CA', 'SE', {"weight": 4}), ('CA', 'HE', {"weight": 4}), ('WI', 'SSM', {"weight": 6}),
                       ('WI', 'HE', {"weight": 4}), ('WI', 'DU', {"weight": 4}), ('SSM', 'MO', {"weight": 5}),
                       ('SSM', 'DU', {"weight": 3}), ('SSM', 'TO', {"weight": 2}), ('MO', 'TO', {"weight": 3}),
                       ('MO', 'BO', {"weight": 2}), ('MO', 'NY', {"weight": 3}), ('SE', 'PO', {"weight": 1}),
                       ('SE', 'HE', {"weight": 6}), ('HE', 'DU', {"weight": 6}), ('HE', 'SLC', {"weight": 3}),
                       ('HE', 'DE', {"weight": 4}), ('HE', 'OM', {"weight": 4}), ('DU', 'TO', {"weight": 6}),
                       ('DU', 'OM', {"weight": 2}), ('DU', 'CH', {"weight": 3}), ('TO', 'CH', {"weight": 4}),
                       ('TO', 'PI', {"weight": 2}), ('BO', 'NY', {"weight": 2}), ('NY', 'PI', {"weight": 2}),
                       ('NY', 'WA', {"weight": 2}), ('WA', 'PI', {"weight": 2}), ('WA', 'RA', {"weight": 2}),
                       ('RA', 'CHA', {"weight": 2}), ('CHA', 'MI', {"weight": 4}), ('VA', 'CA', {"weight": 3}),
                       ('RA', 'PI', {"weight": 2}), ('RA', 'NA', {"weight": 3}), ('RA', 'AT', {"weight": 2}),
                       ('CHA', 'AT', {"weight": 2}), ('AT', 'MI', {"weight": 5}), ('MI', 'NO', {"weight": 6}),
                       ('AT', 'NA', {"weight": 1}), ('AT', 'NO', {"weight": 4}), ('PI', 'CH', {"weight": 3}),
                       ('PI', 'NA', {"weight": 4}), ('PI', 'SL', {"weight": 5}), ('SL', 'NA', {"weight": 2}),
                       ('NA', 'LR', {"weight": 3}), ('CH', 'SL', {"weight": 2}), ('CH', 'OM', {"weight": 4}),
                       ('SL', 'LR', {"weight": 2}), ('SL', 'KC', {"weight": 2}), ('LR', 'NO', {"weight": 3}),
                       ('NO', 'HO', {"weight": 2}), ('LR', 'DA', {"weight": 2}), ('LR', 'OC', {"weight": 2}),
                       ('HO', 'DA', {"weight": 1}), ('DA', 'OC', {"weight": 2}), ('OC', 'KC', {"weight": 2}),
                       ('KC', 'OM', {"weight": 1}), ('KC', 'DE', {"weight": 4}), ('OM', 'DE', {"weight": 4}),
                       ('OC', 'DE', {"weight": 4}), ('OC', 'SFE', {"weight": 3}), ('OC', 'EP', {"weight": 5}),
                       ('DA', 'EP', {"weight": 4}), ('EP', 'HO', {"weight": 6}), ('EP', 'SFE', {"weight": 2}),
                       ('SFE', 'DE', {"weight": 2}), ('EP', 'PH', {"weight": 3}), ('EP', 'LA', {"weight": 6}),
                       ('SFE', 'PH', {"weight": 3}), ('DE', 'PH', {"weight": 5}), ('DE', 'SLC', {"weight": 3}),
                       ('PH', 'LA', {"weight": 3}), ('PO', 'SLC', {"weight": 6}), ('SLC', 'LV', {"weight": 3}),
                       ('LV', 'LA', {"weight": 2}), ('SLC', 'SF', {"weight": 5}), ('SF', 'LA', {"weight": 3}),
                       ('SF', 'PO', {"weight": 5})]
destinations = [['CH', 'AT', 5], ['LA', 'AT', 15], ['MO', 'AT', 9], ['NY', 'AT', 6], ['SF', 'AT', 17],
                ['WA', 'AT', 4], ['CH', 'BO', 7], ['KC', 'BO', 11], ['PH', 'BO', 19], ['LA', 'CA', 12],
                ['TO', 'CHA', 6], ['LA', 'CH', 16], ['MO', 'CH', 7], ['SLC', 'CH', 11], ['DU', 'DA', 7],
                ['MO', 'DA', 13], ['VA', 'DE', 11], ['VA', 'DU', 13], ['DE', 'EP', 4], ['DU', 'EP', 10],
                ['DU', 'HO', 8], ['KC', 'HO', 5], ['PO', 'HO', 8], ['WI', 'HO', 12], ['SLC', 'KC', 7],
                ['SE', 'LV', 10], ['WI', 'LR', 11], ['HE', 'LA', 8], ['SE', 'LA', 9], ['BO', 'MI', 12],
                ['LV', 'MI', 21], ['LA', 'MI', 19], ['NY', 'MI', 10], ['SL', 'MI', 8], ['SSM', 'MI', 12],
                ['TO', 'MI', 10], ['VA', 'MO', 20], ['CA', 'NA', 14], ['PO', 'NA', 17], ['SSM', 'NA', 8],
                ['CH', 'NO', 7], ['MO', 'NO', 13], ['OM', 'NO', 8], ['PI', 'NO', 8], ['SE', 'NO', 20],
                ['CH', 'NY', 5], ['DA', 'NY', 11], ['LV', 'NY', 19], ['LA', 'NY', 20], ['NA', 'NY', 6],
                ['LA', 'OC', 9], ['SSM', 'OC', 8], ['SE', 'OC', 14], ['WI', 'OM', 6], ['CA', 'PH', 13],
                ['PO', 'PH', 11], ['DE', 'PI', 11], ['PO', 'PI', 19], ['VA', 'PO', 2], ['MO', 'RA', 7],
                ['DE', 'SL', 6], ['CA', 'SLC', 7], ['CH', 'SFE', 9], ['VA', 'SFE', 13], ['WI', 'SFE', 10],
                ['SF', 'SSM', 17], ['BO', 'WA', 4], ['HO', 'WA', 10], ['SF', 'WA', 21]]


def getPoints(destination):
    return destination[2]


destinations.sort(reverse=True, key=getPoints)  # want them in order of most points
tMap = nx.Graph() # initial map with all cities/etc
fMap = nx.Graph() # final map with only cities/paths used
tMap.add_nodes_from(cities)
tMap.add_edges_from(connectionsWithCost)
# print(nx.dijkstra_path(tMap, 'LA', 'MI'))
# print(nx.dijkstra_path_length(tMap, 'LA', 'MI'))
# print(nx.johnson(tMap)['VA']) #johnson gets the shortest path of all nodes to all nodes, look at specific nodes though
# could use a greedy algorithm on the list of destinations??
allShortestPaths = nx.johnson(tMap)
firstDest = True
for destination in destinations: # first destination is special, since fmap starts empty
    if (trainsLeft <= 0):
        break
    print("Doing destination: ", destination)
    source = destination[0]
    target = destination[1]
    path = allShortestPaths[source][target]
    pathT = path
    pathS = path
    currentLength = nx.dijkstra_path_length(tMap, source, target)
    currentLengthTarget = currentLength
    for city in fMap.nodes: # get distance to target
        possibleNewLenT = nx.dijkstra_path_length(tMap, city, target)
        if (possibleNewLenT < currentLengthTarget):
            #source = city
            currentLengthTarget = possibleNewLenT
            pathT = allShortestPaths[city][target]
    currentLengthSource = currentLength
    for city in fMap.nodes: # get distance to source
        possibleNewLenS = nx.dijkstra_path_length(tMap, city, source)
        if (possibleNewLenS < currentLengthSource):
            #source = city
            currentLengthSource = possibleNewLenS
            pathS = allShortestPaths[city][source]
    if (currentLengthSource + currentLengthTarget >= trainsLeft):
        continue
    destinationPoints += destination[2]
    destinationsMade.append(destination)
    print("Path to target: ", pathT)
    for i in range(0,len(pathT)-1):
        weight = -1
        for edge in connectionsWithCost:
            if edge[0] == pathT[i] and edge[1] == pathT[i+1]:
                weight = edge[2]['weight']
            if edge[1] == pathT[i] and edge[0] == pathT[i+1]:
                weight = edge[2]['weight']
        fMap.add_edge(pathT[i],pathT[i+1], weight=weight)
        #print("Edge added between ", pathT[i], " and ", pathT[i+1])
        trainsLeft -= weight
        trainPoints += weightToPointConversion[weight]
    if not firstDest:
        print("Path to source: ",pathS)
        for i in range(0,len(pathS)-1):
            weight = -1
            for edge in connectionsWithCost:
                if edge[0] == pathS[i] and edge[1] == pathS[i+1]:
                    weight = edge[2]['weight']
                if edge[1] == pathS[i] and edge[0] == pathS[i+1]:
                    weight = edge[2]['weight']
            fMap.add_edge(pathS[i],pathS[i+1], weight=weight)
            #print("Edge added between ", pathS[i], " and ", pathS[i + 1])
            trainsLeft -= weight
            trainPoints += weightToPointConversion[weight]
    else:
        firstDest = False
print(trainsLeft)
print("Points earned:")
print(destinationPoints+trainPoints)
print("With these destinations:")
print(destinationsMade)
pos=nx.planar_layout(fMap)
nx.draw(fMap, pos, with_labels=True, font_weight='bold')
edge_weight = nx.get_edge_attributes(fMap,'weight')
nx.draw_networkx_edge_labels(fMap, pos, edge_labels = edge_weight)
plt.show()
