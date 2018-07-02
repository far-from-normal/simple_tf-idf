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

After the initialization is complete, running the search engine with the default initialization parameters for 

```
shakespeare
```

should return

```
  1. (31.27)	Five histories, William Shakespeare,William Shakespeare,William Shakespeare,William Shakespeare,William Shakespeare,William Shakespeare

  2. (26.06)	Five tragedies, William Shakespeare,William Shakespeare,William Shakespeare,William Shakespeare,William Shakespeare

  3. (26.06)	Shakespeare day; report of meeting, organised by the Shakespeare association, held at King's college, University of London, on May 3, 1917, to promote an annual Shakespeare day in the schools and other institutions, Shakespeare Association (Great Britain),Shakespeare Association (Great Britain)

  4. (20.84)	Shakespeare day; report of meeting, organised by the Shakespeare association, held at King's college, University of London, on May 3, 1917, to promote an annual Shakespeare day in the schools and other institutions, Shakespeare Association (Great Britain)

  5. (20.84)	A catalogue of the books, manuscripts, works of art, antiquities and relics, illustrative of the life and works of Shakespeare, and of the history of Stratford-upon-Avon; which are preserved in the Shakespeare Library and Museum in Henley Street, Shakespeare Birthplace Trust,Shakespeare Memorial (Stratford-upon-Avon, England). Library

  6. (20.84)	Plays of Mr. William Shakespeare : as re-written or re-arranged by his successors of the restoration period as presented at the Dukes theatre and elsewhere circa 1664-1669; being the text of these so-restored plays with the First folio Shakespeare te, William Shakespeare,Appleton Morgan,Willis Vickery,Shakespeare Society of New York

  7. (15.63)	The old-spelling Shakespeare: being the works of Shakespeare in the spelling of the best quarto and folio texts; ed. by F.J. Furnivall and the late W.G. Boswell-Stone, William Shakespeare,Frederick James Furnivall,W. G. (Walter George) Boswell-Stone

  8. (15.63)	Shakespeare's Comedy of A Midsummer Night's Dream, William Shakespeare , Shakespeare, Israel Gollancz, McMahon

  9. (15.63)	The comedies, histories, and tragedies of Mr. William Shakespeare as presented at the Globe and Blackfriars Theatres, circa 1591-1623 : being the text furnished the players, in parallel pages with the first revised folio text, with critical introduct, William Shakespeare,Appleton Morgan,Rogers, Bruce, former owner. DLC,Shakespeare Society of New York,Pforzheimer Bruce Rogers Collection (Library of Congress) DLC

 10. (15.63)	Plays of Mr. William Shakespeare : as re-written or re-arranged by his successors of the restoration period as presented at the Dukes theatre and elsewhere circa 1664-1669; being the text of these so-restored plays with the First folio Shakespeare te, William Shakespeare,Appleton Morgan,Willis Vickery


 Top 10 results requested. Only 10 documents match the search criteria. Search completed in 1.565483808517456 seconds.
```

In general, searches can accept multiple terms, serarated by spaces.

The end­ of­ file character (^d) will terminate the search engine session.

## Authors

* **Jason Boulet** - *Initial work* - [far-from-normal](https://github.com/far-from-normal)


## License

This project is licensed under the MIT License.