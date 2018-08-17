



my 

first steps learning python based on igc_lib https://github.com/xiadz/igc_lib?files=1





clone and install a couple psckages 
run CompAnalysis.py
next Step
- allow xctrsck task file to be loaded
- create outputfile with ranking


simplesimple library to parse IGC logs and extract thermals.

Uses ground speed to detect flight and aircraft bearing rate of
change to detect thermalling. Both are smoothed using the
Viterbi algorithm.

The code has been battle-tested against a couple hundred thousand
IGC files. Detects various anomalies in the logs and marks files
as suspicious/invalid, providing an explaination for the decision.
If you find an IGC file on which the library misbehaves please
open a GitHub issue, we'd be happy to investigate.



```
  python CompAnalysis.py
```
