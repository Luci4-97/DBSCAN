import DBSCAN

##################################################
#                                                #
#                测试数据： smile.csv              #
#                半径大小： 0.05                   #
#                最少个数： 6                      #
#                                                #
#               dbscan实现见DBSCAN.py             #
##################################################

db = DBSCAN.dbscan(False)
db.feed('./data/smile.csv')
db.cluster(0.05, 6)

# db.feed('./data/long.csv')
# db.cluster(0.2, 3)

# db.feed('./data/moon.csv')
# db.cluster(0.2, 3)

# db.feed('./data/sizes5.csv')
# db.cluster(1.1, 10)

# db.feed('./data/spiral.csv')
# db.cluster(0.2, 3)

# db.feed('./data/square1.csv')
# db.cluster(1, 5)
