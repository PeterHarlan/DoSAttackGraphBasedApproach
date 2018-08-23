Time seperated by 1.25 sec 
Day one data from 8:52:52 to 11:50:59

+++++++++++++++++++++++++++++++
NORM 1

MDL
	No signifigant data

PROB
	No signifigant data

+++++++++++++++++++++++++++++++
NORM 4

MDL
	No signifigant data

PROB
	No signifigant data

+++++++++++++++++++++++++++++++
NORM 9
Substructure: value = 1.02625, instances = 304
	Graph(6v,5e):
		v 1 "Internet"
		v 2 "External Web"
		v 3 "Internet"
		v 4 "Internet"
		v 5 "Internet"
		v 6 "Internet"
		d 1 2 "mid"
		d 3 2 "mid"
		d 4 2 "mid"
		d 5 2 "mid"
		d 6 2 "mid"

MDL
	Flagged the DOS attack IN action (11:50) where internet to external web had a edge of high

PROB
	Alot of anomaly were found but none fo them were in the DOS attack range
	

+++++++++++++++++++++++++++++++
NORM 12
Substructure: value = 1.01953, instances = 319
  Graph(5v,4e):
    v 1 "External Web"
    v 2 "Internet"
    v 3 "Internet"
    v 4 "Internet"
    v 5 "Internet"
    d 2 1 "mid"
    d 3 1 "mid"
    d 4 1 "mid"
    d 5 1 "mid"

MDL
	Flagged the DOS attack IN action (11:50) where internet to external web had a edge of high

PROB
	Alot of anomaly were found but none fo them were in the DOS attack range


+++++++++++++++++++++++++++++++
NORM 15
7 initial substructures
Normative Pattern (15):
Substructure: value = 1.01656, instances = 1091
  Graph(4v,3e):
    v 1 "DHCP"
    v 2 "Workstation"
    v 3 "Workstation"
    v 4 "Workstation"
    d 2 1 "mid"
    d 3 1 "mid"
    d 4 1 "mid"

MDL
	No signifigant data

PROB
	Alot of anomaly were found but none fo them were in the DOS attack range

