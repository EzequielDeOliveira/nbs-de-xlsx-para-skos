import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef

file = 'NBS-e-NEBS-em-excel.xlsx'

xl = pd.ExcelFile(file)

print(xl.sheet_names)

nebs = xl.parse('NEBS')

graph = Graph()
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
graph.bind('skos', skos)

for a in range(0, 1236):
    graph.add((URIRef('URI'), RDF['type'], skos['Concept']))
    graph.add((URIRef('URI'), skos['prefLabel'], Literal(nebs.DESCRIÇÃO.get(a), lang='pt-br')))
    graph.add((URIRef('URI'), skos['prefLabel'], Literal(nebs.NBS2.get(a), lang='pt-br')))
    graph.add((URIRef('URI'), skos['related'], URIRef('URI-Related')))

print(graph.serialize(format='pretty-xml'))

file = open('testfile.xml','w') 

file.write(str(graph.serialize(format='pretty-xml')))