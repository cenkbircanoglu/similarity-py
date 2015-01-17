Clustering
==========
Data mining Examples

###Distances

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

#####&nbsp;&nbsp;<em>Hamming Distance</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   ["abc", "cba"] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:  gives the number of elements whose values disagree in u and v.

#####&nbsp;&nbsp;<em>Jaccard Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a,b,c}, {c,b,a}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**: is defined as the size of the intersection divided by the size of the union of the sample sets.

#####&nbsp;&nbsp;<em>Matching Dissimilarity</em>

  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Data**:   [{a,b,c}, {c,b,a}] <br/>
  &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;**Explanation**:[u,v]  is equivalent to (n10+n01)/Length[u], where  is the number of corresponding pairs of elements in u and v respectively equal to i and j.






##Testing


Run all tests:
```bash
    $ python -m unittest discover -s tests -p '*_test.py'
```



