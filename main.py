from campus import CampusEPN


campus_epn = CampusEPN()

print(campus_epn.graph.bfs_camino("14", "44"))
print(campus_epn.graph.dfs_camino("22","35"))
