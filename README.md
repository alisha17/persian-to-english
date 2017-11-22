# Back-transliteration of Persian names to English names

This repo has the project specifications, code and the final report.

Run this project by this command:

```python
python edit_distance.py
```

1) Edit the paths in the code where we are opening the files, namely train.txt and names.txt.

   ```python
   with open('/home/alisha/Desktop/KT/2017S1-90049P1-data-dos/train.txt') as f:
   ```
    --> Change it to the path where the files reside in your system.

   ```python
   with open('/home/alisha/Desktop/KT/2017S1-90049P1-data-dos/names.txt') as f:
   ```
    --> Here also

   **NOTE: I HAVE NOT ATTACHED THE DATASETS AS THEY ARE NON-REPRODUCIBLE. HOWEVER, SIMILAR DATASETS ARE EASILY AVAILABLE ONLINE**

2) To test the output files, precision and recall for the following methods:

   a) ** Levenshtein Distance **:
      The distance() method calculates this. Simply run the python script and you will get 'edited.txt' output file in the folder where you are running the script and the precision and recall will get printed on the terminal/console.

   b) ** Jaccard Index **:
      Uncomment the following:
      ```python
      import distance
      edit_dist = distance.jaccard(ke, item)
      ```
      And now run the python script.

   c) ** Modification of BLOSUM matrix in combination with Soundex method **
      Uncomment the following:
      ```python
      edit_dist = matchWords(ke, item)
      ```
      And now run the python script.
      Note: This method will take longer than the other ones.

This was a part of my academic course 'Knowledge Technologies'. The lecture sets are here: [blog](https://alisha17.github.io/machine-learning/2017/11/20/pyladies.html)
