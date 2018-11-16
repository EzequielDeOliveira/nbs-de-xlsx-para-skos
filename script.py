import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from parentNodeByNbsCode import parentCodeByNbs
from slugify import slugify

file = 'NBS-e-NEBS-em-excel.xlsx'


xl = pd.ExcelFile(file)

# print(xl.sheet_names)
filesempai = open('sempai.txt','w') 

nebs = xl.parse('NEBS')

graph = Graph()
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
graph.bind('skos', skos)
i = 0

def nodeByDescription(nbsDescription):
    return URIRef('http://vocab.mdic.gov.br/NBS/v2.0/#' + slugify(nbsDescription))
    
nbsCodeDescDict = {'1':'NBS 2.0'}

for a in range(len(nebs)):
    i += 1

    nbsCodeDescDict[nebs.NBS2.get(a)] = nebs.DESCRIÇÃO.get(a)

    uri = nodeByDescription(nebs.DESCRIÇÃO.get(a))
    parentCode = parentCodeByNbs(nebs.NBS2.get(a))

    try:
        uriParent = nodeByDescription(nbsCodeDescDict[parentCode])
    except:
        filesempai.write("Pai não encontrado! Pai: " + parentCode + ' Filho: ' + nebs.NBS2.get(a) + '\n')

    graph.add((uri, RDF['type'], skos['Concept']))
    graph.add((uri, skos['prefLabel'], Literal(nebs.DESCRIÇÃO.get(a), lang='pt-br')))
    
    graph.add((uri, skos['broader'], uriParent))
    

# print(graph.serialize(format='pretty-xml'))

file = open('NBS2-skos.nt','w') 

file.write(str(graph.serialize(format='nt')))
