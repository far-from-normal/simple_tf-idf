# Simple tf-idf

This is a simple Python text-based search engine that returns ranked documents based on the Term Frequency-Inverse Document Frequency (ft-idf) algorithm.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

This project only requires a base installation of Python 3.5.

### Installing

Download the project to a local folder.

In a terminal, cd into the current project directory.

Make search engine executable on a Unix-based machine:

```
chmod a+x run_search_engine.py
```

## Initializing the search engine

In a terminal, cd into the current project directory.

Initializing the search engine with no arguments:

```
./run_search_engine.py
```

will default to building an index with the included database "documents.txt", returning the top 10 results, and using the raw term frequency.

Initializing the search engine can take the three agruments:

```
./run_search_engine.py <path_to_database> <top_N_results> <term_frequency_type>
```
where top_N_results is an integer and term_frequency_type={raw, bool, norm, log, aug}.

Initializing the search engine should take approximatley 1 minute.

## Running the search engine

After the initialization with the default parameters is complete, running the search engine for 

```
shakespeare
```

should return

```
  1. (20.86)	Plays of Mr. William Shakespeare : as re-written or re-arranged by his successors of the restoration period as presented at the Dukes theatre and elsewhere circa 1664-1669; being the text of these so-restored plays with the First folio Shakespeare te, William Shakespeare,Appleton Morgan,Willis Vickery,Shakespeare Society of New York

  2. (15.64)	Shakespeare's Comedy of A Midsummer Night's Dream, William Shakespeare , Shakespeare, Israel Gollancz, McMahon

  3. (15.64)	Plays of Mr. William Shakespeare : as re-written or re-arranged by his successors of the restoration period as presented at the Dukes theatre and elsewhere circa 1664-1669; being the text of these so-restored plays with the First folio Shakespeare te, William Shakespeare,Appleton Morgan,Willis Vickery

  4. (15.64)	Plays of Mr. William Shakespeare as re-written or re-arranged by his successors of the restoration period as presented at the Dukes theatre and elsewhere circa 1664-1669; being the text of these so-restored plays with the First folio Shakespeare text, William Shakespeare,Appleton Morgan,Willis Vickery

  5. (15.64)	The dramatic works of William Shakespeare : accurately printed from the text of the corrected copy left by the late George Steevens, Esq. : with a glossary, and notes, and a sketch of the life of Shakespeare, William Shakespeare,George Steevens

  6. (15.64)	Shakespeare's poems: Venus and Adonis, Lucrece, Sonnets, etc, William Shakespeare,W. J. (William James) Rolfe,William Shakespeare

  7. (15.64)	The Shakespeare apocrypha; being a collection of fourteen plays which have been ascribed to Shakespeare. Edited with introd., notes and bibliography by C.F. Tucker Brooke, Charles Frederick Tucker Brooke,William Shakespeare

  8. (15.64)	Shakespeare's King Lear, Harold Bloom,William. King Lear Shakespeare,Harold. Shakespeare Bloom

  9. (15.64)	Shakespeare's songs, William Shakespeare, Arthur Henry Bullen, Shakespeare Head Press

 10. (15.64)	Shakespeare's Julius Caesar, Harold Bloom,Harold. Shakespeare Bloom,William. Julius Caesar Shakespeare


 Top 10 results requested. Only 10 documents match the search criteria. Search completed in 1.6247971057891846 seconds.
```

In general, searches can accept multiple terms, serarated by spaces.

The end­ of­ file character (^d) will terminate the search engine session.

## Authors

* **Jason Boulet** - *Initial work* - [far-from-normal](https://github.com/far-from-normal)


## License

This project is licensed under the MIT License.