from rdflib import Graph

g = Graph()
g.parse("lab.ttl", format="turtle")
print("File parsed OK")
print("Triple count:", len(g))

q1 = """
PREFIX lab:  <http://example.org/lab#>
PREFIX data: <http://example.org/lab/data/>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?name ?date WHERE {
  ?b lab:bookedEquipment data:M1 ;
     lab:bookedBy ?r ;
     lab:bookingDate ?date .
  ?r rdfs:label ?name .
}
"""
print("\nWho booked M1:")
for row in g.query(q1):
    print(row.name, row.date)

q2 = """
PREFIX lab:  <http://example.org/lab#>
PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#>
SELECT ?person ?equip WHERE {
  ?r lab:holdsCertificate ?c ;
     rdfs:label ?person .
  ?c lab:certifiesFor ?e .
  ?e rdfs:label ?equip .
}
"""
print("\nWho is certified for what:")
for row in g.query(q2):
    print(row.person, "->", row.equip)