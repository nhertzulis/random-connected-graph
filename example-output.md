Example output
==============

Minimum number of edges
-----------------------

`python random_connected_graph.py -p -g names.gml names.txt`

### Console

    [('Anil', 'Rohith'),
     ('Anil', 'Wesley'),
     ('Bandita', 'Saratchandra'),
     ('Brendan', 'Vibha'),
     ('Chengyuan', 'Karthik'),
     ('Karthik', 'Patrick'),
     ('Karthik', 'Yi'),
     ('Keshavan', 'Wesley'),
     ('Patrick', 'Siamak'),
     ('Patrick', 'Vibha'),
     ('Rohith', 'Saratchandra'),
     ('Samuel', 'Saratchandra'),
     ('Samuel', 'Shibamouli'),
     ('Siamak', 'Siddanth'),
     ('Siamak', 'Wesley')]

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
            target 7
        ]
        edge [
            source 0
            target 14
        ]
        edge [
            source 1
            target 9
        ]
        edge [
            source 2
            target 13
        ]
        edge [
            source 3
            target 4
        ]
        edge [
            source 4
            target 6
        ]
        edge [
            source 4
            target 15
        ]
        edge [
            source 5
            target 14
        ]
        edge [
            source 6
            target 11
        ]
        edge [
            source 6
            target 13
        ]
        edge [
            source 7
            target 9
        ]
        edge [
            source 8
            target 9
        ]
        edge [
            source 8
            target 10
        ]
        edge [
            source 11
            target 12
        ]
        edge [
            source 11
            target 14
        ]
    ]

### Image from GML

![names with minimum number of edges](http://s3.postimage.org/ps02l9yj7/names.png)

20 edges
--------

`python random_connected_graph.py -p -e 20 -g names.gml names.txt`

### Image from GML

![names with 20 edges](http://s14.postimage.org/i2sj3aujl/names_20.png)

Generate nodes
--------------

`python random_connected_graph.py -p 16`

    [(0, 6),
     (0, 10),
     (1, 4),
     (1, 9),
     (2, 4),
     (2, 11),
     (3, 6),
     (3, 8),
     (4, 8),
     (5, 8),
     (5, 15),
     (7, 11),
     (10, 12),
     (13, 15),
     (14, 15)]
