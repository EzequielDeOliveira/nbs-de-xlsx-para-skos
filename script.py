import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from parentNodeByNbsCode import parentCodeByNbs
from slugify import slugify

def nodeByDescription(nbsDescription):
    return URIRef('http://vocab.mdic.gov.br/NBS/v2.0/' + slugify(nbsDescription))


file = 'NBS-e-NEBS-em-excel.xlsx'

xl = pd.ExcelFile(file)

# print(xl.sheet_names)
filesempai = open('sempai.txt','w') 

nebs = xl.parse('NEBS')

graph = Graph()
skos = Namespace('http://www.w3.org/2004/02/skos/core#')
dct = Namespace('http://purl.org/dc/elements/1.1')

graph.bind('skos', skos)
graph.bind('dct', dct)
i = 0

# esquema = URIRef('http://vocab.mdic.gov.br/NBS/v2.0/#esquema')
    
nbsCodeDescDict = {'1':'Nomenclatura Brasileira de Serviços'}


uri = nodeByDescription('Nomenclatura Brasileira de Serviços')
graph.add((uri, RDF['type'], skos['Concept']))
graph.add((uri, skos['prefLabel'], Literal('Nomenclatura Brasileira de Serviços', lang='en')))
# graph.add((uri, skos['inScheme'], esquema))

for a in range(len(nebs)):
    i += 1

    nbsCodeDescDict[nebs.NBS2.get(a)] = nebs.DESCRIÇÃO.get(a)

    uri = nodeByDescription(nebs.DESCRIÇÃO.get(a))
    parentCode = parentCodeByNbs(nebs.NBS2.get(a))

    try:
        uriParent = nodeByDescription(nbsCodeDescDict[parentCode])
    except:
        filesempai.write("Pai não encontrado! Pai: " + parentCode + ' Filho: ' + nebs.NBS2.get(a) + '\n')

    # if parentCode != '1':
    graph.add((uri, skos['broader'], uriParent))
    # else:
    #     graph.add((uri, skos['topConceptOf'], esquema))
    #     graph.add((esquema, skos['hasTopConcept'], uri))

    graph.add((uri, skos['prefLabel'], Literal(nebs.DESCRIÇÃO.get(a), lang='en')))
    graph.add((uri, RDF['type'], skos['Concept']))
    
    # graph.add((uri, skos['inScheme'], esquema))


# graph.add((esquema, RDF['type'], skos['ConceptScheme']))
# graph.add((esquema, dct['title'], Literal('Nomeclatura Brasileira de Serviços', lang='en')))



# print(gnbsh.serialize(format='pretty-xml'))
graph.serialize(destination='NBS2-skos.xml', format='pretty-xml')


