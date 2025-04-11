This section deals with processing data for 4-letter idioms

main source:
https://www.edrdg.org/projects/yojijukugo.html

the python file here, `yoji_fixer.py` formats an entry from this list into an acceptable format for Anki

expected input format (from an example line)
屁理屈屋 [へりくつや] /(n) quibbler

output (tabs written out for visibility)
/tへりくつや/t屁理屈屋/tquibbler

! This allows anki to import as a TSV.
! Initial testing shows pattern works.
! selection of "appropriate" phrases and orgnaization of material still requires human judgment...
