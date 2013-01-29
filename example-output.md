Example output
==============

Minimum number of edges
-----------------------

`python random_connected_graph.py -p -g names.gml names.txt`

### Console

    [('Anil', 'Patrick'),
     ('Anil', 'Siamak'),
     ('Bandita', 'Siamak'),
     ('Brendan', 'Yi'),
     ('Chengyuan', 'Keshavan'),
     ('Karthik', 'Siamak'),
     ('Keshavan', 'Siamak'),
     ('Keshavan', 'Wesley'),
     ('Rohith', 'Wesley'),
     ('Samuel', 'Shibamouli'),
     ('Samuel', 'Siamak'),
     ('Samuel', 'Yi'),
     ('Saratchandra', 'Wesley'),
     ('Shibamouli', 'Vibha'),
     ('Siamak', 'Siddanth')]

### GML file

    graph [
        node [
            id 0
            label "Anil"
        ]
        node [
            id 1
            label "Bandita"
        ]
        node [
            id 2
            label "Brendan"
        ]
        node [
            id 3
            label "Chengyuan"
        ]
        node [
            id 4
            label "Karthik"
        ]
        node [
            id 5
            label "Keshavan"
        ]
        node [
            id 6
            label "Patrick"
        ]
        node [
            id 7
            label "Rohith"
        ]
        node [
            id 8
            label "Samuel"
        ]
        node [
            id 9
            label "Saratchandra"
        ]
        node [
            id 10
            label "Shibamouli"
        ]
        node [
            id 11
            label "Siamak"
        ]
        node [
            id 12
            label "Siddanth"
        ]
        node [
            id 13
            label "Vibha"
        ]
        node [
            id 14
            label "Wesley"
        ]
        node [
            id 15
            label "Yi"
        ]
        edge [
            source 0
            target 11
        ]
        edge [
            source 8
            target 11
        ]
        edge [
            source 5
            target 11
        ]
        edge [
            source 4
            target 11
        ]
        edge [
            source 1
            target 11
        ]
        edge [
            source 5
            target 14
        ]
        edge [
            source 7
            target 14
        ]
        edge [
            source 0
            target 6
        ]
        edge [
            source 3
            target 5
        ]
        edge [
            source 9
            target 14
        ]
        edge [
            source 8
            target 10
        ]
        edge [
            source 8
            target 15
        ]
        edge [
            source 2
            target 15
        ]
        edge [
            source 11
            target 12
        ]
        edge [
            source 10
            target 13
        ]
    ]

### Image from GML

![names with minimum number of edges](http://s8.postimage.org/4gqe0u61x/names.png)

20 edges
--------

`python random_connected_graph.py -p -e 20 -g names.gml names.txt`

### Image from GML

![names with 20 edges](http://s1.postimage.org/5lggangf3/names_20.png)

Generate nodes
--------------

`python random_connected_graph.py -p 16`

    [(0, 7),
     (0, 8),
     (1, 2),
     (1, 4),
     (1, 12),
     (3, 9),
     (3, 10),
     (3, 12),
     (4, 6),
     (5, 8),
     (5, 12),
     (6, 13),
     (7, 11),
     (12, 14),
     (14, 15)]
