from rdflib import Graph, Literal, URIRef, RDFS
import networkx as nx
import matplotlib.pyplot as plt

g = Graph()
g.parse("lab.ttl", format="turtle")

start = URIRef("http://example.org/lab/data/Booking1")

def name(x):
    return str(x) if isinstance(x, Literal) else g.qname(x)

def skip(p, o):
    # hide labels and rdfs:Class clutter
    return p == RDFS.label or o == RDFS.Class

# collect nodes within 2 steps of Booking1
keep = {start}
frontier = {start}
for _ in range(2):
    nxt = set()
    for s in frontier:
        for p, o in g.predicate_objects(s):
            if not skip(p, o):
                nxt.add(o)
    keep |= nxt
    frontier = nxt

# build the drawing graph
G = nx.DiGraph()
for s, p, o in g:
    if not skip(p, o) and s in keep and o in keep:
        G.add_edge(name(s), name(o), label=name(p))

literals = [name(n) for n in keep if isinstance(n, Literal)]
classes = [n for n in G.nodes if n.startswith("lab:")]
resources = [n for n in G.nodes if n not in literals and n not in classes]

# manual layout so no arrow passes behind another node
manual = {
    "data:Booking1": (0, 0),
    "lab:Booking": (-2.5, 0),
    "2026-10-12": (-1.2, 1.8),
    "data:M1": (3, 1),
    "lab:Microscope": (3, 3),
    "data:R201": (5.8, 2),
    "Available": (5.8, 0.8),
    "data:Ravi": (5.8, -0.4),
    "data:Anu": (0, -2.5),
    "lab:Researcher": (-2.5, -2.5),
    "data:Cert1": (3, -1.6),
    "data:BioFilm": (0, -4.5),
}
missing = [n for n in G.nodes if n not in manual]
if missing:
    print("WARNING: nodes without a manual position:", missing)
pos = {n: manual.get(n, (0, 0)) for n in G.nodes}

plt.figure(figsize=(18, 12))
nx.draw_networkx_nodes(G, pos, nodelist=resources, node_shape="o",
                       node_color="white", edgecolors="black", node_size=4500)
nx.draw_networkx_nodes(G, pos, nodelist=classes, node_shape="o",
                       node_color="lightblue", edgecolors="black", node_size=4500)
nx.draw_networkx_nodes(G, pos, nodelist=literals, node_shape="s",
                       node_color="lightyellow", edgecolors="black", node_size=4500)
nx.draw_networkx_labels(G, pos, font_size=10)
nx.draw_networkx_edges(G, pos, arrows=True, arrowsize=20, node_size=4500)
nx.draw_networkx_edge_labels(
    G, pos,
    edge_labels=nx.get_edge_attributes(G, "label"),
    font_size=9, label_pos=0.45,
    bbox=dict(facecolor="white", edgecolor="none", alpha=0.9),
)

# legend
plt.scatter([], [], s=200, c="white", edgecolors="black", label="Resource (instance)")
plt.scatter([], [], s=200, c="lightblue", edgecolors="black", label="Class")
plt.scatter([], [], s=200, c="lightyellow", edgecolors="black", marker="s", label="Literal value")
plt.legend(loc="upper left", fontsize=10)

plt.margins(0.15)
plt.axis("off")
plt.title("Subgraph of lab.ttl centred on Booking1", fontsize=14)
plt.savefig("graph.png", dpi=200, bbox_inches="tight")
print("Saved graph.png")