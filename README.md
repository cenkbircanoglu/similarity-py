Similarity Py [![Build Status](https://travis-ci.org/cenkbircanoglu/similarityPy.svg?branch=master)](https://travis-ci.org/cenkbircanoglu/similarityPy)  [![Coverage Status](https://coveralls.io/repos/cenkbircanoglu/similarityPy/badge.svg?branch=master)](https://coveralls.io/r/cenkbircanoglu/similarityPy?branch=master)
===================

###Distance Algorithms

####&nbsp;Numerical Data


#####&nbsp;&nbsp;<em>Norm</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/norm.gif)

#####&nbsp;&nbsp;<em>Manhattan Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/manhattan_distance.gif)


#####&nbsp;&nbsp;<em>Euclidean Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/euclidean_distance.gif)

#####&nbsp;&nbsp;<em>Squared Euclidean Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/squared_euclidean_distance.gif)

#####&nbsp;&nbsp;<em>Normalized Squared Euclidean Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b}, {x, y}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/normalized_squared_euclidean_distance.gif)

#####&nbsp;&nbsp;<em>Chessboard Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/chessboard_distance.gif)

#####&nbsp;&nbsp;<em>Bray Curtis Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/bray_curtis_distance.gif)

#####&nbsp;&nbsp;<em>Canberra Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/canberra_distance.gif)

#####&nbsp;&nbsp;<em>Cosine Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/cosine_distance.gif)

#####&nbsp;&nbsp;<em>Correlation Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Formula**:  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/correlation_distance.gif)


####&nbsp;Boolean Data


#####&nbsp;&nbsp;<em>Jaccard Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] is equivalent to  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/jaccard_dissimilarity.png), where n<sub>ij</sub> is the number of corresponding pairs of elements in u and v respectively equal to i and j.

#####&nbsp;&nbsp;<em>Matching Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v]  is equivalent to (n<sub>10</sub>+n<sub>01</sub>)/Length[u], where n<sub>ij</sub> is the number of corresponding pairs of elements in u and v respectively equal to i and j.

#####&nbsp;&nbsp;<em>Dice Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] is equivalent to  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/dice_dissimilarity.png), where n<sub>ij</sub> is the number of corresponding pairs of elements in u and v respectively equal to i and j.

#####&nbsp;&nbsp;<em>Rogers Tanimoto Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] is equivalent to  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/rogers_tanimoto_dissimilarity.png), where n<sub>ij</sub> is the number of corresponding pairs of elements in u and v respectively equal to i and j.

#####&nbsp;&nbsp;<em>Russell Rao Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] is equivalent to (n<sub>10</sub>+n<sub>01</sub>+n<sub>00</sub>)/Length[u], where n<sub>ij</sub> is the number of corresponding pairs of elements in u and v respectively equal to i and j.

#####&nbsp;&nbsp;<em>Sokal Sneath Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] is equivalent to  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/sokal_sneath_dissimilarity.png), where n<sub>ij</sub> is the number of corresponding pairs of elements in  and  respectively equal to i and j.

#####&nbsp;&nbsp;<em>Yule Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{True,False,True}, {True,True,False}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] is equivalent to  ![alt tag](https://raw.githubusercontent.com/cenkbircanoglu/clustering/master/images/yule_dissimilarity.png), where n<sub>ij</sub> is the number of corresponding pairs of elements in  and  respectively equal to i and j.

####&nbsp;String Data


#####&nbsp;&nbsp;<em>Hamming Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] gives the number of elements whose values disagree in u and v.

#####&nbsp;&nbsp;<em>Edit Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] gives the number of one-element deletions, insertions, and substitutions required to transform u to v.

#####&nbsp;&nbsp;<em>Damerau Levenshtein Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] gives the number of one-element deletions, insertions, substitutions, and transpositions required to transform u to v.

#####&nbsp;&nbsp;<em>Needleman Wunsch Similarity</em> (Not Implemented Yet)

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] finds an optimal global alignment between the elements of u and v, and returns the number of one-element matches.

#####&nbsp;&nbsp;<em>Smith Waterman Similarity</em> (Not Implemented Yet)

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a, b, c}, {x, y, z}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v] finds an optimal local alignment between the elements of u and v, and returns the number of one-element matches.


##Testing


Run all tests:
```bash
    $ python -m unittest discover -s tests -p '*_test.py'
```

Start test with nose and code coverage:
```bash
    $ nosetests --with-cov  --cov-report html  --cov  apps tests/
```


