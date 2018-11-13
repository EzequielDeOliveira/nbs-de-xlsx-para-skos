import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef

file = 'NBS-e-NEBS-em-excel.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

nebs = xl.parse('NEBS')

graph = Graph()
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
graph.bind('skos', skos)
i = 0
for a in range(len(nebs)):
    i += 1
    uri = 'http://vocab.mdic.gov.br/NBS/v2.0/#' + ......
    graph.add((URIRef(uri), RDF['type'], skos['Concept']))
    graph.add((URIRef(uri), skos['prefLabel'], Literal(nebs.DESCRIÇÃO.get(a), lang='pt-br')))
   """  graph.add((URIRef(uri), skos['broader'], Literal(nebs.NBS2.get(a), lang='pt-br'))) """
    graph.add((URIRef(uri), skos['related'], URIRef('URI-Related')))

print(graph.serialize(format='pretty-xml'))

file = open('testfile.xml','w') 

file.write(str(graph.serialize(format='pretty-xml')))

print(i)