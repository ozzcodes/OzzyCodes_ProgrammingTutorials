import tensorflow as tf
from graphviz import Digraph

g = tf.Graph()
with g.as_default():
    a = tf.placeholder(tf.float32, name="a")
    b = tf.placeholder(tf.float32, name="b")
    c = a + b

dot: Digraph = Digraph()

for n in g.as_graph_def().node:
    # Each node has a name and a label. The name identifies the node
    # while the label is what will be displayed in the graph.
    # We're using the name as a label for simplicity.
    dot.node(n.name, label=n.name)

    for i in n.input:
        # Edges are determined by the names of the nodes
        dot.edge(i, n.name)

dot
