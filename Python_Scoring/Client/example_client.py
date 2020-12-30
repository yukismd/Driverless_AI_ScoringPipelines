# Copyright 2020 H2O.ai; Proprietary License;  -*- encoding: utf-8 -*-

import sys

sys.path.append('gen-py')

from numpy import nan
from thrift.transport import TSocket
from thrift.transport import TTransport
from thrift.protocol import TBinaryProtocol

from h2oai_scoring import ScoringService
from h2oai_scoring.ttypes import Row

# ----------------------------------------------------------
# Name   Type      Range                                    
# ----------------------------------------------------------
# x1     float32   [-3.0065999031066895, 2.7874999046325684]
# x2     float32   [-4.136000156402588, 3.256700038909912]  
# x3     float32   [-3.0952999591827393, 3.3822999000549316]
# x4     float32   [-3.42330002784729, 3.0445001125335693]  
# ----------------------------------------------------------

socket = TSocket.TSocket('localhost', 9090)
transport = TTransport.TBufferedTransport(socket)
protocol = TBinaryProtocol.TBinaryProtocol(transport)
client = ScoringService.Client(protocol)
transport.open()

server_hash = client.get_hash()
print('Scoring server hash: '.format(server_hash))

print('Scoring individual rows...')
row1 = Row()
row1.x1 = '-2.631500005722046'  # x1
row1.x2 = '-2.277899980545044'  # x2
row1.x3 = '-2.7997000217437744'  # x3
row1.x4 = '-2.3194000720977783'  # x4

row2 = Row()
row2.x1 = '-2.4870998859405518'  # x1
row2.x2 = '-2.550600051879883'  # x2
row2.x3 = '-2.9811999797821045'  # x3
row2.x4 = '-2.3696999549865723'  # x4

row3 = Row()
row3.x1 = '-2.5062999725341797'  # x1
row3.x2 = '-4.136000156402588'  # x2
row3.x3 = '-2.7997000217437744'  # x3
row3.x4 = '-2.3696999549865723'  # x4

row4 = Row()
row4.x1 = '-2.6043999195098877'  # x1
row4.x2 = '-2.3060998916625977'  # x2
row4.x3 = '-2.5227999687194824'  # x3
row4.x4 = '-2.4237000942230225'  # x4

row5 = Row()
row5.x1 = '-2.4442999362945557'  # x1
row5.x2 = '-2.550600051879883'  # x2
row5.x3 = '-2.9811999797821045'  # x3
row5.x4 = '-2.3696999549865723'  # x4

score1 = client.score(row1, pred_contribs=False, output_margin=False)
print(score1)
score2 = client.score(row2, pred_contribs=False, output_margin=False)
print(score2)
score3 = client.score(row3, pred_contribs=False, output_margin=False)
print(score3)
score4 = client.score(row4, pred_contribs=False, output_margin=False)
print(score4)
score5 = client.score(row5, pred_contribs=False, output_margin=False)
print(score5)

print('Scoring multiple rows...')
rows = [row1, row2, row3, row4, row5]
scores = client.score_batch(rows, pred_contribs=False, output_margin=False)
print(scores)

print('Retrieve column names')
print(client.get_column_names())

print('Retrieve transformed column names')
print(client.get_transformed_column_names())

print('Retrieve target labels') # will be not empty only for classification problems
print(client.get_target_labels())

transport.close()


