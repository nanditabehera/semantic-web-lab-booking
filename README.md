# CSE4007 Semantic Web Assignment
**Option 2, Case 2B: Research Laboratory Equipment Booking**

## What this is
An RDF graph written in Turtle that describes a university research lab: equipment, rooms, researchers, projects, training certificates, bookings and a maintenance event. It includes an RDFS vocabulary (classes, subclasses, properties, domain and range) and sample data.

## Files
| File | Purpose |
|---|---|
| `lab.ttl` | The RDF graph: RDFS vocabulary plus instance data |
| `validate.py` | Checks the file parses, prints the triple count, runs 2 SPARQL queries |
| `graph.py` | Draws the subgraph around Booking1 and saves it as `graph.png` |
| `graph.png` | The drawn subgraph used in the report |

## Tools used
- VS Code (to write the Turtle file and run the scripts)
- Python 3 with the libraries `rdflib`, `networkx` and `matplotlib`

## How to reproduce

1. Put all files in one folder and open that folder in VS Code.
2. Open a terminal (Terminal > New Terminal) and install the libraries once:
```
   pip install rdflib networkx matplotlib
```
3. Validate the Turtle file:
```
   python validate.py
```
   Expected output: `File parsed OK`, the triple count, the booking of M1 (Anu, 2026-10-12), and the list of who is certified for which equipment.
4. Regenerate the graph picture:
```
   python graph.py
```
   This saves `graph.png`. The node positions in `graph.py` are set by hand for readability and only fit the Booking1 subgraph.

## Namespaces
- `lab:` = `http://example.org/lab#` (vocabulary: classes and properties)
- `data:` = `http://example.org/lab/data/` (individual records)

## Notes
- All people, equipment and dates are fictional.
- RDFS only. No OWL reasoning is used in this option.

## Sources
Course material for CSE4007 and the W3C RDF 1.1 Turtle and RDFS specifications.